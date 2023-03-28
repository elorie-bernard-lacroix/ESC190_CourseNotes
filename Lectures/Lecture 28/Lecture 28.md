## Overview of Last Week's Lab

traget 8
want to find the min number of coins that add up to the target
canadian coins: 5, 10, 25, 100, 200

OPT(i) := minimum number of coins to make change for i
OPT(0) = 0

OPT(i) = 1 + min(OPT(i-d)) for d in denominations


short-circuiting: When computing A and B, if A is False, don't compute B



```python

import numpy as np

def compute_opt(denominations, target):
    OPT = [None] * (target + 1)
    OPT[0] = 0
    for amt in range(1, target + 1):
        cur_min = None
        for d in denominations:
            if amt - d >= 0:
                if cur_min is None or (OPT[amt - d] is not None and cur_min > OPT[amt - d] + 1): # order matters, if it is None, you 
                                                                                                 #  can't compare it to cur_min
                    if OPT[amt - d] is not None:                                                                             
                        cur_min = OPT[amt - d] + 1
        OPT[amt] = cur_min


    OPT = np.inf * np.ones(target + 1)
    OPT_soln = {}
    OPT[0] = 0
    OPT_soln[0] = []
    for amt in range(1, target +1):
        for d in denominations:
            if amt -d >= 0:
                if OPT[amt] > OPT[amt - d] + 1:
                           OPT[amt] = OPT[amt - d] + 1
                           OPT_soln[amt] = OPT_soln[amt - d]+ [d]
        return OPT_soln[target]

def compute_opt_rec(target, denom):
     if target == 0:
          return 0
     
     if target < 0:
          return np.inf
    
     min_coins = np.inf
     for d in denom:
        min_coins = min(min_coins, compute_opt_rec(target - d, denom) + 1)
     return min_coins
    


```

time complexity of compute_opt:
1 + 3 + 3^2 + . . + 3^k = (3^(k+1) - 1) . . .
==> this is 3^k

for a more efficient algorithm:

```python

def compute_opt_memo(target, denom):
     if target in memo:
        return memo[target]

     if target == 0:
        memo[0] = 0
        return memo[target]
     
     if target < 0:
        memo[target] = np.inf
        return memo[target]

    
     min_coins = np.inf
     for d in denom:
        min_coins = min(min_coins, compute_opt_rec(target - d, denom) + 1)
     memo[target] = min_coins
     return memo[target]

```

