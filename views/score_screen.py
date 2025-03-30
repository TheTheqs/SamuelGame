from views.base_screen import BaseScreen


class ScoreScreen(BaseScreen):
    def __init__(self, top_scores):
        super().__init__()
        self.top_scores = top_scores

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass
