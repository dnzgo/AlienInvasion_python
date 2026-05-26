import pygame

class Ship():

    def __init__(self, game_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        self.game_settings = game_settings

        # loading ship image and getting its rect
        self.image = pygame.image.load('assets/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # starting ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centerx = self.center
    

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
