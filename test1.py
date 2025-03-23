import time
import sys
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
    elif mode == "2drow":
        arr = [[0 for i in range(length)] for j in range(length)]
        print2dRow(arr)
    elif mode == "2dcol":
        arr = [[0 for i in range(length)] for j in range(length)]
        print2dCol(arr)
    elif mode == "2dzigzag":
        arr = [[0 for i in range(length)] for j in range(length)]
        print2dZigzag(arr)
    elif mode == "2ddiagonal":
        arr = [[0 for i in range(length)] for j in range(length)]
        print2dDiagonal(arr)
    elif mode == "2dantidiagonal":
        arr = [[0 for i in range(length)] for j in range(length)]
        print2dAntiDiagonal(arr)
    
def printLeft(arr):
    for i in reversed(range(len(arr))):
        arr[i] = 1
        printArray(arr)

def printRight(arr):
    for i in range(len(arr)):
        arr[i] = 1
        printArray(arr)

def printOut(arr):
    for k in reversed(range((length+1)//2)):
        arr[k] = 1
        arr[length-1-k] = 1
        printArray(arr)

def printIn(arr):
    for k in range((length+1)//2):
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

def print2dRow(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            arr[x][y] = 1
            printSquare(arr)

def print2dCol(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            arr[y][x] = 1
            printSquare(arr)

def print2dZigzag(arr):
    for x in range(len(arr)):
        if x%2 == 0: # odd row: print left to right
            for y in range(len(arr)):
                arr[x][y] = 1
                printSquare(arr)
        else: # even row: print right to left
            for y in reversed(range(len(arr))):
                arr[x][y] = 1
                printSquare(arr)

def print2dDiagonal(arr):
    for i in range(len(arr)):
        x = i
        y = 0
        for j in range(i+1):
            arr[x][y] = 1
            printSquare(arr)
            x -= 1
            y += 1
    z = len(arr)-1
    for i in range(1, len(arr)):
        y = i
        x = len(arr)-1
        for j in range(z):
            arr[x][y] = 1
            printSquare(arr)
            x -= 1
            y += 1
        z -= 1

def print2dAntiDiagonal(arr):
    z = 1
    for i in reversed(range(len(arr))):
        x = 0
        y = i
        for j in range(z):
            arr[x][y] = 1
            printSquare(arr)
            x += 1
            y += 1
        z += 1
    z = len(arr)-1
    for i in range(1, len(arr)):
        y = 0
        x = i
        for j in range(z):
            arr[x][y] = 1
            printSquare(arr)
            x += 1
            y += 1
        z -= 1

def printSquare(arr):
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            printBlock(arr[x][y])
        print()
    delete_multiple_lines(len(arr))
    time.sleep(0.1)

def printArray(arr):
    print("[", end="")
    for x in arr:
        printBlock(x)
    print("]", end="")
    print(end="\r")
    time.sleep(0.1)

def printBlock(a):
    if a == 0:
        print("-", end="")
    else:
        print(chr(0x2588), end="")

def delete_multiple_lines(n):
    """Delete the last line in the STDOUT."""
    for i in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

main()