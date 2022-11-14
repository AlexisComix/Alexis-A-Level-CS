# This code can only be described as spaghetti code.
# I have taken Python and made it into Java.
# Why?

from dataclasses import dataclass
import sys
import os
from random import randint
import pygame

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
)

class Board:
    """
    The class for the board and the properties of the board.
    Handles events relating to the board
    """
    def __init__(self):
        pass

    def draw(self, screen: pygame.Surface):
        width = screen.get_width()
        height = screen.get_height()

        screen.fill(LIGHT_BROWN)

        startx = width // 6
        boardwidth = width - (2 * startx)
        boardrect = pygame.rect.Rect(startx, 0, boardwidth, height)
        pygame.draw.rect(screen, BROWN, boardrect)


@dataclass
class Counter:
    """
    Dataclass for the counter object
    """



class Asset:
    """
    Class for loading assets
    """
    def __init__(self, asset_filename: str, filetype):
        """
        Checks if path exists to asset, if exists load asset
        based on filetype, else return None.
        Valid filetypes are "img", "audio"
        """
        self.filetype = filetype
        cwd = os.getcwd()
        self.asset_path = os.path.join(cwd, asset_filename)
        if os.path.exists(self.asset_path):
            pass
        else:
            print(
                f"WARN: {self.asset_path} load unsuccessful.", 
                "Are you in the right working directory?"
            )
            return None
    
    def load_asset(self):
        """
        Load the file into the respective pygame object
        and return it
        """
        if self.filetype == "img":
            return pygame.image.load(self.asset_path)
        elif self.filetype == "audio":
            return pygame.mixer.Sound(self.asset_path)
        else:
            return None


class Window:
    """
    The class for the Window and handling window events like drawing
    to the screen and initialising the screen.
    """
    def __init__(self):
        """
        Initialise window variables and pygame window instance
        Set Icon and warn on fail.
        """
        self.width = 600
        self.height = 600
        self.dimensions = (self.width, self.height)
        
        self.win = pygame.display.set_mode(self.dimensions, vsync=1)
        pygame.display.set_caption("Alexis' Mastermind", "Alexis' Mastermind")

        pygame.mixer.init()
        self.load_assets()
        self.set_assets()

    def load_assets(self):
        self.icon = Asset("icon.png", "img")

    def set_assets(self):
        icon = self.icon.load_asset()
        if icon is not None:
            pygame.display.set_icon(icon)  # type: ignore

    def get_win(self):
        return self.win


class Game:
    """
    Game class for handling game logic
    """
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.window = Window()
        self.WIN = self.window.get_win()
        self.board = Board()
        self.main()

    def draw(self):
        self.board.draw(self.WIN)

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

        self.draw()
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    Game()