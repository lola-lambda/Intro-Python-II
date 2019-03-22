class Room():
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = items

    def print_items(self):
        if len(self.items) > 0:
            all_items = ", ".join([str(item) for item in self.items])
        else:
            all_items = "nothing"
        print(f"You look around the {self.name} and see {all_items}.")

    def give_item(self, item):
        self.items = list(filter(lambda i: not i.name is item.name, self.items))
    
    def receive_item(self, item):
        self.items.append(item)