def OPT(denominations, value):
    global mem
    if value <= 0:
        return -1
    
    else:
        for num in range(len(denominations)):
            if denominations[num] > value:
                break
        options = [0]*num
        for index in range(num):
            if denominations[index] > value:
                break
            if value-denominations[index] in mem:
                return mem[value-denominations[index]]
            else:
                mem[value-denominations[index]] = 1 + OPT(denominations, value-denominations[index])
                options[index] = mem[value-denominations[index]]
                        
        return min(options)

# fixed denominations
def FOPT(value):
    if value <= 0:
        return 0
    else:
        return min(1 + FOPT(value-1), 1 + FOPT(value-4), 1 + FOPT(value-5))
    
def OPT_change(v, denom):
    OPT = [0]*(v+1)
    for v in range(1, v+1):
        cur_min = int(v/min(denom)) + 1
        for i in range(len(denom)):
            if denom[i]>v:
                continue
            if cur_min > 1 + OPT[v-denom[i]]:
                cur_min = 1 + OPT[v-denom[i]]

        OPT[v] = cur_min
    return OPT

def make_change(amount, denom):
    OPT = OPT_change(amount, denom)
    change = []
    denom_sorted = sorted(denom, reverse = True)
    while amount > 0:
        for d in denom_sorted:
            changed = False
            if amount >= d:
                if OPT[amount] == 1 + OPT[amount-d]:
                    change += [d]
                    amount -= d
                    changed = True
                    break
    if not changed:
        return "not possible"
    return change

        

if __name__ == '__main__':
    mem = {}
    print(OPT_change(8, [1,4,5]))
    print(OPT_change(10, [1,4,5]))
    print(make_change(8, [1,4,5]))
    print(make_change(16, [1,4,5]))
    print(make_change(20, [1,4,5]))
    print(make_change(4, [1,4,5]))
    print(make_change(42, [1,3,19,20]))

    
