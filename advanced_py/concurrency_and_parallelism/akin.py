import time  
import threading 

def make_dish(name,minutes):
    print(f"we are making {name}   and it will take {minutes}")
    time.sleep(minutes)
    print(f"we are done cooking {name}")

dishes = ["rice","beans","yam"]

th = [threading.Thread(target=make_dish, args=(f"{value}",3))for value in dishes]


for t in th :
    t.start()
for t in th:
    t.join()

print("Kitchen finished. Total wall time .")
