import pygame
import os, sys
import copy
import random
from pygame.locals import *
from GUI_Functions import KEY_PRESSED
from Exceptions import ArraySizeError

def InsertionSort(MyArray, Win, Font, DrawSort=True):
    for arrayPosition in range(1, len(MyArray.Array)):
        actualElement = MyArray.Array[arrayPosition]  # Elemento que se compara.
        while arrayPosition > 0 and MyArray.Array[arrayPosition - 1] > actualElement:
            MyArray.Array[arrayPosition] = MyArray.Array[arrayPosition - 1]
            arrayPosition -= 1
            MyArray.Array[arrayPosition] = actualElement
            if DrawSort:
                MyArray.Moving_Elements = [MyArray.Array[arrayPosition]]
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font)

    if not MyArray.isSorted:
        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray

def CocktailShakerSort(MyArray, Win, Font, DrawSort=True):
    for i in range(len(MyArray.Array) - 1, 0, -1):
        Swapped = False
        for j in range(i, 0, -1):
            if MyArray.Array[j] < MyArray.Array[j - 1]:
                MyArray.Array[j], MyArray.Array[j - 1] = MyArray.Array[j - 1], MyArray.Array[j]
                MyArray.Moving_Elements = [MyArray.Array[j], MyArray.Array[j - 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        MyArray.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True
        for j in range(i):
            if MyArray.Array[j] > MyArray.Array[j + 1]:
                MyArray.Array[j], MyArray.Array[j + 1] = MyArray.Array[j + 1], MyArray.Array[j]
                MyArray.Moving_Elements = [MyArray.Array[j], MyArray.Array[j + 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        MyArray.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True
        if not Swapped:
            if not MyArray.isSorted:
                MyArray.Draw_Check_Sorted(Win, Font)

            MyArray.isSorted = True
            return MyArray

def BubbleSort(MyArray, Win, Font, DrawSort=True):
    Swapped = True
    while Swapped:
        Swapped = False
        for i in range(len(MyArray.Array) - 1):
            if MyArray.Array[i] > MyArray.Array[i + 1]:
                MyArray.Array[i], MyArray.Array[i + 1] = MyArray.Array[i + 1], MyArray.Array[i]
                MyArray.Moving_Elements = [MyArray.Array[i], MyArray.Array[i + 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        MyArray.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True

    if not MyArray.isSorted:
        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray

RUN = 32

def Tim_InsertionSort(MyArray, Left, Right, Win, Font, DrawSort):
    for i in range(Left + 1, Right + 1):
        Temp = MyArray.Array[i]
        j = i - 1
        while MyArray.Array[j] > Temp and j >= Left:
            MyArray.Array[j + 1] = MyArray.Array[j]
            MyArray.Moving_Elements = [MyArray.Array[j], MyArray.Array[j + 1]]
            j -= 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                if DrawSort:
                    MyArray.Draw(Win, Font)
        MyArray.Array[j + 1] = Temp
        MyArray.Moving_Elements = [MyArray.Array[j + 1]]
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                MyArray.Draw(Win, Font)

def Merge(MyArray, l, m, r, Win, Font, DrawSort):
    LEN_1, LEN_2 = m - l + 1, r - m
    Left, Right = [], []
    for i in range(0, LEN_1):
        Left.append(MyArray.Array[l + i])

    for i in range(0, LEN_2):
        Right.append(MyArray.Array[m + 1 + i])

    i, j, k = 0, 0, l
    while i < LEN_1 and j < LEN_2:
        if Left[i] <= Right[j]:
            MyArray.Array[k] = Left[i]
            MyArray.Moving_Elements = [MyArray.Array[k]]
            i += 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font)
        else:
            MyArray.Array[k] = Right[j]
            MyArray.Moving_Elements = [MyArray.Array[k]]
            j += 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                if DrawSort:
                    MyArray.Draw(Win, Font)
        k += 1
    while i < LEN_1:
        MyArray.Array[k] = Left[i]
        MyArray.Moving_Elements = [MyArray.Array[k]]
        k += 1
        i += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                MyArray.Draw(Win, Font)
    while j < LEN_2:
        MyArray.Array[k] = Right[j]
        MyArray.Moving_Elements = [MyArray.Array[k]]
        k += 1
        j += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                MyArray.Draw(Win, Font)


def TimSort(MyArray, Win, Font, DrawSort=True):
    if not MyArray.isSorted:
        N = len(MyArray.Array)
        for i in range(0, N, RUN):
            Tim_InsertionSort(MyArray, i, min((i + 31), (N - 1)), Win, Font, DrawSort)
        Size = RUN
        while Size < N:
            for Left in range(0, N, 2 * Size):
                Mid = Left + Size - 1
                Right = min((Left + 2 * Size - 1), (N - 1))
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    if DrawSort:
                        MyArray.Draw(Win, Font)
                Merge(MyArray, Left, Mid, Right, Win, Font, DrawSort)
            Size = 2 * Size

    if not MyArray.isSorted:
        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray


def CycleSort(MyArray, Win, Font):
    if not MyArray.isSorted:
        Writes = 0
        for cycleStart in range(0, len(MyArray) - 1):
            Item = MyArray.Array[cycleStart]
            Position = cycleStart
            for i in range(cycleStart + 1, len(MyArray)):
                if MyArray.Array[i] < Item:
                    Position += 1
            if Position == cycleStart:
                continue

            while Item == MyArray.Array[Position]:
                Position += 1
            MyArray.Array[Position], Item = Item, MyArray.Array[Position]
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font, extraAcceses=2)
            Writes += 1

            while Position != cycleStart:
                Position = cycleStart
                for i in range(cycleStart + 1, len(MyArray)):
                    if MyArray.Array[i] < Item:
                        Position += 1
                while Item == MyArray.Array[Position]:
                    Position += 1
                MyArray.Array[Position], Item = Item, MyArray.Array[Position]
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font, extraAcceses=2)
                Writes += 1

    if not MyArray.isSorted:
        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray

def rotLeft(Array, n=1):
    return Array[n % len(Array):] + Array[:n % len(Array)]

def Rotate(MyArray, rotationTimes, Win, Font):
    if not MyArray.isSorted:
        for _ in range(rotationTimes):
            MyArray.Array = rotLeft(MyArray.Array)
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font)

        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray

def ElementsIncreaser(MyArray, increaseSize, Win, Font):
    if not MyArray.isSorted:
        for _ in range(increaseSize):
            for arrayPosition in range(len(MyArray)):
                MyArray.Array[arrayPosition] += 1
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font)

        MyArray.Draw_Check_Sorted(Win, Font)

    MyArray.isSorted = True
    return MyArray