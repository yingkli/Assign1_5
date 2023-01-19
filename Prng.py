import time
import random


while True:
    time.sleep(1.0)
    # read content from prng-service.txt
    with open('prng-service.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
    f.closed

    if not line:
        continue
    # with "run" in txt, then generate a random number and overwrite to prng-service.txt 
    if "run" in line:
        print("Generating random number...")
        with open('prng-service.txt', 'w', encoding="utf-8") as f:
            time.sleep(1.0)
            f.write(f"{random.randint(0, 100)}\n")
        f.closed


