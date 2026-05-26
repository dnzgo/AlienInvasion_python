import sys 
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()

    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height)) # creating a frame width, height

    ship = Ship(screen) # make a ship
    
    pygame.display.set_caption(game_settings.screen_caption) # set title of screen
 
    background_color = game_settings.background_color # setting background color(RGB)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(background_color) # redraw screen each loop iteration
        ship.blitme()
        pygame.display.flip() # make last drawn screen visible

run_game()