import time

total_img = 6

while True:
    time.sleep(1.0)
    # read from image-service.txt
    with open('image-service.txt', 'r', encoding="utf-8") as f:
        line = f.readline()
    f.closed

    if not line:
        continue
    # if random number in txt, calculate the image number and write the path to txt
    try:
       int(line)
    except ValueError as e:
        pass
    else:
        print("Looking for image...")
        img_num = int(line) % total_img

        with open('image-service.txt', 'w', encoding="utf-8") as f:
            time.sleep(1.0)
            f.write(f"C:/Users/zhiya/Desktop/CS361/Assign1_5/imgs/{img_num}.jpg\n")
        f.closed


