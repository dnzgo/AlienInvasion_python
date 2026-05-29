import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(game_settings, game_stats, screen, ship, aliens, bullets, play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, game_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(game_settings, game_stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y)


def check_keydown_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # stop moving the ship to the right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # stop moving the ship to the left
        ship.moving_left = False


def check_play_button(game_settings, game_stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        game_stats.reset_stats()
        game_stats.game_active = True

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_alien_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(game_settings, game_stats, screen, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(game_settings.background_color) # redraw screen each loop iteration

     # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)

    # Draw the play button if the game is inactive
    if not game_stats.game_active:
        play_button.draw_button()

    pygame.display.flip() # make last drawn screen visible


def update_bullets(game_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    bullets.update() # Update bullet positions

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy(): # use a copy of the list in loop because we should not remove an element of looped list/group
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # loops bullets and aliens, rects of a bullet and alien overlap deletes both

    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty() # empty bullet list
        create_alien_fleet(game_settings, screen, ship, aliens)


def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if game_settings.bullet_size > len(bullets):
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet) 


def create_alien_fleet(game_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_row(game_settings, ship.rect.height, alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)
        


def get_number_aliens_x(game_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = game_settings.screen_width - 2 * alien_width # width of screen that can aliens be placed
    number_aliens_x = int(available_space_x / (2 * alien_width)) # number of aliens fits to screen

    return number_aliens_x


def get_number_row(game_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    # Spacing between each alien is equal to one alien width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_aliens(game_settings, game_stats, screen, ship, aliens, bullets):
    """Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet."""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, game_stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(game_settings, game_stats, screen, ship, aliens, bullets)


def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    
    game_settings.fleet_direction *= -1


def ship_hit(game_settings, game_stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if game_stats.ship_left > 0:
        # Decrement ships_left
        game_stats.ship_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_alien_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        # pause 0.5 sec
        sleep(0.5)
    else:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(game_settings, game_stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(game_settings, game_stats, screen, ship, aliens, bullets)
            break