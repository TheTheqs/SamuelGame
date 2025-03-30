from views.base_screen import BaseScreen


class GameOverScreen(BaseScreen):
    def __init__(self, final_score):
        super().__init__()
        self.final_score = final_score

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass
