class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
    def check_inventory(self):
        print(f"your inventory includes {self.items}")
    def move_rooms(self, room):
        self.room = room