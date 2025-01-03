input_file = open(r"Python\cse221\lab4\task2_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task2_output.txt", 'w')

N, M = list(map(int, input_file.readline().strip().split()))

adj_list = {}  #undirected + unweighted

for i in range(N+1):
    adj_list[i] = None

for i in range(M):
    u, v = list(map(int, input_file.readline().strip().split()))
    if i == 0:
        start = u
        
    if adj_list[u] == None:
        adj_list[u] = [v]
    else:
        adj_list[u].append(v)

    if adj_list[v] == None:
        adj_list[v] = [u]
    else:
        adj_list[v].append(u)

output_file.write(f"============GRAPH==============\n")
print(adj_list)

for key, value in adj_list.items():
    if value == None:
        output_file.write(f"{key}: \n")
    else:
        output_file.write(f"{key}: {value}\n")

#bfs 

visited = [False] * (N+1)

serial = [start]
visited[start] = True
bfs_result = []

while len(serial) != 0:
    u = serial.pop(0)
    bfs_result.append(u)

    if adj_list[u] != None:
        for v in adj_list[u]:
            if visited[v] == False:
                visited[v] = True
                serial.append(v)

output_file.write(f"BFS RESULT: \n")
for i in bfs_result:
    output_file.write(f"{i} ")


#dfs
def dfs_visit(adj_list, u, visited, result):
    visited[u] = True
    result.append(u)

    if adj_list[u] != None:
        for v in adj_list[u]:
            if visited[v] == False:
                dfs_visit(adj_list, v, visited, result)


visited = [False] * (N+1)
dfs_result = []
start = 5
dfs_visit(adj_list, start, visited, dfs_result)

for u, v in adj_list.items():
    if visited[u] == False and v != None:
        dfs_visit(adj_list, start, visited, dfs_result)

print(dfs_result)


input_file.close()
output_file.close()
