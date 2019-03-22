class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def check_inventory(self):
        if len(self.items) > 0:
            all_items = ", ".join([str(item) for item in self.items])
        else:
            all_items = "nothing"
        print(f"Your inventory contains {all_items}.")

    def drop_item(self, item):
        self.items = list(filter(lambda i: not i.name is item.name, self.items))

    def take_item(self, item):
        self.items.append(item)

    def move_rooms(self, room):
        self.room = room