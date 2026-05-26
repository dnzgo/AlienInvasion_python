import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # Move the ship to the right
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # stop moving the ship to the right
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    # stop moving the ship to the left
                    ship.moving_left = False


def update_screen(settings, screen, ship):
     """Update images on the screen and flip to the new screen."""
     screen.fill(settings.background_color) # redraw screen each loop iteration
     ship.blitme()

     pygame.display.flip() # make last drawn screen visible