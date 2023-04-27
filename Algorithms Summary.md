# Sorting Algorithms

# Search Algorithms

## Graph Traversal 

## Shortest Path

# Dynamic Programming
**Definition**: A set of techniques for problem solving (rbeaking up a problem into sub-tasks and uses teh results from those sub tasks to solve the original problem)
1. Dvide a complex problem into a number of simpler overlapping problems
2. Define a relationship between solutions to more complex problems and solutions to simpler problems. This is known as a Bellman Equation. For example:
   1. Fibonacci: 
   0               --> i = 0
   1               --> i = 1
   F(i-1) + F(i-2) --> i >= 2
3. Store solutions to each subproblem (only solving each once)
4. Use stored solutions to solve original problem

**Memoization**: Maintaining a table of values that were already computed so that we don't have to recompute them. May also be more effective than an iterative approach that computes all previous values rather than only the ones we need.

Example:
```python
def fib(n, mem = {}):
    if n in mem:
        return mem[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return mem[n]
```

This can also be done without recursion, but with a list instead that gets updated:

```python
def fib_iter(int n):
    fib_list = [0] * n
    fib_list[0:2] = [0, 1]
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[n]
```
