class Queue:
    def __init__(self):
        self.data = [None]*6
        self.begin = 0
        self.end = -1

    def enqueue(self, item):
        
        if self.end == 5:
            self.data[0] = item
            self.end = 0
            
        else:
            self.data[self.end+1] = item
            self.end = self.end + 1   # O(n) worst-case, usually O(1)

    def dequeue(self):
        # return self.data.pop()
        ret_val = self.data[self.begin]
        self.data[self.begin] = None # O(n), because need to move self.data[1:] to self.data[0:]
        self.begin = self.begin + 1
        return ret_val
    
    def __str__(self):
        ret_val = str(self.data[self.begin])
        i = self.begin + 1
        while i != self.end:
            ret_val += "; "
            ret_val += str(self.data[i])
            i = (i+1)%6

        return ret_val
    
    def __lt__(self, other):
        
        for i in range(0,5,1):
            if self.data[self.begin+i] < other.data[other.begin+i]:
                return True
            elif self.data[self.begin+i] > other.data[other.begin+i]:
                return False
            
        return True  # they are equal


    

if __name__ == '__main__':

    # Question 1
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(3)
    s.enqueue(3)
    s.enqueue(3)
    print(s.dequeue())
    print(s.dequeue())
    
    s.enqueue(4)
    s.enqueue(5)
    print(s.dequeue())

    # Question 2
    s1 = Queue()
    s1.enqueue(8)

    s2 = Queue()
    s2.enqueue(3)
    s2.enqueue(8)

    print(s1.__lt__(s1))
    

