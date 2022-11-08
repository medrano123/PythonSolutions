# Giovanni Medrano



import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)

class Edge(object):
    def __init__(self, s, f, w=1):
        self.start = s
        self.finish = f
        self.weight = w

class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1
    def get_adj_unvisited_vertex_special(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 and not (self.Vertices[i]).was_visited():
                return i



        return -1

    def get_vertices(self):
        nVert = len(self.Vertices)
        copy = []
        for i in range(nVert):
            copy.append(self.Vertices[i])
        return copy

    def delete_vertex(self, vertex):
        nvert = len(self.Vertices)
        # x = self.get_index(vertexLabel)
        del self.Vertices[vertex]
        del self.adjMat[vertex]
        for row in self.adjMat:
            del row[vertex]


    # do a depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us rest the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        return
    def has_cycle(self):
        nVert = len(self.Vertices)
        list_of_cycles = []
        for i in range(nVert):
            for x in range(nVert):
                (self.Vertices[x]).visited = False
            list_of_cycles.append(self.cycle_dfs(i))
        # the stack is empty, let us rest the flags
        for i in range(nVert):
            (self.Vertices[i]).visited = False
        if True in list_of_cycles:
            return True
        return False

    def cycle_dfs(self, v):
        # create the Stack
        theStack = Stack()
        # mark the vertex v as visited and push it on the Stack
        #self.Vertices[v].visited = True
        theStack.push(v)
        x=[]
        # visit all the other vertices according to depth
        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex_special(theStack.peek())
            if u == -1:
                u = theStack.pop()
            elif u == v:
                return True
            else:
                (self.Vertices[u]).visited = True
                theStack.push(u)
                x.append(u)
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        topo_queue = Queue()
        list_of_vertices = []
        topo_queue = self.topo_helper(topo_queue)
        while not topo_queue.is_empty():
            new_vertex = topo_queue.dequeue()
            list_of_vertices.append(new_vertex.get_label())
        return list_of_vertices

    def topo_helper(self, topo_queue):
        list_of_vertices = []
        temp_list = []
        nVert = len(self.Vertices)
        if nVert > 0:
            for i in range(nVert):
                if self.in_degree(i) == 0:
                    temp_list.append(i)
                    #            temp_list.sort()
            delete_count = 0
            for i in temp_list:
                topo_queue.enqueue(self.Vertices[i - delete_count])
                self.delete_vertex(i - delete_count)
                delete_count += 1
            self.get_vertices()
            self.topo_helper(topo_queue)

        return topo_queue

    def in_degree(self, idx):
        counter = 0
        for row in self.adjMat:
            if row[idx] != 0:
                counter += 1
        return counter



def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        print(city)
        cities.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)
    print(num_edges)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        print(edge)
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # print the adjacency matrix
    print("\nAdjacency Matrix")
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(cities.adjMat[i][j], end=" ")
        print()
    print()

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()
    print(start_vertex)

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)
    print(start_index)

    # do the depth first search
    print("\nDepth First Search from " + start_vertex)
    cities.dfs(start_index)
    print()


if __name__ == "__main__":
    main()
