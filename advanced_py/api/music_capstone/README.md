# Music Search — Simple API Capstone

A tiny program that searches songs on the **iTunes Search API** and lets
you save favorites to a JSON file. It runs in your terminal.

The best part: the iTunes API is **completely free and needs NO API key**.
No signups, no payments — you install one library and you're done.

---

## What you will learn

- What an API is, and what a `requests.get()` call does
- How query parameters work (`?term=...&limit=10`)
- How to read a JSON response in Python
- How to handle errors politely instead of crashing
- How to save data to a file so it survives a restart

---

## 1. Set it up

```bash
# 1. (optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. install the one library we need
pip install -r requirements.txt

# 3. run it
python music_search.py
```

---

## 2. Try it

```
==================================================
MUSIC SEARCH — powered by the free iTunes API
==================================================

Search for a song/artist (press Enter to quit): coldplay

Found 10 song(s):

1. Yellow - Coldplay | $1.29 | Parachutes
2. Viva La Vida - Coldplay | $1.29 | Viva La Vida or Death and All His Friends
3. A Sky Full of Stars - Coldplay | $1.29 | Ghost Stories
...

Save numbers as favorites (1,3) or Enter to skip: 1,3

Saved 2 song(s) to favorites.json
```

After quitting, open `favorites.json` — your picks are still there.

---

## 3. How the code works

Only **two real actions** happen:

### Searching (makes the API call)

```python
response = requests.get(BASE_URL, params=params, timeout=10)
response.raise_for_status()
songs = response.json()["results"]
```

Line by line:

| Line | Meaning |
|------|---------|
| `requests.get(...)` | sends a GET request to the API |
| `params=params` | turns your dict into `?term=coldplay&entity=song&limit=10` |
| `timeout=10` | give up after 10 seconds instead of waiting forever |
| `raise_for_status()` | crash with a clear message if the API returns a 404/500 |
| `.json()` | converts the JSON the API sends back into a Python list/dict |

### Saving favorites (writes to a file)

```python
favorites = json.load(...)   # read old favorites (if any)
favorites.append(song)       # add the new ones
json.dump(favorites, f, indent=2)   # write them back
```

That's the whole pattern: **ask the API → get JSON → use the data → save what you like.**

---

## 4. Real APIs often need a key (know the pattern)

`iTunes` is generous — no key required. But most real APIs (weather, maps,
Spotify, AI) ask you to register and get a **free API key**. The pattern
is always the same:

```python
params = {"q": term, "appid": "YOUR_FREE_KEY_HERE"}
response = requests.get("https://api.something.com/data", params=params)
```

`appid`, `key`, `api_key`, `apikey` — different APIs use different names,
but the idea is identical: you send your key with every request so the API
knows who you are and how many requests you've used.

---

## 5. Project files

| File | What it is |
|------|-----------|
| `music_search.py` | the whole program |
| `favorites.json` | created when you save favorites (don't hand in a filled one) |
| `requirements.txt` | the libraries to install |

---

## 6. Test yourself (mini challenges)

1. Add a `limit` option so the search returns 20 songs instead of 10.
2. Print the song's 30-second preview link (`song["previewUrl"]`).
3. Search **albums** instead of songs (change `"entity": "song"` to `"album"`).
4. Catch the case where a song's `trackName` key is missing (try `.get()`).

---

## 7. Quick troubleshooting

| Problem | Fix |
|---------|-----|
| `ModuleNotFoundError: requests` | run `pip install -r requirements.txt` |
| Hang forever on search | add/keep `timeout=10` |
| API error "not found" | check the spelling of the search term |
| `favorites.json` has weird data | delete the file, run again |

---

## Sponsor note to the teacher

This capstone is intentionally ~70 lines: one file, one API, no framework.
For the next step, students can swap in a key-required API (e.g. OpenWeatherMap)
or wrap the same function in a simple web endpoint with FastAPI.