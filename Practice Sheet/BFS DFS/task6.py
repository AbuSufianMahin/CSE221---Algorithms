def dfs_visit(graph, u, visited, result):
    if graph[u] != None:
        visited[u] = True
        result.append(u)
        for v in graph[u]:
            if visited[v] == False:
                dfs_visit(graph, v, visited, result)
            else:
                result.append(v)
                return result
    
    return 0
def DFS(graph, start):
    visited = [False] * (len(graph)+1)
    result = []

    dfs_visit(graph, start, visited, result)

    
    for u, v in graph.items():
        if visited[u] == False and v != None:
            dfs_visit(graph, u, visited, result)

    return result
#=============================DFS DONE============================#

input_file = open(r"Python\cse221\Practice Sheet\BFS DFS\input.txt", 'r')

N, M = list(map(int, input_file.readline().strip().split()))

second_line = list(map(int, input_file.readline().strip().split()))
third_line = list(map(int, input_file.readline().strip().split()))

adj_list = {}

for i in range(1, N+1):
    adj_list[i] = None

for u in range(M):
    if adj_list[second_line[u]] == None:
        adj_list[second_line[u]] = [third_line[u]]
    else:
        adj_list[second_line[u]].append(third_line[u])




print(DFS(adj_list, second_line[0]))