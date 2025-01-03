import heapq

def shortest_path(start, adj_list):
    pq = []

    heapq.heappush(pq, (0, start))

    dist = [float('inf')]*(len(adj_list)+1)
    dist[start] = 0

    while len(pq) != 0:
        current_w, u = heapq.heappop(pq)

        if adj_list[u] != []:
            for v, w in adj_list[u]:
                if current_w + w < dist[v]:
                    dist[v] = current_w + w

                    heapq.heappush(pq, (dist[v], v))

    return dist #distance list

input_file = open(r"Python\cse221\lab5\task1_input.txt", 'r')
output_file = open(r"Python\cse221\lab5\task1_output.txt", 'w')

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

start = int(input_file.readline().strip())

ans = shortest_path(start, adj_list)

for i in ans:
    if i != float('inf'):
        output_file.write(f"{i} ")