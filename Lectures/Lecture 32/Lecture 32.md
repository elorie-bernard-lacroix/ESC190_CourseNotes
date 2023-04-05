## graph traversal
want to visit (e.g. in order to print) each vertex exactly once

## depth first traversal

pseudo code:
```txt
while (there are non-visited nodes)
    initialize a data structure DS
    add a non-visited vertex vi to DS
    mark vi as visited 
    while (DS is not empty)
        remove vertex vj from DS
        mark vj as visited 
        add non-visited vertices adjacent to vj to DS
```
data structure file:
```python

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbours = []

class Graph:
    def __init__(self):
        self.nodes = []


```

separate file:
```python
from graph1 import Graph, Node
def bfs(graph):
    visited = set() # average insertion and lookup time is O(1)

    for starting_node in graph.nodes:
        queue = [graph.nodes[0]]
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                print(node.data)
                visited.add(node)
                queue.extend(node.neighbours)

# can initialize set with myset = set([1, 2, 3])

def dfs(graph):
    visited = set() # average insertion and lookup time is O(1)

    for starting_node in graph.nodes:
        stack = [graph.nodes[0]]
        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                print(node.data)
                visited.add(node)
                stack.extend(node.neighbours)

```

### let's try something else
Race to 21:
* start at 0, each player can go +1 or +2
* whoever gets to 21 first wins
* print all possible games of Race to 21


start with 0, which is connected to two possible game states, which is connected to more responses, etc.

graph:
nodes: game states for race to 21
edges: possible moves (+1, +2)

```txt

            [0]
       /           \
    [0, 1]          [0,2]
     /    \
[0, 1, 2] [0, 1, 3] .....

```

```python
from graph1 import Graph, Node

def filter_neighbours(neighbours):
    res = []
    for n in neighbours:
        if n <= 21:
            res.append(n)
    return res

def bfs21():
    # starting node: [0]
    # don't have node.neighbours: need to generate them
    # don't need to worrt about returning to visited nodes, since cannot go back from +1 or +2 to previous game state

    queue = [[0]]
    while len(queue) > 0:
        node = queue.pop(0)
        if node[-1] == 21:
            print(node)
        neightbours = filter_neighbours([node[-1] + 1, node+ [node[-1] + 2]])
        queue.extend(neighbours)

```

We can also write a depth first algorithm recursively:

```txt
DFS(vi)
    mark vi as visited
    for each non-visited vertex vj adjacent to i
        DFS(vj)
```

