# contains the behaviour of Alien_ship
import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class so represent single alien on the fleet."""

    def __init__(self, ai_game):
        """Intialize the alien and set its starting position."""
        super().__init__()
        # import the screen of the alien game
        self.screen = ai_game.screen

        # import setting class
        self.settings = ai_game.settings

        # load teh image and set it's rect attrbute, problem faced,self.aliens.draw(self.screen) uses self.image not self.scaled_image.
        self.image = pygame.image.load("images/Alien_Ship.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # self.scaled_image= pygame.transform.scale(self.image, (10, 10))
        # self.rect =self.scaled_image.get_rect()

        # moving the new ship at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Check if the alien has hit the edge of screen"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (self.rect.left <= 0):
            return True

        else:
            return False

    def update(self):
        """Moves the alien left or right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
