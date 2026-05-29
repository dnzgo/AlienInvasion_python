import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group # behaves like a list
import game_functions
from game_stats import GameStats

def run_game():
    pygame.init()

    game_settings = Settings()
    pygame.display.set_caption(game_settings.screen_caption) # set title of screen
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height)) # creating a frame width, height

    # Create an instance to store game statistics.
    game_stats = GameStats(game_settings)

    ship = Ship(game_settings, screen) # make a ship

    # Make  groups to store bullets and aliens in
    bullets = Group()
    aliens = Group()
    
    game_functions.create_alien_fleet(game_settings, screen, ship, aliens)

    # main game loop
    while True:
        game_functions.check_events(game_settings, screen, ship, bullets) # check events like keypress and mouse events

        if game_stats.game_active:
            ship.update()
            game_functions.update_bullets(game_settings, screen, ship, aliens, bullets)
            game_functions.update_aliens(game_settings, game_stats, screen, ship, aliens, bullets)
            
        game_functions.update_screen(game_settings, screen, ship, aliens, bullets) # Update images on the screen and flip to the new screen.

run_game()