from room import Room
from player import Player
from item import Item

# Declare all the items

item = {
    'potion': Item("potion", "unknown effects"),
    'torch': Item("torch", "portable light source"),
    'sword': Item("sword", "finely crafted blade of iron"),
    'pear': Item("pear", "perfectly ripe fruit"),
    'robe': Item("robe", "linen full-length garment"),
    'ale': Item("ale", "strong and bitter brew"),
    'gem': Item("gem", "radiant and valuable stone"),
    'scroll': Item("scroll", "worn parchment with script"),
    'berries': Item("berries", "cluster of edible berries"),
    'bottle': Item("bottle", "glass bottle with unknown contents")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", 
                    "North of you, the cave mount beckons.",
                    [item['potion'], item['torch'], item['sword']]),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    [item['pear'], item['robe'], item['ale']]),

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. 
                    Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    [item['sword'], item['potion'], item['gem']]),

    'narrow':   Room("Narrow Passage", 
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    [item['scroll'], item['potion'], item['berries']]),

    'treasure': Room("Treasure Chamber", 
                    """You've found the long-lost treasure chamber! 
                    Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
                    [item['bottle'], item['robe'], item['gem']])
}


# Associate current room with direction & destination

moves = { 
    'outside': [{'dir': 'n', 'dest': 'foyer'},],
    'foyer': [{'dir': 's', 'dest': 'outside'}, {'dir': 'n', 'dest': 'overlook'}, {'dir': 'e', 'dest': 'narrow'}],
    'overlook': [{'dir': 's', 'dest': 'foyer'},],
    'narrow': [{'dir': 'w', 'dest': 'foyer'}, {'dir': 'n', 'dest': 'treasure'}],
    'treasure': [{'dir': 's', 'dest': 'narrow'},]
}

# Game initialization

name = input("Hello there, dear adventurer, what is your name? ")
room_type = 'outside'
player = Player(name, room[room_type])

print(f"Welcome, {player.name}!") 
choice = ''

# Game loop

while not choice is 'q':
    print(f"You are at the {player.room.name}. {player.room.desc}")
    choice = input(f"['i'] view inventory ['e'] explore room ['a'] adventure onward ")

    if choice is 'i':
        player.check_inventory()
        action = input(f"[drop item-name] to drop an item or enter to go back: ")
        for item in player.items:
            if action == f"drop {item.name}":
                player.drop_item(item)
                room[room_type].receive_item(item)
                print(f"You dropped the {item.name}")

    elif choice is 'e':
        room[room_type].print_items()
        action = input(f"[take item-name] to take an item or enter to go back: ")
        for item in room[room_type].items:
            if action == f"take {item.name}":
                room[room_type].give_item(item)
                player.take_item(item)
                print(f"You took the {item.name}")

    elif choice is 'a':
        move_options = [" ['q'] Quit'"]
        for move in moves[room_type]:
            move_options.append(f"{[move['dir']]} {room[move['dest']].name} ")
        choice = input(f"Where would you like to go?" + ' '.join(move_options) + ' ')
        prevRoom = room_type
        for move in moves[room_type]:
            if move['dir'] is choice:
                move_options = [' [q] quit']
                player.move_rooms(room[move['dest']])
                room_type = move['dest']
        if prevRoom == room_type:
            print('Invalid input, try again...')
    elif choice is 'q':
        break
    else:
        print('Invalid input, try again...')
print(f"See you next time, {player.name}")