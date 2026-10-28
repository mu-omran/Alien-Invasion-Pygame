# This file will contain all the settings of the project in one place instead of
# of searching through the entire project


class Settings:
    """A file storing all settings for alien invasion"""

    def __init__(self):
        """intialise the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship setting
        self.ship_speed = 1.5
        # Bullet_Setting
        self.bullet_speed = 0.2  # default 0.9
        self.bullet_width = 3  # default 3
        self.bullet_height = 15  # default 15
        self.bullet_color = (60, 70, 90)
        self.bullets_allowed = 10
        # Alien_Settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # Right -> 1, Left -> -1
        self.alien_delay = 1
