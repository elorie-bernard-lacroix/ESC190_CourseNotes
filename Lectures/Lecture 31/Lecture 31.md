Review of a problem in Q0
```C
#include "list.h"
#include <stdlib.h>
#include <stdio.h>


typedef struct myLL {
    node *head;
    int size;
} myLL;

int LL_elem_in_list(void *list, data, int data)
{
    int size = ((myLL *)list)->size;
}

```


# Graphs

how to get a handle on dynamic programming: 
* know how to use several techniques
* practice, practice, practice! (he posted some leet code problems for this)
  * start with easy ones, go to medium, etc.

note on adjacency matrix:
* when every edge between nodes are reciprocal, matrix is symmetrical

## adjacency list
* choose a starting point anywhere
* for every node it is connected to: [2, [8, [...]]]
* the parent list is the list of all the elements you started with
* if there is a weight associated with each edge: [2, weight, [8, weight, [...]]]


## complexity of operations
* is there an edge between vi and vj?
  * adjacency matrix: O(1)
  * adjacency list: O(d) (d is the max degree of any node in the graph)
    * how many nodes one node is connected to
* find all vertices adjacent to vi
  * adjacency matrix: O(|v|)
    * |v|: the number of vertices in the graph
  * adjacency list: O(d)

## space requirements
* adjacency matrix: O(|v|^2)
  * need to store |V|^2 matrix entries
* adjacency list: O(|V| + |E|)
  * |V|: number of vertices
  * |E|: number of edges
  * so space requirement is a1|V| + a2|E|, where a1 and a2 are constants

## graph traversal
* want to visit (e.g. in order to print) each vertex exactly once

pseudo code:
```txt
while(there are non-visited nodes)
    initialize a data structure DS
    add a non-visited vertex vi to DS
    mark vi as visited 
    while(DS is not empty)
        remove vertex vj from DS
        mark vj as visited 
        add non-visited vertices adjacent to vj to DS
        
```

two frameworks:
* breadth first (the one we will discuss today): 
  * visit all the vertices at distance 0 from the starting vertex
  * then visit all the vertices at distance 1 from the starting vertex
  * etc.
* depth first:
  * visit all the way through the possible paths first

application
```C

// starting position in chaess, want to list out all the possible games
// possible moves for white: e2-e4, f2-f3, etc.
//                          / / \ \ / / \ \       
// possible moves for black: e7-e5, f7-f6, etc.
// ..................................................
// start with listing possible 1-moves, 2-moves, etc.




```



