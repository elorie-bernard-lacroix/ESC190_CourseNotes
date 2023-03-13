class Node: 
    def __str__(self):
        return f"value of node: {self.value}" # crash because you called value before you made it an attribute 

    def __init__(self, value): 
        print("self")
        self.value = value 
        self.next = None 
        print("I loved the ESC190 midterm") # doesnt have to be something true 

class LinkedList:
    def __init__(self):
        self.head = None

    def get_tail(self):
        '''Return the tail of the list'''
        current = self.head
        while current.next:
            current = current.next
        return current

    def get_node_at_index(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            tail = self.get_tail()
            tail.next = Node(value)
    def insert(self, value, index):
        '''Insert a node with value at index'''
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            # slef.head, new_node.next = new_node, self.head
        else:
            prev = self.get_node_at_index(index - 1)
            new_node = Node(value)
            new_node.next = prev.next
            prev.next = new_node

    def __str__(self):
        current = self.head
        output = []
        while current:
            output.append(current value)
        return str(output)

            
if __name__ == '__main__':
    LL = LinkedList()
    LL.append(4)
    LL.append(10)
    LL.append(12)

    print(LL)
    n1 = Node(42)  # void create_node1(node **p_n, int_value);
            # node *n1; create_node1(&n1, 42);
            # node *create_node2(int values);
            # node *n2 = create_node2(42);
            # node *n2 = create_node2(42);

    a = 5000
    b = a    #








# class Student: 
#     def __init__(self, name, age): 
#         self.name = name
#         self.age = age

#     def __str__(self): 
#         return f"Name (self.name), age: {self.age}" 

# if __name__ =='__main__': 
#     s = Student("Bob", 19)
#     #s.name : "Bob" 
#     #s.age: 19 
#     #s.age = 20
#     print("hi")

# s.__str_() is the same as Student.__str__(s)
