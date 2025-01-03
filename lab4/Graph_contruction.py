class Graph:
    def __init__(self, vertex_count = 0, undirected = False):
        self.adjacency_list = {}
        self.undirected = undirected  #self interest#haven't implemented yet

        for i in range(vertex_count+1):
            self.adjacency_list[i] = None


    def add_node(self, s, d, w = 1): #source, destination, weight
        if self.adjacency_list[s] == None:
            self.adjacency_list[s] = [(d, w)]
        else:
            self.adjacency_list[s].append((d, w))

        if self.undirected == True:         #self interest#
            if self.adjacency_list[d] == None:
                self.adjacency_list[d] = [(s, w)]
            else:
                self.adjacency_list[d].append((s, w))
        
            

    def display_graph(self):
        result = f""
        for key, val in self.adjacency_list.items():
            if val == None:
                result += f"{key} : "
            else:
                result += f"{key} : "
                for tup in range(len(val)):
                    result += f"{val[tup]} "
            
            result += "\n"

        return result
    

    def bfs(self, start):
        visited = [False] * (len(self.adjacency_list)+1)

        serial = [start]
        visited[start] = True
        result = []

        while serial:
            u = serial.pop(0)
            result.append(u)

            if self.adjacency_list[u]!= None:   #why it is valid? 
                # when there is no adj nodes! the value will be none, then this if condition is needed!
                for tup in self.adjacency_list[u]:
                    if visited[tup[0]] == False:
                        visited[tup[0]] = True
                        serial.append(tup[0])
            
        return result 


    def dfs(self, start):
        visited = [False] * (len(self.adjacency_list))
        result = []
        
        self.dfs_visit(start, visited, result)

        for key, value in self.adjacency_list.items():
                #skipping the values that deosn't have adj nodes
            if value != None and visited[key] == False:
                self.dfs_visit(key, visited, result)
            

        return result
    
    def dfs_visit(self, u, visited, result):
        visited[u] = True
        result.append(u)
        
        if self.adjacency_list[u] != None:
            # when there is no adj nodes! the value will be none, then this if condition is needed!
            for tup in self.adjacency_list[u]:
                if visited[tup[0]] == False:
                    self.dfs_visit(tup[0], visited, result)



input_file = open(r"Python\cse221\lab4\Graph_construction_inp.txt", 'r')
n, m = list(map(int, input_file.readline().strip().split())) 

graph1 = Graph(n, undirected = True)
bfs_start = None
for i in range(m):
    node1, node2 = list(map(int, input_file.readline().strip().split()))
    if i == 0:
        bfs_start = node1
    graph1.add_node(node1, node2)


print("==============GRAPH==============")
print(graph1.display_graph())

print("==============BFS==============")
print(graph1.bfs(bfs_start))

print("==============DFS==============")
print(graph1.dfs(bfs_start)) 
