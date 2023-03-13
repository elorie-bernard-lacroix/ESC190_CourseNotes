# more info on linked lists

## stack
**definition**: collection of elements with operations, push and pop
* push: add an element to the collection
* pop: remove the most recently added element that was not yet removed
* LIFO: last in, first out

**example**:
```txt
push 1 
push 50
[1, 50]
pop \\ return 50
push 100
push 200
[1, 100, 200]
pop \\ return 200
pop \\ return 100
pop \\ return 1
[ ]
```

**implementation**
```python
class Stack:
  def __init__(self):
    self.data = []
    
  def push(self, item):
    self.data.append(item)  # renaming append to push basically
                            # 0(1), because the vast majority of the time
                            # just need to write to data[len(data)]
                            # worst-case complexity: O(n), because we might need
                            # to move data to an address where ther is space
                            # for another element
  def pop(self):
    # return data.pop() -- this works but we can manually write it for lists
    elem = self.data[-1]    # O(1)
    del self.data[-1]       # same as self.data[len(slef.data)-1]
    return elem
    
if __name__ = '__main__':
  s = Stack()
  s.push(1)
  s.push(50)
  print(s.pop()) # will print 50
```

## queues 
**definition**: a collection of elements with the operations: enqueue and dequeue
* enqueue: add an element to the collection  -- O(1) complexity
* dequeue: remove the least recently added element that was not yet removed -- O(n) complexity
* FIFO: first in, first out

example:
```txt
enqueue 1
[1]
enqueue 50
[50]
dequeue \\ return 1
[1]
```

**implementation**
```python
class Queue:
  def __init__(self):
    self.data = []
    
  def enqueue(self, item):
    self.data.append(item)  # O(1) complexity
  def dequeue(self):
    # return data.pop()
    elem = self.data[0]
    del self.data[0]    # need to move data[1:} to data[0:], O(n)
    return elem

```

another implementation

```python
import linkedlist

# HEAD 

class LLQueue:
  def __init__(self):
    self.data = linkedlist.LinkedList()
    slef.tail = None
    # we added the tail to the LL, so that when it is initialized and every time we append, the tail is updated
    
  def dequeue(self):
    ret_val = self.data.head.value
    self.data.head = self.data.head.next 
    
  def enqueue(self): 
    self.data.append(item) # O(n), because you need to iterate through the list -- based on code in LL, but we can do better
```
