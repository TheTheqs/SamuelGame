# Game rules and management
class GameState:
    # Constructor
    def __init__(self):
        self.sequence = []  # Generated sequence
        self.player_input = []  # Sequence Input
        self.round = 1  # Start score
        self.score = 0  # Current score

    # Restart function
    def reset(self):
        self.sequence = []
        self.player_input = []
        self.round = 1
        self.score = 0

    # Sequence manipulation
    def add_to_sequence(self, color):
        self.sequence.append(color)

    # Real time player answer check
    def is_player_correct_so_far(self):
        return self.player_input == self.sequence[:len(self.player_input)]

    # Round check
    def is_round_complete(self):
        return self.player_input == self.sequence
