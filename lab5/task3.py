import heapq

def least_danger(start, destination, adj_list):
    pq = []
    dist = [float('inf')] * (len(adj_list)+1)

    heapq.heappush(pq, (0, start))
    dist[start] = 0
    
    while pq:

        current_max_danger, u = heapq.heappop(pq)
        if u == destination:
            return current_max_danger
        
        for v, w in adj_list[u]:
            
            new_max_danger = max(current_max_danger, w)

            if dist[v] > new_max_danger:
                dist[v] = new_max_danger
                heapq.heappush(pq, (new_max_danger, v))

    return -1

input_file = open(r"Python\cse221\lab5\task3_input.txt", 'r')
output_file = open(r"Python\cse221\lab5\task3_output.txt", 'w')

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

path = least_danger(1, n, adj_list)

print(path)