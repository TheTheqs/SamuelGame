from views.base_screen import BaseScreen
import pygame


class MenuScreen(BaseScreen):
    def __init__(self):
        print("Entering menu screen...")
        super().__init__()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key just for test
                from views.game_screen import GameScreen
                self.controller.set_screen(GameScreen())
            elif event.key == pygame.K_s:  # S key just for test
                from views.score_screen import ScoreScreen
                self.controller.set_screen(ScoreScreen([]))  # Empty for now
            elif event.key == pygame.K_ESCAPE:  # Close game with esc
                self.controller.running = False

    def update(self, dt):
        pass

    def render(self, screen):  # Actual function for test
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 40)
        text1 = font.render("Press ENTER to Start", True, (255, 255, 255))
        text2 = font.render("Press S to View Scores", True, (255, 255, 255))
        text3 = font.render("Press Esc to close the game", True, (255, 255, 255))
        screen.blit(text1, (200, 250))
        screen.blit(text2, (200, 300))
        screen.blit(text3, (200, 350))
