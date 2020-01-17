import random
import pygame
from Exceptions import ArraySizeError
from GUI_Functions import KEY_PRESSED
from time import sleep as WaitTime
import winsound as BeepSound
from Sound_Generator import ToneGenerator

Generator = ToneGenerator()
Sound_Duration = 0.2 # Time (seconds) to play at each step.
Sound_Frequency_Range = [i for i in range(255, 1000)]
Amplitude = 3  # Amplitude of the waveform.

RED_PINK = [[255, 0, i] for i in range(256)]
PINK_BLUE = [[i, 0, 255] for i in reversed(range(256))]
BLUE_AQUA = [[0, i, 255] for i in range(256)]
AQUA_GREEN = [[0, 255, i] for i in reversed(range(256))]
GREEN_YELLOW = [[i, 255, 0] for i in range(256)]
YELLOW_RED = [[255, i, 0] for i in reversed(range(256))]
RGB = RED_PINK + PINK_BLUE + BLUE_AQUA + AQUA_GREEN + GREEN_YELLOW + YELLOW_RED
RGB_SIZE = len(RGB)

class Visualized_Array:
    def __init__(self, Size, X, Y, Width, Height, Information_Text, CompleteArray=True, Sound=False):
        """

        :param Size: Number of elements on the array.
        :param X: Initial x position for the first element on the array.
        :param Y: Initial y position for the first element on the array.
        :param Width: Width of the biggest element on the array.
        :param Height: Height of the biggest element on the array.
        :param Information_Text: Array storing the current Sorting Algorithm and the array size.
        :param CompleteArray: Boolean value. If True, we are going to create the array with the numbers from 1 to Size randomly shuffled, if is False, we add 'Size' random numbers from 1 to Size, so numbers can be repeated.
        :param Sound: Boolean to know if we want to generate sounds.
        """
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
            self.Jumps = round(RGB_SIZE/Size) # Depending on the size of the array we acces to the RGB colours with more or less steps.
            self.Audio_Jumps = len(Sound_Frequency_Range)//Size # Same as RGB.
            self.Information_Text = Information_Text
            self.Moving_Elements = [] # Knowing the values of the current elements that we are moving.
            self.isSorted = False # Using it to know if we have to execute the sorting algorithm.
            self.Sound = Sound
            if CompleteArray: # If the array has to be complete.
                self.Array = [i for i in range(1, Size+1)] # Generating array with numbers from one to Size.
                random.shuffle(self.Array) # Moving the numbers to random positions.
            else: # If not, we just add Size times a random value between 1 and Size.
                self.Array = []
                for _ in range(Size):
                    self.Array.append(random.randint(1, Size))

            try:
                self.Normalized_Array = [i/max(self.Array) for i in self.Array] # Creating an array with values between [0, 1].
            except ZeroDivisionError:
                self.Normalized_Array = []
                for i in self.Array:
                    if i == 0:
                        self.Normalized_Array.append(i)
                    else:
                        self.Normalized_Array.append(i/max(self.Array))

    def Draw(self, Win, Font, extraAcceses=1, cleanScreen=True):
        """
        :param Win: PyGame surface, to draw the array.
        :param Font: Font to write the information.
        :param extraAcceses: Using it to count the array accesses, sometimes we move more than one element so we have to add more than one to the counter.
        """
        if cleanScreen:
            Win.fill((0, 0, 0)) # Cleaning everything on the screen.
        if not self.isSorted: # If not sorted, we add the accesses.
            self.Current_Accesses += extraAcceses

        try:
            self.Normalized_Array = [i / max(self.Array) for i in self.Array]  # Creating an array with values between [0, 1].
        except ZeroDivisionError:
            self.Normalized_Array = []
            for i in self.Array:
                if i == 0:
                    self.Normalized_Array.append(i)
                else:
                    self.Normalized_Array.append(i / max(self.Array))

        for i in range(self.Size):
            if self.Array[i] in self.Moving_Elements and self.Sound and self.isSorted is False: # If we are drawing the moving element, and Sound is enabled, and the array isn't sorted, we make the corresponding sound.
                # BeepSound.Beep(Sound_Frequency_Range[self.Array[i]*self.Jumps%len(Sound_Frequency_Range)], Sound_Duration)
                Generator.play(Sound_Frequency_Range[self.Array[i]*self.Audio_Jumps%len(Sound_Frequency_Range)], Sound_Duration, Amplitude)
                while Generator.is_playing():
                    None
            Current_Element = self.Normalized_Array[i] # Getting the value of the element.
            Rectangle = pygame.Rect(self.x + i*self.Width, self.y, self.Width, -self.Height*Current_Element) # Drawing the rectangle, x position increases at every iteration and Height depends on the value of the element.
            # Height is negative to draw in up direction.
            Element_Colour = RGB[self.Array[i]*self.Jumps%RGB_SIZE] # Getting the colour value depending on our value, here we don't use the normalized value, since we want to acces to a position of an array and we can't do Array[0.7].
            pygame.draw.rect(Win, Element_Colour, Rectangle) # Drawing on the surface, with the colour, and the generated rectangle.

        Accesses_Text = Font.render(f"Array Accesses: {self.Current_Accesses}", True, (255, 255, 255)) # Drawing the text with the accesses to the array.
        Win.blit(Accesses_Text, (10, 10))
        Rendered_1 = Font.render(self.Information_Text[0], True, (255, 255, 255)) # Array size.
        Rendered_2 = Font.render(self.Information_Text[1], True, (255, 255, 255)) # Current algorithm.
        Win.blit(Rendered_1, (400, 10))
        Win.blit(Rendered_2, (720, 10))
        pygame.display.update() # Updating screen.

    def Draw_Check_Sorted(self, Win, Font):
        Accesses_Text = Font.render(f"Array Accesses: {self.Current_Accesses}", True, (255, 255, 255))  # Drawing the text with the accesses to the array.
        Win.blit(Accesses_Text, (10, 10))
        Rendered_1 = Font.render(self.Information_Text[0], True, (255, 255, 255))  # Array size.
        Rendered_2 = Font.render(self.Information_Text[1], True, (255, 255, 255))  # Current algorithm.
        Win.blit(Rendered_1, (400, 10))
        Win.blit(Rendered_2, (720, 10))
        self.Normalized_Array = [i / max(self.Array) for i in self.Array]  # Creating an array with values between [0, 1].
        for i in range(self.Size):
            Current_Element = self.Normalized_Array[i] # Getting the value of the element.
            Rectangle = pygame.Rect(self.x + i*self.Width, self.y, self.Width, -self.Height*Current_Element) # Drawing the rectangle, x position increases at every iteration and Height depends on the value of the element.
            # Height is negative to draw in up direction.
            Element_Colour = (70, 230, 70) # Getting the colour value depending on our value, here we don't use the normalized value, since we want to acces to a position of an array and we can't do Array[0.7].
            pygame.draw.rect(Win, Element_Colour, Rectangle) # Drawing on the surface, with the colour, and the generated rectangle.
            if self.Sound: # If Sound is enabled, we make the corresponding sound.
                # BeepSound.Beep(Sound_Frequency_Range[self.Array[i]*self.Jumps%len(Sound_Frequency_Range)], Sound_Duration)
                Generator.play(Sound_Frequency_Range[self.Array[i]*self.Audio_Jumps%len(Sound_Frequency_Range)], Sound_Duration, Amplitude)
                while Generator.is_playing():
                    None
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                break
                pygame.quit()
                sys.exit()
            else:
                pygame.display.update() # Updating screen.

    def __len__(self):
        return self.Size

    def __str__(self):
        return str(self.Array)