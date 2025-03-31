from views.base_screen import BaseScreen
from models.score_manager import ScoreManager
import pygame


class ScoreScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.scores = ScoreManager()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Close back to main menu
                from views.menu_screen import MenuScreen
                self.controller.set_screen(MenuScreen())

    def update(self, dt):
        pass

    def render_content(self, screen):
        vertical_offset = -50
        try:
            scores = self.scores.get_top_scores(10)
        except Exception as e:
            print("Databank error!", e)
            scores = []

        # Message when there is no data in the databank or there was a connection failure
        if not scores:
            msg = self.font.render("No saved scores yet.", True, (30, 30, 30))
            msg_rect = msg.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
            screen.blit(msg, msg_rect)
        else:
            title = self.title_font.render("Top Scores", True, (30, 30, 30))
            title_rect = title.get_rect(center=(self.SCREEN_WIDTH // 2, 80 + vertical_offset))
            screen.blit(title, title_rect)

            headers = ["RANK", "NAME", "SCORE"]
            header_positions = [200, 400, 600]
            for i, h in enumerate(headers):
                header_text = self.font.render(h, True, (30, 30, 30))
                header_rect = header_text.get_rect(center=(header_positions[i], 140 + vertical_offset))
                screen.blit(header_text, header_rect)

            # Building list
            for i, (name, score) in enumerate(scores):
                y = 180 + i * 40 + vertical_offset

                rank_text = self.font.render(str(i + 1), True, (30, 30, 30))
                name_text = self.font.render(name, True, (30, 30, 30))
                score_text = self.font.render(str(score), True, (30, 30, 30))

                screen.blit(rank_text, rank_text.get_rect(center=(header_positions[0], y)))
                screen.blit(name_text, name_text.get_rect(center=(header_positions[1], y)))
                screen.blit(score_text, score_text.get_rect(center=(header_positions[2], y)))

        # Back instruction
        back_text = self.footer_font.render("Press Esc to return to Main Menu", True, (30, 30, 30))
        back_rect = back_text.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT - 50))
        screen.blit(back_text, back_rect)
