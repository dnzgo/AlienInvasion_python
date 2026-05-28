import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        #Loading alien image and set rect
        self.image = pygame.image.load('assets/alien.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # store aliens exact position
        self.x = float(self.rect.x)

    
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

