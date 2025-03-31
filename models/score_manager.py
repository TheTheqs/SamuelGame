# Score management and DB manipulation
import sqlite3
from datetime import datetime


class ScoreManager:
    # Constructor
    def __init__(self, db_path="data/game.db"):
        self.db_path = db_path
        self._init_db()

    # DB start
    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS scores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   score INTEGER,
                   date TEXT
               )
           """)
        conn.commit()
        conn.close()

    # Save new Score
    def save_score(self, name, score):
        if not name or name == "":
            name = "Player"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (name, score, date) VALUES (?, ?, ?)",
                       (name, score, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    # Get top 20 scores
    def get_top_scores(self, limit=20):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        results = cursor.fetchall()
        conn.close()
        return results
