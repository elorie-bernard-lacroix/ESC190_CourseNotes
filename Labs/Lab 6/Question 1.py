import queue
import Queue

if __name__ == '__main__':
    s = queue.Queue()
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
