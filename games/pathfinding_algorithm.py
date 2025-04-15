from math import sqrt

# Distance and heuristic functions


def distance(current, target): return sqrt(
    (target[0]-current[0])**2+(target[1]-current[1])**2)


target = (0, 0)


def heuristic(node, target=target): return distance(
    node.coordinates, target=target)


class Node:
    def __init__(self, coordinates,):
        self.coordinates = coordinates
        self.x, self.y = self.coordinates[0], self.coordinates[1]
        self.heuristic = heuristic(self)
        self.value = distance(current.coordinates,
                              self.coordinates) + heuristic(self)
        self.north = Node(self.x, self.y+1)
        self.east = Node(self.x+1, self.y)
        self.south = Node(self.x, self.y-1)
        self.west = Node(self.x-1, self.y)


start = (-9, -1)
current = Node(start)
target = Node(target)


# TODO: Check if this is necessary DON'T REMOVE IT
# def in_grid(node, grid,): return (abs((x := node.coordinates[0])-(h := (grid.origin[0]))+(
#     y := (node.coordinates[1])-(k := grid.origin[1])))) + abs((x-h)-(y-k)) <= grid.side_length

def Solve_A_Star(current,target,blocked):
    