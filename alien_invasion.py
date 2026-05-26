import pygame
from settings import Settings
from ship import Ship
import game_functions

def run_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height)) # creating a frame width, height

    ship = Ship(game_settings, screen) # make a ship
    
    pygame.display.set_caption(game_settings.screen_caption) # set title of screen

    # main game loop
    while True:
        game_functions.check_events(ship) # check events like keypress and mouse events
        ship.update()
        game_functions.update_screen(game_settings, screen, ship) # Update images on the screen and flip to the new screen.

run_game()