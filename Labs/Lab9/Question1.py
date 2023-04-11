import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []
        self.distance_from_start = np.inf

class Con:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

def dijkstra(start, end):
    start.distance_from_start = 0
    visited = set([start])
    current = start
    while current != end:
        
        cur_dist = np.inf
        cur_v = None
        for node in visited:
            for con in node.connections:
                if con.node in visited:
                    continue
                if cur_dist > node.distance_from_start + con.weight:
                    cur_dist = node.distance_from_start + con.weight
                    cur_v = con.node
    
        current = cur_v
        current.distance_from_start = cur_dist
        visited.add(current)
    return current.distance_from_start


if __name__ == "__main__":
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")

    con1 = Con(nodeB, 2)
    con2 = Con(nodeC, 8)
    con3 = Con(nodeD, 8)
    con4 = Con(nodeD, 2)
    con5 = Con(nodeC, 2)

    nodeA.connections.append(con1)
    nodeA.connections.append(con2)
    nodeB.connections.append(con3)
    nodeC.connections.append(con4)
    nodeB.connections.append(con5)

    print(dijkstra(nodeA, nodeD))
                                                
