
# More practice will dynamic, recursive programming
```python

import numpy as np

def make_change_rec(denom, target, memo = {}, solns = {}):

    if target in memo:          # checking if solution has already been computed
        return memo[target], solns[target]

    if target == 0:             # base case
        memo[0] = 0
        solns[0] = []
        return memo[target], solns[target]    # returns all solutions  
    if target < 0:
        memo[target] = None     # 
        solns[target] = None
        return None

    min_coins = np.inf
    min_soln = None
    for d in denom:
        if target - d >= 0:
            cur_min = make_change_rec(denom, target - d, memo, solns)
            cur_min += 1
            if cur_min < min_coins:
                min_coins = cur_min
                min_soln = solns[target-d] + [d] # inefficient but this is ignored, initialized solutions

    memo[target] = min_coins
    solns[target] = min_soln
    return memo[target], solns[target]

```

Possible runtime analysis:
* number of calls that make recursive calls: at most target + 1
* number of calls that don't make recursive calls: makes at most 3 calls
* at most, we make 3*(target+1) calls due to recursive calls
    * some of the calls will make recursive calls
    * at most, there are 3*(target+1) calls that don't make recursive calls
* in total there are at most 4*(target + 1) calls
* for 3 denominations, the complexity is O(target)
* in general, the complexity is O(len(denom)*target)

# graphs
* a graph G = (V, E) consists of a set of certices (nodes) V and a set of edge E
* applications:
    * verticies are cities, edges are direct flights between cities, finding the best route
    * vertices are classes, edges connect classs whose scehdules overlap, want to find reasible schedules for a student
    * certices are objectives in memory, edges connect objects that refer to each other, want to know when an object can be freed

### undirected graphs and undirected graphs
  * directed: edges have directions associated with them
  * undirected: edges have no direction associated with them
  * weighted graphs: edges have weights associated with them

### terminology
  * Vertex 𝑣1 is adjacent to vertex 𝑣2 if an edge connects 𝑣1 and 𝑣2
  * There exists an edge 𝑒 = (𝑣1, 𝑣2) ∈ 𝐸
  * A path is a sequence of vertices in which each vertex is adjacent to the next one
  * p = (𝑣1, … , 𝑣𝑛)s.t. 𝑣𝑖, 𝑣𝑖+1 ∈ 𝐸
  * The length of the path is the number of edges in it
  * A cycle in a path is a sequence (𝑣1, … , 𝑣𝑛) s.t. 𝑣𝑖, 𝑣𝑖+1 ∈ 𝐸 and 𝑣𝑛, 𝑣1 ∈ 𝐸
  * A graph with no cycles is an acyclic graph 
  * A DAG is a directed acyclic graph
  * A simple path is a path with no repetition of vertices
  * A simple cycle is a cycle with no repetition of vertices
  * Two vertices are connected is there is a path between them
  * A subset of vertices is a connected component of G if each pair of vertices in the subset are connected.
  * The degree of vertex v is the number of edges associated with v

