# Game rules and management
import random

class GameState:
    # Constructor
    def __init__(self):
        self.COLOR_POOL = ["red", "blue", "yellow", "green"]
        self.sequence = []  # Generated sequence
        self.player_input = []  # Sequence Input
        self.round = 0  # Start score
        self.score = 0  # Current score
        self.states = {
            0: "start_round",
            1: "play_demo",
            2: "demo_finished",
            3: "player_turn",
            4: "end_player_turn"
        }
        self.turn_state = 4

        self.turn = "samuel"

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
    def is_player_correct_so_far(self, color):
        self.add_player_color(color)
        return self.player_input == self.sequence[:len(self.player_input)]

    # Round check
    def is_round_complete(self):
        return len(self.player_input) == len(self.sequence)

    def generate_next_round(self):
        self.player_input = []
        self.round += 1
        self.score += 1
        new_color = random.choice(self.COLOR_POOL)
        self.sequence.append(new_color)

    def add_player_color(self, new_color):
        self.player_input.append(new_color)

    def next_state(self):
        if self.get_turn_state() == "end_player_turn":
            self.turn_state = 0
        else:
            self.turn_state += 1

    def get_turn_state(self):
        return self.states[self.turn_state]
