def BFS(graph, value, start):
    visited = [False] * (len(graph)+1)

    serial = [start]
    visited[start] = True

    #result = []

    amount = [0] * (len(graph)+1)
    amount[start] = value[start]

    while serial:
        u = serial.pop(0)
        #result.append(u)

        if graph[u] != None:
            for v in graph[u]:
                if visited[v] == False:
                    visited[v] = True
                    serial.append(v)
                    amount[v] = amount[u] + value[v]
    return amount

input_file = open(r"Python\cse221\Practice Sheet\BFS DFS\input.txt", 'r')

N, M = list(map(int, input_file.readline().strip().split()))
gold = [None] + list(map(int, input_file.readline().strip().split()))

adj_list = {}

for i in range(1, N+1):
    adj_list[i] = None

for i in range(M):
    u, v = list(map(int, input_file.readline().strip().split()))

    if adj_list[u] == None:
        adj_list[u] = [v]
    else:
        adj_list[u].append(v)

    if adj_list[v] == None:
        adj_list[v] = [u]
    else:
        adj_list[v].append(u)


output = BFS(adj_list, gold, 1)
max_gold = 0

for i in output:
    if i > max_gold:
        max_gold = i

print(max_gold)