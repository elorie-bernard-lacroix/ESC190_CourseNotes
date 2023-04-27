class Graph:
    def __init__(self, capacity):
        self.capacity = capacity # The maximum number of nodes
        self.cur_num_nodes = 0 # The current number of nodes
        self.nodes = [] # The list of nodes
        self.indices = {} # A dictionary mapping node names to indices
        self.adj_array = [] # The adjacency array

        # Initialize the adjacency array
        for i in range(self.capacity):
            self.adj_array.append([None] * self.capacity)

    def expand(self):
        '''
        Expand the graph by doubling the capacity.
        '''
        adj_array_new = []
        self.capacity *= 2
        
        # Create a new adjacency array
        for i in range(self.capacity):
            adj_array_new.append([None] * self.capacity)

        # Copy the old adjacency array into the new one
        for i in range(self.cur_num_nodes):
            for j in range(self.cur_num_nodes):
                adj_array_new[i][j] = self.adj_array[i][j]

        self.adj_array = adj_array_new

    def register_node(self, name):
        '''
        Register a new node in the graph.
        '''

        # If the graph is full, expand it
        if self.capacity == self.cur_num_nodes:
            self.expand()

        # Add the node to the graph
        self.nodes.append(name)

        # Add the node to the adjacency array
        self.indices[name] = self.cur_num_nodes

        # Increment the number of nodes
        self.cur_num_nodes += 1

        # Initialize the new row and column
        for i in range(self.cur_num_nodes):
            self.adj_array[i][self.cur_num_nodes-1] = 0
            self.adj_array[self.cur_num_nodes-1][i] = 0
        
    def connect_by_name(self, name1, name2):
        '''
        Connect two nodes in the graph by name.
        '''

        # If either node is not in the graph, add it
        if name1 not in self.indices:
            self.register_node(name1)
        if name2 not in self.indices:
            self.register_node(name2)
        
        # Connect the nodes
        self.connect_by_index(self.indices[name1], self.indices[name2])
        
    def connect_by_index(self, index1, index2):
        '''
        Connect two nodes in the graph by index.
        '''
        self.adj_array[index1][index2] = 1


if __name__ == "__main__":
    node