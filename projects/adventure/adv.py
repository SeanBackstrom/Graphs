from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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


class Graph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        if room_id not in self.rooms:
            self.rooms[room_id] = set()



    def add_connection(self, r1, r2):
        """
        Add a directed connection to the graph.
        """
        
        if r1 in self.rooms:
            self.rooms[r1].add(r2)
        else:
            self.rooms[r1] = [r2]

    def get_neighbors(self, room_id):
        """
        Get all neighbors (connections) of a room.
        """
        return self.rooms[room_id]

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:

            path = q.dequeue()

            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path
                
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)
        return None


trav_graph = Graph()
print(trav_graph.rooms)




def traverse():
    while len(visited_rs) < 500:

        # initialize
        if player.current_room.id not in visited_rs:
            visited_rs.add(player.current_room.id)

        # get directions to go
        possible_directions = {}
        for i in player.current_room.get_exits():
            i = f'{i}'
            possible_directions[i] = "meow"
            print('possible', possible_directions)

        #list with just directions possible
        possible_dir_list = list(possible_directions.keys())

        # check each direction, if not in visited give value of '?'
        for direction in possible_dir_list:
            dir_room = player.current_room.get_room_in_direction(direction)

            #make the values either the room id or a '?'
            if dir_room.id in visited_rs:
                possible_directions[direction] = dir_room.id
            else:
                possible_directions[direction] = '?'

        print("updated", possible_directions)
        print("possible dir list", possible_directions)
        # if deadend
        
        #prioritize towards '?'
        #priority_dir_list = possible_directions.
        priority = [key for (key,value) in possible_directions.items() if value == '?'] 

        #find closest question mark with bfs
        
        # move
        print("prioirty", priority)
        if priority:
            rand_dir = random.choice(priority)

        bfs(player.current_room)
        #change this after succesful bfs
        if not priority:
            rand_dir = random.choice(possible_dir_list)
        print("direction chosen: ", rand_dir)
        player.travel(rand_dir)
        visited_rs.add(player.current_room.id)
        traversal_path.append(rand_dir)
        
        print("current room: ", player.current_room.id)
        print("visited rooms: ", visited_rs, len(visited_rs))
        print("\n")

        print("length: ", len(traversal_path))


traverse()




"""
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
"""