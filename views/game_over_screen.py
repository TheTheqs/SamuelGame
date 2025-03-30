from views.base_screen import BaseScreen
import pygame


class GameOverScreen(BaseScreen):
    def __init__(self, final_score):
        print("Entering game over screen...")
        super().__init__()
        self.final_score = final_score

    def handle_event(self, event):  # Pressing enter get the player back to menu/ Will be not dealing with db saving
        # score in test phase
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            from views.menu_screen import MenuScreen
            self.controller.set_screen(MenuScreen())

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((100, 0, 0))
        font = pygame.font.SysFont(None, 40)
        text = font.render(f"Game Over! Score: {self.final_score}", True, (255, 255, 255))
        text2 = font.render("Press ENTER to return to menu", True, (255, 255, 255))
        screen.blit(text, (200, 250))
        screen.blit(text2, (200, 300))
