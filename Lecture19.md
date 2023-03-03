# Lecture 19: Abstract Data Types
* Any colection of values toegther with operations on those values
  * int with operations '+', '*';
  * lists with operations insert and remove
* specifies what valuess are represented and what operations can be performed but not how to store the values or how to carry out the operations
* more important for specification *provide modularity, and resuse - usage is independent of implementation)
* data structure is an implementation of an ADT-- a way to represent the values and algorithms for each operation
  * e.g. the actual implementation (I'll do a linked list and this is how it works)

lists
* A list is an ordered collection of data items that supports the
following operations
* Insert(list, i, x): add item x at index i of list—the item
previously at index i, and all following items, are “shifted up”
by one index to make room for x
* Remove(list, i): remove the item at index i in list—the item
previously at index i + 1, and all following items, are “shifted
down” by one index to leave no gap
* Get(list, i): return the item at index i in list
Every operation assumes that list contains at least i items
* We defined the list ADT in a very abstract way, only
specifying what the outcome of each operation should be
* Internally, this behaviour can be implemented any way we like;
in particular, lists can be implemented using arrays


note on robustness
* adding statements like the one below, will make the code more robust, however it is not necessary on the midterm or exam
```C
if(array[index] == NULL){
  fprintf("Index out of bounds");
  return
}
```

## review of last lab
* take a look at the corresponding lab files in lab5 folder: list.h, linekdlist.c, and main.c
* to compile all of them you can first compile linkedlist.c in the termindal (gcc main.c linkedlist.o)

```txt
gcc main.c linkedlist.o

gcc arraylist.c

gcc -lm main.c
```





 

