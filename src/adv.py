from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

moves = { 
    'outside': [{'dir': 'n', 'dest': 'foyer'},],
    'foyer': [{'dir': 's', 'dest': 'outside'}, {'dir': 'n', 'dest': 'overlook'}, {'dir': 'e', 'dest': 'narrow'}],
    'overlook': [{'dir': 's', 'dest': 'foyer'},],
    'narrow': [{'dir': 'w', 'dest': 'foyer'}, {'dir': 'n', 'dest': 'treasure'}],
    'treasure': [{'dir': 's', 'dest': 'narrow'},]
}

name = input("Hello there, what is your name? ")
room_type = 'outside'
player = Player(name, room[room_type])

print(f"Welcome, {player.name}!") 
next = ''

while not next is 'q':
    print(f"You are at the {player.room.name}. {player.room.desc}")
    move_options = [" ['q'] Quit'"]
    for move in moves[room_type]:
        move_options.append(f"{[move['dir']]} {room[move['dest']].name} ")
    next = input(f"Where would you like to go?" + ' '.join(move_options) + ' ')
    prevRoom = room_type
    for move in moves[room_type]:
        if move['dir'] is next:
            move_options = [' [q] quit']
            player.move_rooms(room[move['dest']])
            room_type = move['dest']
    if prevRoom == room_type:
        print('Invalid option, try again...')
