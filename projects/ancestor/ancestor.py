
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
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1] = [v2]

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

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

def earliest_ancestor(ancestors, starting_node):

    a_graph = Graph()
    #build graph
    for family in ancestors:
        parent = family[0]
        child = family[1]

        a_graph.add_vertex(parent)
        a_graph.add_vertex(child)
        a_graph.add_edge(parent, child)

    
    lendict = {}
    #search every entry leading to the input for the longest length
    for i in a_graph.vertices:
        search = a_graph.bfs(i, starting_node)

        if search is not None:
            lendict[i] = len(search)
    #find key of the longest length search, then pair with original vertices entry
    longest_tree = max(lendict.values())
    longest_trees = [k for k,v in lendict.items() if v == longest_tree]

    #if input has no parent return -1
    if lendict[min(longest_trees)] == 1:
        return -1
    
    #return smallest int parent if more than 1
    return min(longest_trees)






    print(a_graph.vertices)



    return "boom bb"


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))

