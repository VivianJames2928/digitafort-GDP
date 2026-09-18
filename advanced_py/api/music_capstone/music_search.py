"""
Music Search — simple capstone.

Search songs on iTunes using the free iTunes Search API.
It is 100% free and needs NO API key.

Run:  python music_search.py
"""

import json
import requests

BASE_URL = "https://itunes.apple.com/search"


def search_songs(term, limit=10):
    """Ask iTunes for songs matching the search term. Returns a list."""
    params = {"term": term, "entity": "song", "limit": limit}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()          # stop if the API returned an error
    return response.json()["results"]    # turn the JSON answer into a list


def show_songs(songs):
    """Print each song with a number next to it."""
    print(f"\nFound {len(songs)} song(s):\n")
    for i, song in enumerate(songs, start=1):
        price = song.get("trackPrice")
        price = f"${price}" if price is not None else "no price"
        album = song.get("collectionName", "single")
        print(f"{i}. {song['trackName']} - {song['artistName']} | {price} | {album}")


def save_favorites(songs, picks):
    """Save the picked songs to favorites.json."""
    favorites = []
    try:
        with open("favorites.json") as f:
            favorites = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    for pick in picks:
        index = int(pick) - 1            # users count from 1, lists from 0
        if 0 <= index < len(songs):
            song = songs[index]
            favorites.append({
                "title": song["trackName"],
                "artist": song["artistName"],
                "album": song.get("collectionName", ""),
            })

    with open("favorites.json", "w") as f:
        json.dump(favorites, f, indent=2)

    print(f"\nSaved {len(picks)} song(s) to favorites.json")


def main():
    print("=" * 50)
    print("MUSIC SEARCH — powered by the free iTunes API")
    print("=" * 50)

    while True:
        term = input("\nSearch for a song/artist (press Enter to quit): ").strip()
        if not term:
            break

        try:
            songs = search_songs(term)
            show_songs(songs)

            picks = input("Save numbers as favorites (1,3) or Enter to skip: ").strip()
            if picks:
                numbers = picks.split(",")
                save_favorites(songs, numbers)
        except requests.exceptions.RequestException as e:
            print(f"\nSomething went wrong: {e}\n")

    print("\nBye! Your favorites are in favorites.json.")


if __name__ == "__main__":
    main()