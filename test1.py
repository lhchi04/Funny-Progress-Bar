import time
length = int(input("Enter array length: "))
mode = input("Choose mode: ").lower()
arr = [0] * length

def main():
    if mode == "left" or mode == "l":
        printLeft()
    elif mode == "right" or mode == "r":
        printRight()
    elif mode == "in":
        printIn()
    elif mode == "out":
        printOut()
    
def printLeft():
    for i in reversed(range(0, length)):
        arr[i] = 1
        printArray(arr)

def printRight():
    for i in range(0, length):
        arr[i] = 1
        printArray(arr)

def printOut():
    j = length//2
    i = (length-1)//2
    for k in range(0,(length+1)//2):
        arr[i] = 1
        arr[j] = 1
        i -= 1
        j += 1
        printArray(arr)

def printIn():
    j = 0
    i = length-1
    for k in range(0,(length+1)//2):
        arr[i] = 1
        arr[j] = 1
        i -= 1
        j += 1
        printArray(arr)

def printArray(arr):
    print("[", end="")
    for x in arr:
        printBlock(x)
    print("]", end="")
    print(end="\r")
    time.sleep(0.5)

def printBlock(x):
    if x == 0:
        print("-", end="")
    else:
        print(chr(0x2588), end="")

main()