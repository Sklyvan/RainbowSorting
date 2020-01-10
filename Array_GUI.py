import random
import pygame
from Exceptions import ArraySizeError

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
        if Size > 1000: # Sizes bigger than 1000 take too much time sorting and displaying the array.
            raise ArraySizeError(f"Array size is too big, size can't be bigger than 10000. Selected size is {Size}.")
        else:
            self.x = X
            self.y = Y
            self.Width = Width
            self.Height = Height
            self.Size = Size
            self.Current_Accesses = 0 # Using that to know how many accesses to the array we have made.
            self.isComplete = CompleteArray
            self.Jumps = RGB_SIZE//Size
            if CompleteArray: # If the array has to be complete.
                self.Array = [i for i in range(1, Size+1)] # Generating array with numbers from one to Size.
                random.shuffle(self.Array) # Moving the numbers to random positions.
            else:
                self.Array = []
                for _ in range(Size):
                    self.Array.append(random.randint(1, Size))
            self.Normalized_Array = [i/max(self.Array) for i in self.Array] # Creating an array with values between [0, 1].

    def Draw(self, Win, Font, isSorted=False, extraAcceses=1):
        Win.fill((0, 0, 0))
        if not isSorted:
            self.Current_Accesses += extraAcceses
        self.Normalized_Array = [i / max(self.Array) for i in self.Array]  # Creating an array with values between [0, 1].
        for i in range(self.Size):
            Current_Element = self.Normalized_Array[i]
            Rectangle = pygame.Rect(self.x + i*self.Width, self.y, self.Width, -self.Height*Current_Element)
            Element_Colour = RGB[self.Array[i]*self.Jumps]
            pygame.draw.rect(Win, Element_Colour, Rectangle)
        Accesses_Text = Font.render(f"Array Accesses: {self.Current_Accesses}", True, (255, 255, 255))
        Win.blit(Accesses_Text, (10, 10))
        pygame.display.update()

    def __len__(self):
        return self.Size

    def __str__(self):
        return str(self.Array)
