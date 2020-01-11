import random
import pygame
import pyaudio
from Exceptions import ArraySizeError
from Sound_Generator import ToneGenerator

Sound_Amplitude = 0.50
Sound_Duration = 0.10
Sound_Frequency_Range = [i for i in range(100, 1000)]
Generator = ToneGenerator()

RED_PINK = [[255, 0, i] for i in range(256)]
PINK_BLUE = [[i, 0, 255] for i in reversed(range(256))]
BLUE_AQUA = [[0, i, 255] for i in range(256)]
AQUA_GREEN = [[0, 255, i] for i in reversed(range(256))]
GREEN_YELLOW = [[i, 255, 0] for i in range(256)]
YELLOW_RED = [[255, i, 0] for i in reversed(range(256))]
RGB = RED_PINK + PINK_BLUE + BLUE_AQUA + AQUA_GREEN + GREEN_YELLOW + YELLOW_RED
RGB_SIZE = len(RGB)

class Visualized_Array:
    def __init__(self, Size, X, Y, Width, Height, CompleteArray=True):
        if Size > 1500: # Sizes bigger than 1000 take too much time sorting and displaying the array.
            raise ArraySizeError(f"Array size is too big, size can't be bigger than 1500. Selected size is {Size}.")
        else:
            self.x = X
            self.y = Y
            self.Width = Width
            self.Height = Height
            self.Size = Size
            self.Current_Accesses = 0 # Using that to know how many accesses to the array we have made.
            self.isComplete = CompleteArray
            self.Jumps = RGB_SIZE//Size
            self.Audio_Jumps = len(Sound_Frequency_Range)//Size
            self.Moving_Elements = []
            self.isSorted = False
            if CompleteArray: # If the array has to be complete.
                self.Array = [i for i in range(1, Size+1)] # Generating array with numbers from one to Size.
                random.shuffle(self.Array) # Moving the numbers to random positions.
            else:
                self.Array = []
                for _ in range(Size):
                    self.Array.append(random.randint(1, Size))
            self.Normalized_Array = [i/max(self.Array) for i in self.Array] # Creating an array with values between [0, 1].

    def Draw(self, Win, Font, isSorted=False, extraAcceses=1, Sound=False):
        Win.fill((0, 0, 0))
        if not isSorted:
            self.Current_Accesses += extraAcceses
        self.Normalized_Array = [i / max(self.Array) for i in self.Array]  # Creating an array with values between [0, 1].
        for i in range(self.Size):
            Current_Element = self.Normalized_Array[i]
            Rectangle = pygame.Rect(self.x + i*self.Width, self.y, self.Width, -self.Height*Current_Element)
            Element_Colour = RGB[self.Array[i]*self.Jumps%RGB_SIZE]
            pygame.draw.rect(Win, Element_Colour, Rectangle)
            if self.Array[i] in self.Moving_Elements and Sound:
                try:
                    Generator.play(Sound_Frequency_Range[self.Array[i]*self.Jumps%len(Sound_Frequency_Range)], Sound_Duration, Sound_Amplitude)
                except OSError:
                    None
        Accesses_Text = Font.render(f"Array Accesses: {self.Current_Accesses}", True, (255, 255, 255))
        Win.blit(Accesses_Text, (10, 10))
        pygame.display.update()

    def __len__(self):
        return self.Size

    def __str__(self):
        return str(self.Array)
