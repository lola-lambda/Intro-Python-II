class Room():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []
    def print_room(self):
        print(f"{self.name} {self.desc}")
    def print_items(self):
        print(f"available items: {self.items}")
