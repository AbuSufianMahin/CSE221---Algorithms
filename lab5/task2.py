import heapq

def shortest_path(start, adj_list):
    pq = []

    heapq.heappush(pq, (0, start))

    dist = [float('inf')]*(len(adj_list)+1)
    dist[start] = 0

    while len(pq) != 0:
        current_w, u = heapq.heappop(pq)

        
        for v, w in adj_list[u]:
            if current_w + w < dist[v]:
                dist[v] = current_w + w

                heapq.heappush(pq, (dist[v], v))

    return dist #distance list

input_file = open(r"Python\cse221\lab5\task2_input.txt", 'r')
output_file = open(r"Python\cse221\lab5\task2_output.txt", 'w')

n, m = list(map(int, input_file.readline().strip().split()))

adj_list = {}

for i in range(1, n+1):
    adj_list[i] = []

for i in range(m):
    u, v, w = list(map(int, input_file.readline().strip().split()))

    if adj_list[u] == None:
        adj_list[u] = [(v, w)]
    else:
        adj_list[u].append((v, w))

#same as task1 upto this part

alice_start, bob_start = list(map(int, input_file.readline().strip().split()))

alice_path = shortest_path(alice_start, adj_list)
bob_path = shortest_path(bob_start, adj_list)

print(alice_path)
print(bob_path)

time = float('inf')
node = None
for i in range(len(alice_path)):
    if alice_path[i] != float('inf') and bob_path[i] != float('inf'): #got a pair
        pair_max = 0
        if alice_path[i] > bob_path[i]:
            pair_max = alice_path[i]
        else:
            pair_max = bob_path[i]

        if pair_max < time:
            time = pair_max
            node = i

if node == None:
    output_file.write("Impossible")
else:
    output_file.write(f"time: {time}\n")
    output_file.write(f"Node: {node}")
