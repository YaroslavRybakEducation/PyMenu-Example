from settings import *
import pygame

class Settings_menu:
    def __init__(self):
        self.options = [
            "Video Settings [Soon]",
            "Audio Settings [Soon]",
            "Back"
        ]
        self.selected = 0
        self.font = pygame.font.SysFont("Calibri", 30, bold = False)
        self.selected_font = pygame.font.SysFont("Calibri", 60, bold = False)

    def draw(self, surface):
        for i in range(len(self.options)):
            if i == self.selected:
                text = self.selected_font.render(self.options[i], True, WHITE)
            else:
                text = self.font.render(self.options[i], True, GREY)
            rect = text.get_rect(topleft = (surface.get_width() / 9, 50 + 70 * i))
            surface.blit(text, rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected += 1
            if event.key == pygame.K_UP:
                self.selected -= 1
        
        self.selected = self.selected % len(self.options)