import time
length = int(input("Enter array length: "))
mode = input("Choose mode: ").lower()
arr = [0] * length

def main():
    if mode == "left" or mode == "l":
        arr = [0] * length
        printLeft(arr)
    elif mode == "right" or mode == "r":
        arr = [0] * length
        printRight(arr)
    elif mode == "in":
        arr = [0] * length
        printIn(arr)
    elif mode == "out":
        arr = [0] * length
        printOut(arr)
    elif mode == "loopr":
        arr = [0] * length
        pos = int(input("Enter position: "))
        printLoopRight(arr, pos)
    elif mode == "loopl":
        arr = [0] * length
        pos = int(input("Enter position: "))
        printLoopLeft(arr, pos)
    elif mode == "loopout":
        arr = [0] * length
        pos = int(input("Enter position: "))
        printLoopOut(arr, pos)
    elif mode == "reading":
        arr = [[0 for i in range(length)] for j in range(length)]
        # printSquare(arr)
        print2dReading(arr)
    
def printLeft(arr):
    for i in reversed(range(0, length)):
        arr[i] = 1
        printArray(arr)

def printRight(arr):
    for i in range(0, length):
        arr[i] = 1
        printArray(arr)

def printOut(arr):
    for k in reversed(range(0,(length+1)//2)):
        arr[k] = 1
        arr[length-1-k] = 1
        printArray(arr)

def printIn(arr):
    for k in range(0,(length+1)//2):
        arr[k] = 1
        arr[length-1-k] = 1
        printArray(arr)

def printLoopRight(arr, pos):
    for k in range(pos, pos+length):
        arr[k%length] = 1
        printArray(arr)

def printLoopLeft(arr, pos):
    for k in range(pos, pos-length, -1):
        arr[k%length] = 1
        printArray(arr)

def printLoopOut(arr, pos):
    for k in range(pos, pos+(length+1)//2):
        arr[k%length] = 1
        arr[(pos*2-k)%length] = 1
        printArray(arr)

def print2dReading(arr):
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            arr[x][y] = 1
            printSquare(arr)

def printSquare(arr):
    print("square\n")
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            printBlock(arr[x][y])
        # print(end="\r")
        print()
        
    # time.sleep(0.5)

def printArray(arr):
    print("[", end="")
    for x in arr:
        printBlock(x)
    print("]", end="")
    print(end="\r")
    time.sleep(0.5)

def printBlock(a):
    if a == 0:
        print("-", end="")
    else:
        print(chr(0x2588), end="")

main()