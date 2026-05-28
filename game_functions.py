import sys
import pygame
from bullet import Bullet

def check_events(game_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, game_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = True
    if event.key == pygame.K_UP:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # stop moving the ship to the right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # stop moving the ship to the left
        ship.moving_left = False


def update_screen(game_settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(game_settings.background_color) # redraw screen each loop iteration

     # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    alien.blitme()

    pygame.display.flip() # make last drawn screen visible


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update() # Update bullet positions

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy(): # use a copy of the list in loop because we should not remove an element of looped list/group
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if game_settings.bullet_size > len(bullets):
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet) 

