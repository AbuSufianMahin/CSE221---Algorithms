class MinHeap:
    def __init__(self):
        self.heap = []  # tup = (distance, vertex) pair
        self.size = 0
        
    def insert(self, key):
        self.heap.append(key) # have to insert key as (distance, node)
        self.swim(self.size)

        self.size += 1

    def swim(self, index):
        if index <= 0:  
            return 
        
        parent = index // 2 

        if self.heap[parent][0] > self.heap[index][0]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.swim(parent)

    def remove(self):
        if self.size == 0:
            return None 
        
        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size-1]  # Last element
        self.heap.pop()
        self.size -= 1
        self.min_heapify(0)
        
        return min_value  #its a tuple
    
    def min_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < self.size and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.min_heapify(smallest)

    def display_heap(self):
        return self.heap
    
    def get_min(self):
        if self.size == 0:
            return None
        return self.heap[0]

    def isEmpty(self):
        return self.size == 0

input_file = open(r"Python\cse221\lab4\task5_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task5_output.txt", 'w')

N, M, D = list(map(int, input_file.readline().strip().split()))

adj_list = {}
for i in range(N+1):
    adj_list[i] = None

for i in range(M):
    u, v = list(map(int, input_file.readline().strip().split()))

    #start is always 1
    if adj_list[u] == None:
        adj_list[u] = [(v, 1)]
    else:
        adj_list[u].append((v, 1))

print("============ Graph Construction Done ===============")

def dijkstra(graph, source):
    distance = [float('inf')] * (len(graph))
    parent = [None] * (len(graph))
    priority_Q = MinHeap()

    for i in graph:
        if i != source:
            priority_Q.insert((float('inf'), source))

    distance[source] = 0
    priority_Q.insert((0, source))
    
    while priority_Q.isEmpty() == False:
        current_distance, current_node = priority_Q.remove()

        if current_distance > distance[current_node]:
            continue

        if graph[current_node] != None:
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight 

                if new_distance < distance[neighbor]:
                    parent[neighbor] = current_node
                    distance[neighbor] = new_distance
                    priority_Q.insert((new_distance, neighbor))

    return distance, parent

distance, parent = dijkstra(adj_list, 1)

output_file.write(f"Time : {distance[D]}\n")
reverse_path = [D]

i = D
while parent[i] != None:
    reverse_path.append(parent[i])
    i = parent[i]

output_file.write("Shortest path: ")
for i in range(len(reverse_path)-1, -1, -1):
    if i == 0:
        output_file.write(f"{reverse_path[i]}\n")

    else:
        output_file.write(f"{reverse_path[i]} --> ")

input_file.close()
output_file.close()
