"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = []


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        if v1 in self.vertices:
            self.vertices[v1].insert(0, v2)
        else:
            self.vertices[v1] = [v2]

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                #print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)



            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack() #Depth first is a Stack. Could also do this with a list with append and pop().
        visited = set() #Sets won't save duplicates but also won't save order. Might be problematic later.
        q.push(starting_vertex) #Add starting node to the stack.
        while q.size() > 0:
            v = q.pop() #Removes last item in the stack
            if v not in visited: #Checks if removed item is in the set.
                #print(v) #Prints if not. Mostly to pass tests. Could append this to a new list if we wanted.
                visited.add(v) #Add to set.
                for neighbor in self.get_neighbors(v): #Poor man's recursion.
                    q.push(neighbor) #Add each neighbor to the stack.

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

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


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
        #same as bfs, but with a stack and push and pop
        q = Stack()
        visited = set()

        q.push([starting_vertex])

        while q.size() > 0:

            path = q.pop()

            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path
                
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex)


        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
