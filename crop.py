import cv2
import numpy as np

def crop(input):
    og = cv2.imread(input)
    img = cv2.imread(input,0)
    flag = True
    count = 0
    rows,cols = img.shape
    for i in range(cols):
        pixel = img[i, 900]
        if pixel == 0:
            count+=1
        else:
            break
    end = rows - count
    if not count > end:
        crop = og[count:end,0:img.shape[1]]
        cv2.imwrite(input[:-4] + "_crop.jpg",crop)
    else:
        print(input, "failed")

def main():
    for i in range(1,125):
        file_name = "testfile/Test"+str(i)+".jpg"

        out = crop(file_name)



main()