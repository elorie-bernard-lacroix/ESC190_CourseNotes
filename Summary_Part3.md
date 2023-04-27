# Data Structures Summary

## Table of Contents
- [Data Structures Summary](#data-structures-summary)
  - [Table of Contents](#table-of-contents)
  - [What is an Absract Data Type (ADT)?](#what-is-an-absract-data-type-adt)
  - [Boilerplate Code for Data Structures](#boilerplate-code-for-data-structures)
    - [**Implementation in C**:](#implementation-in-c)
    - [**Implementation in Python**:](#implementation-in-python)
- [Examples of Data Structures](#examples-of-data-structures)
  - [Linked Lists](#linked-lists)
  - [ArrayList](#arraylist)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Priority Queues \& Heaps](#priority-queues--heaps)
    - [Heaps](#heaps)
  - [Graphs](#graphs)
    - [Implementation](#implementation)
  - [Hash Tables](#hash-tables)

## What is an Absract Data Type (ADT)?
* any collection of values, together with operations on those values
  * ints with operations +, -, *, %, /
  * lists with operations insert, remove, get

## Boilerplate Code for Data Structures
### **Implementation in C**:
```C
#if !defined(STRUCT_H)
#define STRUCT_H

typedef struct new_name 
{
    dataType member1;
    dataType member2;
    ...
} new_name;

void insert(new_name *p_struct, dataType data){
    // insert code here
}

void remove(new_name *p_struct, dataType *data){
    // insert code here
}

void get(new_name *p_struct, dataType data){
    // insert code here
}

#endif


```
**typedef keyword**: typedef function allows users to provide alternative names for the primitive and user-defined data types.

### **Implementation in Python**:
```python
class ADT:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, data):
        self.data.append(data)
        self.size += 1

    def remove(self, data):
        self.data.remove(data)
        self.size -= 1

    def get(self, index):
        return self.data[index]

```
  


# Examples of Data Structures
## Linked Lists
* used to dyamically add elements more effectively
* consists of nodes which have
  * data: the actual data you need to store
  * next: the address of the next node
* operations:
  * insert: O(1)
  * remove: O(1)
  * get: O(n) or O(1) if index is known
* note: it takes up more space in memory but it is more time efficient in general

Implementation:
```C
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
    int size;
} LL;

void create_node(node **p_n, int data)
{
    *p_n = (node*)malloc(sizeof(node));
    (*p_n)->data = data;
    (*p_n)->next = NULL;
}


void create_LL_from_data(LL **p_LL, int *data_arr, int size)
{
    (*p_LL) = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0; // initialize size to 0
    
    // keep track of the last node of the linked list
    node *tail = 0;

    for(int i = 0; i < size; i++){

        // n is a pointer to a node with data = data[i], next = NULL
        node *n;
        create_node(&n, data_arr[i]);

        // If the last node is the 1st node
        if(tail == 0){
            (*p_LL)->head = n;
        }

        // If the last node is not the 1st node
        else{
            // append the new node to the end of the linked list
            tail->next = n;
        }

        // update the tail
        tail = n;

        // update the size
        (*p_LL)->size++;
    }
}

int main(){
    int data_arr[] = {1, 2, 3, 4, 5};
    LL *p_LL;
    create_LL_from_data(&p_LL, data_arr, 5);
}
```

## ArrayList


## Stacks
**Definition**: Collection of elements where the last elements in are the first out (LIFO).
It uses the following operations:
* `push`: inserts an elements at the end of the collection
* `pop`: removes and returns the last (most recent) element of the collection

**Time Complexity**:
* push: O(1) (unless it is written in C and we need to realloc space)
* pop: O(1) -- same complexity to retrieve an element by index

```python
class stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        res = self.data[-1]
        del self.data[-1]
        return res

```



## Queues
**Definition:** Collection of elements where the first elements in are the first out (FIFO). It uses the following operations:
* `enqueue`: inserts an element at the end of the collection
* `dequeue`: removes and returns the first (least recent) element of the collection  


**Time Complexity**:
* enqueue: O(1) (but it's O(n) in C if we need to reallocate space)
* dequeue: O(1) -- retrieving elements by index is also O(1)

```python

class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        res = self.data[0]
        del self.data[0]
        return res

```
To replace the need to shift over all the elements when you `dequeue()`, you can make an improved queue with linked lists

```python
class LLQueue:
    def __init__(self):
        self.data = linkedlist.LinkedList()

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self, element):
        res = self.data.head.value
        self.data.head = self.data.head.next
        return res

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get_i(self, i):
        # return the value at index i
        cur = self.head
        for j in range(i):
            cur = cur.next
        return cur.value

    def append(self, value):
        '''Add a new node with the value value to the end of the list'''
        # Create a new node
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node
    
    def insert(self, value, i):
        '''Insert a node with the value value at index i'''
        new_node = Node(value)

        if i == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            cur = self.head
            for j in range(i-1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        
        if new_node.next == None:
            self.tail = new_node

    def __str__(self):
        cur = self.head
        s = ""
        if(cur == None):
            return "Empty list :("
        
        while cur != None:
            print(cur)
            s += str(cur) + " -> "
            cur = cur.next
        return s[:-4] # remove last arrow 

```  

## Priority Queues & Heaps
**Definition:** A queue who's first element dequeued is the one with the highest priority.
* `insert(S,x)` : adds a new element with priority, x, to the priority queue, s.
* `min(S)` : returns the element with the smallest value from the priority queue (S)
* `extract_min(S)` : removes and returns the element with the smallest value from the priority queue

Most efficient implementation: Heaps

### Heaps
**Definition:** An implementation of a priority queue in the form of a binary tree (read as a list). 
* Binary Tree: collection of nodes, where each node has two children, except the nodes at the bottom. The nodes at the bottom right are filled in last.
* Constraint: The parent is smaller than both children.
* Stored as an array (e.g. [_, a, b, c, d ...] where a is the top most element, followed by the left then right child). The first element in left blank

Operations:
* Adding elements: 
  * add to the bottom and percolate up to its position
  ```python
  def heapify_up(self):
        index = self.size 
        while self.has_parent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index) 
   ```
* Finding elements:
  * given a node at index i: 
    * `parent(i) = i/2 `
    * `left(i) = 2i`
    * `right(i) = 2i + 1`
  * index of first element of each row given by `2^n`

* `extract_min()` : 
  * need to switch top one with the last one, remove what is now the last element, and perculate what is now the first element down to its proper place
  * when perculating down, if element is larger than both children, swap with smaller one

  ```python
  def heapify_down(self):
        index = 1
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index
  ```
**Complexity**:
* inserting and extracting the min of a heap is O(height of heap) = O(log2(n))

## Graphs
**Definition:** consists of a set of vertices (nodes), V, connectd by a set of edges, E.
* **Directed Graphs**: Edges have associated directions.
* **Weighted Graphs**: Edges have associated weights.

**Terminology**:
* **Adjacent**: connected by an edge
* **Path**: sequences of ertices connected by edges (length = number of edges)
* **Cycle**: path that starts and ends at same vertex
* **Acyclic graph**: a graph without cycles
* **Simple path**: path that doesn't contain any repeated vertices
* **Simple cycle**: cycles that does not ocntain any repeated vertices
* **Connection**: there is a path between the vertices
* **Connected Component**: A subset of vertices where every pair of vertices in the subset is connected
* **Degree of vertex**: number of connected edges


### Implementation 

* **Adjacency List:** list of lists where L[i] is a list of all the vertices that are adjacent to vertex *i*
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

* **Adjacency Matrix:** n x n matrix where M[i][j]=1 if there is an edge between vertex *i* and vertex *j*, M[i][j]=0 otherwise







## Hash Tables
