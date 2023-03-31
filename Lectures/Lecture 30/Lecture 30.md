
# Graphs

* a graph is a set of vertices and edges
* adjacency list: a list of lists, where each list is a list of vertices adjacent to the vertex at the same index
* adjacency matrix: a matrix where the entry at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise

## adjacency list:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

node1 = Node('TO')
node2 = Node('Ottawa')
node3 = Node('Orlando')

node1.adjacent.append(node2)
node1.adjacent.append(node3)
node2.adjacent.append(node1)
node3.adjacent.append(node1)
```
```txt
picture of this graph:
     TO
    /  \
Ottawa Orlando
```

## adjacency matrix:
```txt  
        TO Ottawa Orlando
TO      [0,   1,   1]
Ottawa  [1,   0,   0]
Orlando [1,   0,   0]
```
## pagerank
* a way to rank web pages

M: adjacency matrix of the web graph
* nodes are webpages and edges are hyperlinks between pages

example:
* M[i][j] = 1 if there is a hyperlink from page i to page j
* M[i][i] = 1 always

wihch pages are th emost important?
* operationaize this as: if I start at a random page and follow random links, what is teh probability that I will end up at page 1?

```txt
                                    [1]
                                    [0]
  image the you start at, state v0, [0]
```

* the (unnormalized probabilty of ending up at page i) is Mv0 after one step
* after k steps, the probability of ending yp at page i is (M^k)v0
* the probability of ending up at page i is (M^k)v0
* = (M^k)(a0*w0 + a1*w1 +...+ an*wn), where w0, w1, . . . , wn are eigenvectors of M, in descending order of the eigenvalue of M
* (M^k)v0 - a0^k*w0 = 0

translating to code:
```python
class Graph:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur_num_nodes = 0
        self.nodes = []
        self.indices = {}
        self.adj_array = []
        for i in range(self.capacity):
            self.adj_array.append([None] * self.capacity)

            # now the matrix is set up
            # we need to add nodes and edges

    def expand(self):
        adj_array_new = []
        self.capacity *= 2
        for i in range(self.capacity//2):
            adj_array_new.append([None] * self.capacity)
            adj_array_new[i][:self.capacity//2] = self.adj_array[i]
        for i in range(self.capacity//2, self.capacity):
            adj_array_new.append([None] * self.capacity)

        

    def register_node(name):
        if self.capacity == self.cur_num_nodes:
            self.expand()

        self.nodes.append(name)
        self.indices[name] = self.cur_num_nodes
        self.cur_num_nodes += 1

        for i in range(self.cur_num_nodes):
            self.adj_array[i][self.cur_num_nodes - 1] = 0
            self.adj_array[self.cur_num_nodes - 1][i] = 0

    def connect_by_index(self, index1, index2):
        self.adj_array[index1][index2] = 1

    def connect_by_name(self, name1, name2):
        if name1 not in self.indices:
            self.register_node(name1)
        if name2 not in self.indices:
            self.register_node(name2)

        self.connect_by_index(self.indices[name1], self.indices[name2])

g = Graph(2)
g.connect_by_name('TO', 'Ottawa')


```