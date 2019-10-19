import os
import random
import math
from shutil import copy

def main():
    folders = os.listdir(os.getcwd() + "\\data\\dataset")

    for i in folders:
        images = os.listdir(os.getcwd() + "\\data\\dataset\\" + i)
        for j in images:
            print(j)
            randNum = random.randint(1, 10)
            if randNum <= 8:
                copy(os.getcwd() + "\\data\\dataset\\" + i + "\\" + j, os.getcwd() + "\\data\\training\\" + i + "\\" + j)
            else:
                copy(os.getcwd() + "\\data\\dataset\\" + i + "\\" + j, os.getcwd() + "\\data\\testing\\" + i + "\\" + j)

if __name__ == "__main__":
    main()