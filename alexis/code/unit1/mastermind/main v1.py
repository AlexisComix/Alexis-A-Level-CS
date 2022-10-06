# A pygame version of the board game Mastermind

import sys
from random import randint
import pygame

class Mastermind:
    """
    Main Mastermind game class
    """
    
    # Constants
    COLOURS = (
        BLACK := (0, 0, 0),
        WHITE := (255, 255, 255),
        GREY := (150, 150, 150),
        RED := (255, 0, 0),
        GREEN := (0, 255, 0),
        BLUE := (0, 0, 255),
        YELLOW := (255, 255, 0),
        PURPLE := (175, 0, 255),
        PINK := (255, 120, 165),
        BROWN := (103, 65, 15),
        LIGHT_BROWN := (104, 86, 61)
    )   # epic walrus operator fan club

    def __init__(self):
        """
        Game inits
        """
        # Class vars
        self.running = True

        # Function calls
        self.win_setup()
        self.main()

    def win_setup(self):
        """
        Initialise and setup pygame window
        """
        self.WIN_WIDTH = 500
        self.WIN_HEIGHT = 500
        self.DIMENSIONS = (self.WIN_WIDTH, self.WIN_HEIGHT)
        self.WIN = pygame.display.set_mode(self.DIMENSIONS, vsync=1)
        pygame.display.set_caption("Alexis' Mastermind")

        self.icon = pygame.image.load("icon.png")
        pygame.display.set_icon(self.icon)

    def main(self):
        """
        Main game loop
        """
        while self.running:
            self.handle_events()
            self.update_display()

    def handle_events(self):
        """
        Handle the game events in the main loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_display(self):
        self.WIN.fill(self.BROWN)
        self.draw_grid()
        pygame.display.flip()

    def draw_grid(self):
        light_rect = pygame.Rect(150, 0, 200, 500)
        pygame.draw.rect(self.WIN, self.LIGHT_BROWN, light_rect)


if __name__ == "__main__":
    Mastermind()