
## Priority Queue
A queu where the first element dequeued is the one with the highest priority
Uses: 
* simlulate a real-world system queue organized by priority
    * pateints in a hospital
    * files requested from a server
* A* search

Functions:
* insert(S, x): add a new element with priority x to priority queue S
* min(S): return the element with the smallest value from the priority queue
* extract_min(S): remove and return the element with the smallest value from the queue

implementation:
```python

class PriorityQueueSlow:
    def __init__(self):
        self.head = []
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1              # O(1) (O(size) worst case)

    def extract_min(self):
        if self.size == 0:
            return None
        min = self.data[0]
        loc_min = 0
        for i in range(1, self.size):   # O(size)
            if self.data[i] < min:
                min = self.data[i]
                loc_min = i
        del self.data[loc_min]          # O(size)
        self.size -= 1
        return min                      # O(size) in total

```

sorted array or linked list 
* O(n) for insert
( O(1) for min/extract)

```python
class PriorityQueueSortedArray:
    def __init__(self):
        self.head = []
        self.size = 0

    def insert(self, value):  # this is sorted now
        # assume self.data is currently sorted in non-increasing order
        # find the location where value should be inserted
        for i in range(self.size):
            if value < self.data[i]:
                break
        # self.data[i] is the first element that is smaller than value
        # so we should insert value before self.data[i]

        self.data.insert(i, value)


        self.size += 1              # O(size) because eventually need to shift all elements 
                                    # after location i, which might be 0

    def extract_min(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop()       # O(1) because we are popping from the end of the list
                                     # never need to shift any elements

        

```


## heaps
* a tree with eery node having two children, except the "leaves" (nodes at the bottom with no children)
* every leaf is as far left as possible of the last level
* the tree is specifically binary (each node has at least two children)
* it is complete (every node that is not on the bottom right should have two children)

how is it stored:
* could store similarly to linked lists, with each node have two "children"
* because the tree is complete, we can (and will) store the heap as an array

            a                       (index: 1 = 2^0)
         /     \
        b       c                   (indices: 2^(k-1), 2^(k-1)+1, ...)
      /   \    /  \
     d     e  f    g                (indices: 2^k, 2^k+1, 2^k+2, ...)

array: [a, b, c, d, e, f, g]

* given a node at index

What is the index of e:
* 1 + 1 (a) + 2 (b and c) + 1 (d) = 5

How many nodes at levels 1, 2, 3, .. , k:
2^0 + 2^1 + ... + 2^(k-1) = 2^k - 1

How many nodes at level (k+1):
2^k

* given a node at index i 

