import sys
import os
import time
import pygame
from pygame.locals import *
from Array_GUI import Visualized_Array
from GUI_Functions import KEY_PRESSED
from Sorting_Algorithms import InsertionSort, CocktailShakerSort, BubbleSort
import ctypes

ARRAY_SIZE = int(input("Array Size: "))
print("\n")
Algorithm = ("Insertion Sort", "Cocktail Shaker Sort", "Bubble Sort")
for i in range (len(Algorithm)):
    print(i+1, Algorithm[i])
AL = int(input("Algorithm: "))

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (625, 200) # Starting the game screen on the center.
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
MyArray = Visualized_Array(ARRAY_SIZE, 5, WIN_SIZE[1], 1900/ARRAY_SIZE, WIN_SIZE[1]-20, CompleteArray=True)

while MAIN_LOOP:
    KEY = KEY_PRESSED()
    if KEY == "QUIT":
        MAIN_LOOP = False
        pygame.quit()
        sys.exit()
    else:
        if AL == 1:
            InsertionSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 2:
            CocktailShakerSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
        elif AL == 3:
            BubbleSort(MyArray, WIN, FONT).Draw(WIN, FONT, True)
