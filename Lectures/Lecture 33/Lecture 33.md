# Lecture 33

```python

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node.data)
            visited.add(node)
            stack.extend(node.neighbours)
    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start.data)
    visited.add(start)
    for neighbour in start.neighbours:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)
    return visited

# could also pop from the stack and add to visited
```

```txt

Example:
A -> C
 \ 
  B -> D

D -> D is printed, stack: [C], visited: [A, B, D]
|
  B -> B is printed, stack: [C, D], visited: [A, B]             C: C printed
   |                                            /             
   A -> A is printed, stack: [C, B], visited: [A]

```

```python

def fact(n):
    if n == 1:
        return 1
    else: 
        return  n * fact(n-1)


def trace_factorial(n):
    local_n = [n]
    i = n
    while i != 1:
        local_n.append(i-1)
    res = 1
    while len(local_n) > 0:
        res *= local_n.pop()
    return res

    # recursive functions can resemble a stack



```

# More about Graphs
## Shortest Path (SP)

* given a weighted connected graph G=(V,E), and a pair of vertices v_s, and v_d?
* path with th esmallest sum of edge weights


**Dikstra's algorithm**

```txt
Dijkstra(G = (V, E), source) # V is set of vertices, E is set of edges
    S = {source}    # set of visited nodes
    d (source) = 0  # d(v) is shortest path from source to v

    while S ! = V
        choose v \in V/S s.t. d(u) + |(u, v)| is minimized (u \in S)
        add v to S, set d(v) = d(u) + |(u, v)|

```

* complexity based on simlest implementation: O(V^2)
  * this implementation adds one vertex to S, searches through all possible additional vertices

* complexity based on fancier implementation: O(E log V)
  * this implementation uses a priority queue to find the next vertex to add to S
  
  



