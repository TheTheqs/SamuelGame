from views.base_screen import BaseScreen
import pygame


class ScoreScreen(BaseScreen):
    def __init__(self, top_scores):
        print("Entering Score Screen...")
        super().__init__()
        self.top_scores = top_scores

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Close game with esc
                from views.menu_screen import MenuScreen
                self.controller.set_screen(MenuScreen())

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 40)
        text1 = font.render("No saved score yet", True, (255, 255, 255))
        text3 = font.render("Press Esc to return to Main Menu", True, (255, 255, 255))
        screen.blit(text1, (200, 250))
        screen.blit(text3, (200, 350))
