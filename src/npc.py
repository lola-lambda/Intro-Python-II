from player import Player

class NPC(Player):
    def __init__(self, name, room, stories):
        super().__init__(name, room)
        self.stories = []
    def speak(self, index):
        print(f"{self.stories[index]}")
