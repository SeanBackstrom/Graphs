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
'''




def bfs(current_room = player.current_room, trav_ind = 0, pathway = []):
    """
    Return a list containing the shortest path from
    current_room to destination in
    breath-first order.
    """
    print("hi")
    print(len(visit_dict))
    print(len(traversal_path))
    #print("rev", traversal_path[::-1])
    print("visit dict", visit_dict[current_room.id])
    
    if '?' in list(visit_dict[current_room.id].values()):
        print("returning pathway", pathway)
        return pathway

    inversetrav = traversal_path[::-1]
    last_move = inversetrav[trav_ind]
    print(last_move, "lastmove")

    if last_move == 'n':
        last_move = 's'
    elif last_move == 's':
        last_move = 'n'
    elif last_move == 'e':
        last_move = 'w'
    elif last_move == 'w':
        last_move = 'e'
    print(last_move, "changed")
    pathway.append(last_move)
    prev_room2 = current_room.get_room_in_direction(last_move)

    f = get_qmarks(current_room)
    for i in f:
        print(i)
        room = current_room.get_room_in_direction(i)
        r = get_qmarks(room)
        print(room.items())
        if '?' in room.items():
            pass


    #return bfs(current_room = )
    #print("path", pathway)

    return bfs(current_room = prev_room2, trav_ind = trav_ind+1, pathway= pathway)




def traverse():
    while len(visit_dict) < 500:
        print("init", visit_dict)


        # get directions to go
        possible_directions = {}
        for i in player.current_room.get_exits():
            i = f'{i}'
            possible_directions[i] = "meow"

        #list with just directions possible
        possible_dir_list = list(possible_directions.keys())

        # check each direction, if not in visited give value of '?'
        for direction in possible_dir_list:
            dir_room = player.current_room.get_room_in_direction(direction)

            #make the values either the room id or a '?'
            if dir_room.id in list(visit_dict.keys()):
                possible_directions[direction] = dir_room.id
            else:
                possible_directions[direction] = '?'

        
        visit_dict[player.current_room.id] = possible_directions

        #print("TRAVERSAL_PATH", traversal_path)

        priority = [key for (key,value) in possible_directions.items() if value == '?'] 
        #find closest question mark with bfs
        # move
        print("prioirty", priority)
        if priority:
            rand_dir = random.choice(priority)

        
        #change this after succesful bfs
        if not priority:
            path_to_v = bfs(current_room = player.current_room, trav_ind = 0, pathway = [])
            for i in path_to_v:
                print(i)
                player.travel(f'{i}')
                traversal_path.append(i)

            print("visit dict again", visit_dict[player.current_room.id])
            priority = [key for (key,value) in visit_dict[player.current_room.id].items() if value == '?'] 
            rand_dir = random.choice(priority)


        print("direction chosen: ", rand_dir)
        player.travel(rand_dir)
        traversal_path.append(rand_dir)

        if rand_dir == 'n':
            prev_room = player.current_room.get_room_in_direction('s').id
            print(prev_room, "prev room")
            visit_dict[prev_room]['n'] = player.current_room.id
            #visit_dict[current_room]['s'] = 
        if rand_dir == 's':
            prev_room = player.current_room.get_room_in_direction('n').id
            print(prev_room, "prev room")
            visit_dict[prev_room]['s'] = player.current_room.id
        if rand_dir == 'e':
            prev_room = player.current_room.get_room_in_direction('w').id
            print(prev_room, "prev room")
            visit_dict[prev_room]['e'] = player.current_room.id
        if rand_dir == 'w':
            prev_room = player.current_room.get_room_in_direction('e').id
            print(prev_room, "prev room")
            visit_dict[prev_room]['w'] = player.current_room.id
        
        print("current room: ", player.current_room.id)

        print("length: ", len(traversal_path))
        print('current', visit_dict, len(visit_dict))
        print('\n')


traverse()


'''


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
