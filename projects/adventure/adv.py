from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import sys 
sys.setrecursionlimit(10**6) 

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
#world.print_rooms()

player = Player(world.starting_room)



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)



def get_qmarks(room):
            # get directions to go
        possible_directions = {}
        for i in room.get_exits():
            i = f'{i}'
            possible_directions[i] = "meow"

        #list with just directions possible
        possible_dir_list = list(possible_directions.keys())

        # check each direction, if not in visited give value of '?'
        for direction in possible_dir_list:
            dir_room = room.get_room_in_direction(direction)

            #make the values either the room id or a '?'
            if dir_room.id in list(visit_dict.keys()):
                possible_directions[direction] = dir_room.id
            else:
                possible_directions[direction] = '?'
        return possible_directions


def has_question_marks(room):
    if '?' in get_qmarks(room).values():
        return True
    else:
        return False

def get_neighbors(room):
    rooms = []
    q=get_qmarks(room)
    for d in q:
        rooms.append(room.get_room_in_direction(d))
    return rooms

def directions(room_path_list):
    directions = []
    cl = player.current_room
    
    """
    if '?' in get_qmarks(cl).values():
        print(get_qmarks(cl))
        onlyq = [k for k, v in get_qmarks(cl).items() if '?' in v]
        directions.append(random.choice(onlyq))
        print(directions)
        return directions"""

    for room in room_path_list:
        #get every room in directions and if it matches room, add that direction to directions
        for direction in get_qmarks(cl):
            possroom = cl.get_room_in_direction(direction)
            sucdir = direction
            if possroom == room:
                directions.append(sucdir)

    return directions

        
def bfs2(starting_room):
    q = Queue()
    visited = set()

    q.enqueue([starting_room])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        #get qmarks
        vq = get_qmarks(v)
        
        if v not in visited:
            if has_question_marks(v) == True:
                entry = get_qmarks(v)
                print(entry)
                #onlyq = [k for (k, val) in entry.items() if '?' in val]
                for k, val in entry.items():
                    #print(k, val)
                    if val == '?':
                        onlyq = k
                qroom = v.get_room_in_direction(random.choice(onlyq))
                path.append(qroom)
                return directions(path[1:])
            visited.add(v)

            for neighbor in get_neighbors(v):

                new_path = path + [neighbor]
                q.enqueue(new_path)
        
    return None

def traverse():
    #print(visit_dict)
    if len(traversal_path) > 2000:
        print("FAILURE, OVER 2K")
        return -1
    if len(visit_dict) == 500:
        print("SUCCESS!")
        return

    path = bfs2(player.current_room)
    for r in path:
        player.travel(r)
        traversal_path.append(r)
        visit_dict[player.current_room.id] = get_qmarks(player.current_room)
        #print(player.current_room.id)
    return traverse()

visit_dict = {}

visit_dict[player.current_room.id] = get_qmarks(player.current_room)

traverse()






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

"""

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
"""
