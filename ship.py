#contains most of behaviour of player ship
import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        self.screen =ai_game.screen
        self.screen_rect =ai_game.screen.get_rect()
        #setting instance to be able to set ship speed..
        self.settings = ai_game.settings
        #loads the ship image and gets its rect.
        self.image=pygame.image.load('images/ship.bmp')
        self.scaled_image = pygame.transform.scale_by(self.image, 0.15)
        self.rect =self.scaled_image.get_rect()
        #starts each new ship at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        #stores ship's x value for horizontal position as rect only store integers
        self.x=float(self.rect.x)
        #A flag for moving Right/Left
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """Updates ship position based on movement flag"""
        #updates ship's horizontal not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x +=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -=self.settings.ship_speed
        #update the ship's rect positon from self.x,but only the integer value will be used to position the ship
        self.rect.x = self.x
    def bltime(self):
        """draw the ship at its current location"""
        self.screen.blit(self.scaled_image, self.rect)


        