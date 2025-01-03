class MinHeap:
    def __init__(self):
        self.heap = []  # Heap as (distance, vertex) pairs
        self.size = 0

    def insert(self, key):
        self.heap.append(key)
        self.swim(self.size)
        self.size += 1

    def swim(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent][0] > self.heap[index][0]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def remove(self):
        if self.size == 0:
            return None  # Empty heap

        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]  # Replace root with last element
        self.heap.pop()
        self.size -= 1
        self.min_heapify(0)

        return min_value

    def min_heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

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
        return self.heap[0] if self.size > 0 else None

    def isEmpty(self):
        return self.size == 0

# Reading input and constructing the graph
input_file = open(r"Python\cse221\lab4\task5_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task5_output.txt", 'w')

N, M, D = list(map(int, input_file.readline().strip().split()))

adj_list = {i: [] for i in range(N + 1)}

for _ in range(M):
    u, v = list(map(int, input_file.readline().strip().split()))
    adj_list[u].append((v, 1))  # Assuming weight is 1 as per provided code

# Writing adjacency list to output file
for key, val in adj_list.items():
    output_file.write(f"{key} : {' '.join(map(str, val))}\n")

print("============ Graph Construction Done ===============")

def dijkstra(adj_list, source):
    distance = [float('inf')] * (len(adj_list))
    parent = [None] * (len(adj_list))
    priority_Q = MinHeap()

    distance[source] = 0
    priority_Q.insert((0, source))

    while not priority_Q.isEmpty():
        current_distance, current_node = priority_Q.remove()

        # If the distance is outdated, skip processing
        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in adj_list[current_node]:
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current_node
                priority_Q.insert((new_distance, neighbor))

    return distance, parent

# Run Dijkstra's algorithm from source node 1
distances, parents = dijkstra(adj_list, 1)
print(distances)
print(parents)
# Write distances to output file
output_file.write("\nDistances from source:\n")
for node in range(1, N + 1):
    output_file.write(f"Node {node}: {distances[node]}\n")

input_file.close()
output_file.close()
print("============ Dijkstra's Algorithm Completed ===============")

input_file.close()
output_file.close()