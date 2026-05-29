
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)
        self.screen_caption = 'Alien Invasion'
        self.ship_speed_factor = 1

        # bullet settings
        self.bullet_speed_factor = 0.8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_size = 3

        # alien settings
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 -> right, -1 -> left

    