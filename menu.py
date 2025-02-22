import pygame
from settings import *


# Class game menu
class Menu:
    def __init__(self):
        self.options = [
            "Play",
            "",
            "Settings",
            "",
            "Quit",
        ]
        self.selected = 0
        self.selected_add = 0
        self.font = pygame.font.SysFont("Calibri", 30, bold = False)
        self.selected_font = pygame.font.SysFont("Calibri", 60, bold = False)

    # Drawing method
    def draw(self, surface):
        for i in range(len(self.options)):
            if i == self.selected:
                text = self.selected_font.render(self.options[i], True, WHITE)
            else:
                text = self.font.render(self.options[i], True, GREY)
            rect = text.get_rect(topleft = (surface.get_width() / 9, 50 + 70 * i))
            surface.blit(text, rect)

    # Event handling
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_add += 1
            elif event.key == pygame.K_UP:
                self.selected_add -= 1
    # Starts over when out of options    
        self.selected = (self.selected + self.selected_add) % len(self.options)

        while self.options[self.selected] == "":
            self.selected = (self.selected + self.selected_add) % len(self.options)

        self.selected_add = 0