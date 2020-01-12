import pygame
import os, sys
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
    MyArray.isSorted = True
    return MyArray

RUN = 32

def Tim_InsertionSort(MyArray, Left, Right, Win, Font):
    for i in range(Left + 1, Right + 1):
        Temp = MyArray.Array[i]
        j = i - 1
        while MyArray.Array[j] > Temp and j >= Left:
            MyArray.Array[j + 1] = MyArray.Array[j]
            j -= 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font)
        MyArray.Array[j + 1] = Temp
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            MyArray.Draw(Win, Font)

def Merge(MyArray, l, m, r, Win, Font):
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
            i += 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font)
        else:
            MyArray.Array[k] = Right[j]
            j += 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                MyArray.Draw(Win, Font)
        k += 1
    while i < LEN_1:
        MyArray.Array[k] = Left[i]
        k += 1
        i += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            MyArray.Draw(Win, Font)
    while j < LEN_2:
        MyArray.Array[k] = Right[j]
        k += 1
        j += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            MyArray.Draw(Win, Font)


def TimSort(MyArray, Win, Font):
    if not MyArray.isSorted:
        N = len(MyArray.Array)
        for i in range(0, N, RUN):
            Tim_InsertionSort(MyArray, i, min((i + 31), (N - 1)), Win, Font)
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
                    MyArray.Draw(Win, Font)
                Merge(MyArray, Left, Mid, Right, Win, Font)
            Size = 2 * Size

    MyArray.isSorted = True
    return MyArray