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
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font)
    return MyArray

def CocktailShakerSort(MyArray, Win, Font):
    for i in range(len(MyArray.Array) - 1, 0, -1):
        Swapped = False
        for j in range(i, 0, -1):
            if MyArray.Array[j] < MyArray.Array[j - 1]:
                MyArray.Array[j], MyArray.Array[j - 1] = MyArray.Array[j - 1], MyArray.Array[j]
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
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                Swapped = True
        if not Swapped:
            return MyArray

def BubbleSort(MyArray, Win, Font):
    Swapped = True
    while Swapped:
        Swapped = False
        for i in range(len(MyArray.Array) - 1):
            if MyArray.Array[i] > MyArray.Array[i + 1]:
                MyArray.Array[i], MyArray.Array[i + 1] = MyArray.Array[i + 1], MyArray.Array[i]
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    MyArray.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                Swapped = True
    return MyArray