class RPGInfo:
    author = None

    def __init__(self,game_name):
        self.title = game_name

    def welcome(self):
        print(f"Welcome to {self.title}")

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
