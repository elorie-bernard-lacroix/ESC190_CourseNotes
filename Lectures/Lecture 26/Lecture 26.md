## Heap Order property
* each node is smaller or equal to its children
* therefore, the root is its minimum (makes finding minimum easy)

* insert: initially place the new value at the leftmost empty space in the bottom level of the heap
    * heap remains a complete tree
    * might break the heap order property
* to fix this, percolate the value up the tree until it is in an appropriate spot (use swapping with parent until it reaches the right spot)

insert algorithm:
```python
def insert(x):
    k = n + 1
    pq[k] = x
    while (k > 1 and pq[k/2] > pq[k])
        swap(pq[k], pq[k/2])
        k = k / 2
```

extract minimum algorithm: 
```python
extract_min()
    min = pq[1]
    swap(pq[1], pq[n])
    n = n-1
    k = n
    while (2*k <= n)
        j = 2*k
        if (j < n and pq[j] > pq[j+1]) 
            j = j+1 # want to exchange with the smaller child since the smaller
            # child can be a parent of the larger one
        if (pq[k] <= pq[j])
            break
        swap(pq[k], pq[j])
        k = j
    return min

```

complexity:
* height of a tree: the longest path from node to leaf
    * n <= 2^0 + 2^1 + 2^2 + ... 2^h = 2^(h+1) - 1
    * n > 2^0 + 2^1 + ... + 2^(h-1) = 2^h - 1
* insert and extract min need at most h swaps (start at the top -> bottom or bottom -> top)
* O(h) = O(log(n)) -- pretty fast


## Dynamic Programming
* a set of techniques that work on some problems (but people use it differently)
* programming in this context means optimization

# Memoization
* keeping track of values that have already been computed
* example with the recursive fibonacci function
```python
def fib(n, mem = {}):
    if n in mem:
        return mem[n]
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]

```
* only compute each entry in mem once
* fib(n-1) + fib(n-2) does not produce internal calls to fib
* Compute n entries in mem, each taking constant time
* O(n) time (assuming addition is constant time)

dynamic programming approach
*  Solve subproblems, and store the solutions to those subproblems
*  Use solutions to small subproblems to compute solutions to larger problems

```python
def fib_iter(int n):
    fib_list = [0] * n
    fib_list[0:2] = [0, 1]
    for i in range(2, n+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]

```


