import os
import sys
import ctypes
import pygame
from pygame.locals import *
from Array_GUI import Visualized_Array
from GUI_Functions import KEY_PRESSED
from Sorting_Algorithms import InsertionSort, CocktailShakerSort, BubbleSort, TimSort, CycleSort, Rotate, ElementsIncreaser
from Exceptions import ArraySizeError
from time import sleep as WaitTime
from math import log

ARRAY_SIZE = 1024 # Max value is 10000.
AL = 4 # 1 for Insertion Sort, 2 for Cocktail Shaker Sort, 3 for Bubble Sort, 4 for Tim Sort, 5 for Cycle Sort, 6 for Rotation and 7 for Elements Increaser.
SOUND = False # Sound just works at 100% on Insertion Sort.

user32 = ctypes.windll.user32
SCREENSIZE = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
FLAGS = FULLSCREEN | DOUBLEBUF # Fullscreen mode.
pygame.init() # Starting PyGame library.
WIN_SIZE = (SCREENSIZE[0], SCREENSIZE[1]) # Screen resolution depending on the screen size.
WIN_NAME = "Array Visualizer"
WIN_BG = (0, 0, 0)
WIN_ICON = pygame.image.load("./Icon.png")
WIN = pygame.display.set_mode(WIN_SIZE, FLAGS) # Creating screen in fullscreen mode.
WIN.set_alpha(None) # Disabling alpha, since we don't use images so that improves the perfomance.
pygame.display.set_caption(WIN_NAME)
pygame.display.set_icon(WIN_ICON)
pygame.mouse.set_visible(False) # Hidding the mouse.
pygame.event.set_allowed([QUIT, KEYDOWN]) # Adding the two onlu allowed keys, for better perfomance.
FONT = pygame.font.SysFont('Consolas', 30) # Using the font to count iterations.
MAIN_LOOP = True
ALS = ["Insertion Sort", "Cocktail Shaker Sort", "Bubble Sort", "Tim Sort", "Cycle Sort", "Rotation", "Elements Increaser"]

def isIntegrer(N):
	N = str(N)
	i = N.index(".")
	if N[i+1] == "0" and len(N) == i+2:
		return True
	else:
		return False

if AL == 4: # In case of TimSort, checking if the array size is a power of two.
    if not isIntegrer(log(ARRAY_SIZE, 2)):
        raise ArraySizeError("When using Tim Sort, array size should be power of two. (64, 128, 256, 512)")
        MAIN_LOOP = False

Information_Text = [str(f"Array Size: {ARRAY_SIZE}"), str(f"Current Algorithm: {ALS[AL-1]}")] # Creating the text which contains information like the name of the algorithm and the size of the array.
MyArray = Visualized_Array(ARRAY_SIZE, 5, WIN_SIZE[1], (WIN_SIZE[0] - 20) / ARRAY_SIZE, WIN_SIZE[1] - 30, Information_Text, CompleteArray=True, Sound=SOUND) # Creating the array.

while MAIN_LOOP:
    KEY = KEY_PRESSED()
    if KEY == "QUIT":
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    else:
        if AL == 1:
            InsertionSort(MyArray, WIN, FONT, False).Draw(WIN, FONT, True)
        elif AL == 2:
            CocktailShakerSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 3:
            BubbleSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 4:
            TimSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 5:
            CycleSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 6:
            Rotate(MyArray, len(MyArray), WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 7:
            ElementsIncreaser(MyArray, len(MyArray), WIN, FONT).Draw(WIN, FONT, True)