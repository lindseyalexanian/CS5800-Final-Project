import random
import sys


class KruskalMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes, self.edges = self.generate_graph()
        self.maze = self.create_maze()
        self.maze_edges = self.get_maze_edges

    def get_maze_edges(self):
        maze_edges = {}
        for s in sorted(self.maze):
            if s[0] not in maze_edges:
                maze_edges[s[0]] = [s[1]]
            else:
                maze_edges[s[0]].append(s[1])
            if s[1] not in maze_edges:
                maze_edges[s[1]] = [s[0]]
            else:
                maze_edges[s[1]].append(s[0])
        return maze_edges

    def generate_graph(self):
        nodes = set()
        edges = set()
        x = self.width
        y = self.height

        for i in range(x):
            for j in range(y):
                nodes.add((i, j))
                if i > 0:
                    e1 = (i - 1, j)
                    edges.add(((i, j), e1))
                if i < x - 1:
                    e2 = (i + 1, j)
                    edges.add(((i, j), e2))
                if j > 0:
                    e3 = (i, j - 1)
                    edges.add(((i, j), e3))
                if j < y - 1:
                    e4 = (i, j + 1)
                    edges.add(((i, j), e4))
        return nodes, edges

    def get_random_weights(self):
        edge_weights = [(random.randint(1, 4), x, y) for (x, y) in self.edges]
        return edge_weights

    def create_maze(self):
        weights = self.get_random_weights()
        groups = {n: n for n in self.nodes}
        ranks = {n: 0 for n in self.nodes}
        solution = set()

        def find(u):
            if groups[u] != u:
                groups[u] = find(groups[u])
            return groups[u]

        def union(x, y):
            x, y = find(x), find(y)
            if ranks[x] > ranks[y]:
                groups[y] = x
            else:
                groups[x] = y
            if ranks[x] == ranks[y]:
                ranks[y] += 1

        for w, x, y in sorted(weights):
            if x != y:
                if find(x) != find(y):
                    # adding edge to the solution
                    solution.add((x, y))
                    union(x, y)

        return solution


maze = KruskalMaze(5, 5).create_maze()

# initialize matrix
matrix = []

for i in maze:
    list_i = list(i)
    matrix.append(list_i)

### some formatting fun

import string

class Point_Maze():

    def __init__(self, maze, width, height):
        self.maze = maze
        self.width = width
        self.height = height

    def use_letters(self):
        letters = string.ascii_lowercase[0:26]
        #letters = string.ascii_lowercase[0:self.width*self.height]
        point_names = []

        for i in letters:
            point_names.append(i)

        return point_names

    def make_maze_dict(self):

        letter_list = self.use_letters()

        my_points = []
        for i in range(0, self.width):
            for j in range(0, self.height):
                my_points.append((i, j))

        maze_dictionary = {my_points[item]: letter_list[item] for item in range(len(my_points))}

        return maze_dictionary

    def final_maze_gen(self):

        letter_maze_dict = self.make_maze_dict()

        final_maze = []

        # loop through matrix dimensions
        for i in self.maze:
            # initialize (or re-initialize) edge
            my_edge = []
            for j in i:
                # print(j)
                u = letter_maze_dict[j]
                #print(u)
                # add point to edge
                my_edge.append(u)
            # add edge to maze
            final_maze.append(my_edge)

        return final_maze






class Adjacency:

    def __init__(self, maze, star_pt, end_pt):
        self.maze = maze
        self.star_pt = star_pt
        self.end_pt = end_pt


    def make_adj_list(self):

        adj_list_keys = []

        for i in self.maze:
            for j in i:
                adj_list_keys.append(j)

        adj_list_keys = sorted(adj_list_keys)
        adj_list = dict.fromkeys(adj_list_keys)
        for i in adj_list.keys():
            adj_list[i] = []

        for i in self.maze:
            for j in i:

                my_index = i.index(j)

                if my_index % 2 != 0:
                    prev = my_index - 1
                    adj_list[i[prev]].append(j)

                else:
                    next_one = my_index + 1
                    adj_list[i[next_one]].append(j)

        return adj_list

    def make_adj_matrix(self):

        adj_list = self.make_adj_list()

        adj_matrix = [[0] * len(adj_list) for _ in range(len(adj_list))]

        # get letters again
        my_letters = string.ascii_lowercase[0:26]

        for key, val in adj_list.items():
            ascii_index_key = my_letters.index(key)
            for item in val:
                ascii_index_val = my_letters.index(item)
                adj_matrix[ascii_index_key][ascii_index_val] = 1

        #for line in adj_matrix:
            #print(line)

        return adj_matrix




### let's solve the maze!


class Solve_Me:

    def __init__(self, adjacency_list, start_pt, end_pt, path_length, vertex_count):
        self.adjacency_list = adjacency_list
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.path_length = path_length
        self.vertex_count = vertex_count

    def solve_maze_dfs(self):

        dfs_passed_nodes = [0 for _ in range(vertex_count)]
        previous_nodes = [-1 for _ in range(vertex_count)]

        self.dfs(self.start_pt, dfs_passed_nodes, previous_nodes)
        my_shortest_route = self.compile(previous_nodes)
        return my_shortest_route

    def bfs(self, source, sink):

        # initialize list to keep track of nodes we've passed through
        passed_nodes = []

        # initialize priority queue (w/ source node)
        priority_queue = [[source]]

        # if source and sink are the same node, exit and give exit message
        if source == sink:
            sys.exit("Shortest path is 0; source & sink are the same node")

        # while priority queue is not empty
        while len(priority_queue) > 0:
            # remove item at top of priority queue #bye
            my_path = priority_queue.pop(0)
            # get node
            node = my_path[-1]

            # if the node hasn't been passed through yet
            if node not in passed_nodes:
                # initialize adjacency list dictionary and add node as a key
                adj_nodes = self.adjacency_list[node]

                # for each key in the list of adjacent nodes
                for i in adj_nodes:
                    new_path = list(my_path)
                    new_path.append(i)
                    priority_queue.append(new_path)

                    if i == sink:
                        return new_path

                # add node to list of nodes we've passed through
                passed_nodes.append(node)

        # else return none
        return None


    def dfs(self, vertex, dfs_passed_nodes, prev):

        """Run a depth first search! Hooray!"""


        # increment path length (+1) each time we run dfs
        self.path_length += 1


        # if path length is shorter than infinity
        if self.path_length > sys.maxsize:
            return


        if vertex == self.end_pt:
            sys.maxsize = self.path_length
            return

        # add vertex to the list of visited nodes
        dfs_passed_nodes[vertex] = 1


        for i in range(self.vertex_count):
            if adj_matrix_test[vertex][i] == 1 and dfs_passed_nodes[i] == 0:
                adjacent_node = i

                # update the preceding vertex of the adjacent nodes
                prev[adjacent_node] = vertex

                # run dfs
                self.dfs(adjacent_node, dfs_passed_nodes, prev)

        # now we have to backtrack, so go back one in the path
        self.path_length = self.path_length - 1

    def compile(self, prev):
        """Now let's actually compile the route from the path we traversed!"""

        # initialize the path tracker
        path_tracker = []

        # set vertex as the end point (input)
        vertex = self.end_pt

        # while the start node is not passed
        while vertex >= 0:
            # add the vertex to the path
            path_tracker.append(vertices_names[vertex])
            # update vertex with previous one (backtrack)
            vertex = prev[vertex]

        # reverse, reverse!
        path_tracker.reverse()

        # return the updated route
        return path_tracker





### time for the driver code! Almost there!
if __name__ == "__main__":


    my_maze = Point_Maze(matrix, 5, 5).final_maze_gen()
    print(my_maze)
    # print(my_maze)

    # print(matrix)

    # find start and end point in generated maze
    start, end = my_maze[0], my_maze[len(my_maze) - 1]

    # how many vertices?
    vertices = len(my_maze)

    # get adjacency list
    adj_list_test = Adjacency(my_maze, start, end).make_adj_list()
    # print(adj_list_test)

    # get adjacency matrix
    adj_matrix_test = Adjacency(my_maze, start[0], end[1]).make_adj_matrix()

    # print a phrase, any phrase!
    print(f"Here be the solutions!\n")

    # vertices or nodes
    vertices_names = list(adj_list_test.keys())
    # number of vertices
    vertex_count = len(adj_matrix_test)



    # get letters again
    global_letters = string.ascii_lowercase[0:26]
    start_index = global_letters.index(start[0])
    end_index = global_letters.index(end[1])

    # get bfs solution
    bfs_solution = Solve_Me(adj_list_test, start_index, end_index, 0, vertex_count).bfs(start[0], end[1])
    # print result!
    print(f"Shortest path (BFS) = {' '.join(bfs_solution)}\nlength of shortest path: {len(bfs_solution)}\n")

    # get dfs solution
    dfs_solution = Solve_Me(adj_list_test, start_index, end_index, 0, vertex_count).solve_maze_dfs()
    #print(final_route)
    print(f"Shortest path (DFS) = {' '.join(dfs_solution)}\nlength of shortest path: {len(dfs_solution)}")


    # "Exit, pursued by a bear"