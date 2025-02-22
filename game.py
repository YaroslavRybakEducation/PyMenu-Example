##########################################################################################
# Welcome to official another Python game menu.                                          #
# License will be avaiable on file *LICENSE*                                             #
# However if you have any problems and bugs please Create new issue above                #
# NOTE: You can choose any options Like this: Play, settings, Quit and much more!        #
# WARNING: Make sure if you have installed pygame, but without pygame isn't recommended. #
# Thanks :)                                                                              #
##########################################################################################












# Import modules
import pygame, sys
from menu import Menu
from menu_settings import Settings_menu
from settings import *
import time


# Class Application Games
class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygame Menu")

        self.in_menu = True
        self.in_settings = False
        self.clock = pygame.time.Clock()
        self.menu = Menu()
        self.settings = Settings_menu()

    def update(self):
        self.clock.tick(60)

    def check_events_and_drawing(self):
        if self.in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Closing Down")
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()
                self.menu.handle_events(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.menu.options[self.menu.selected] == "Settings":
                            self.in_settings = True
                            self.in_menu = False
            
            self.screen.fill(BLACK)
            self.menu.draw(self.screen)
            pygame.display.update()
        
        if self.in_settings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Closing Down")
                    pygame.quit()
                    sys.exit()
                self.settings.handle_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.settings.options[self.settings.selected] == "Back":
                            self.in_menu = True
                            self.in_settings = False
            
            self.screen.fill(BLACK)
            self.settings.draw(self.screen)
            pygame.display.update()

    def run(self):
        while True:
            self.check_events_and_drawing()
            self.update()