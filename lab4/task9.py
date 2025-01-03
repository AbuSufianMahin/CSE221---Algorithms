input_file = open(r"Python\cse221\lab4\task9_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task9_output.txt", 'w')

N, M = list(map(int, input_file.readline().strip().split()))

adj_list = {}

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

def DFS_topological_sort(graph, source):
    
    def dfs(source, visited, dfs_result):
        if visited[source] == -1:  #visiting, cycle detected
            return False
        if visited[source] == 1: #fully explored
            return True
        
        visited[source] = -1  #vising

        if graph[source] != None:
            for neighbor in graph[source]:
                if dfs(neighbor, visited, dfs_result) == False:  
                    return False        #cylce detected
            
        visited[source] = 1 #explored
        dfs_result.append(source)


    visited = [0]* len(graph)  # 0 = not visited, -1 = visiting, 1 = explored
    dfs_result = []

            
    for i in range(1, len(adj_list)):
        if adj_list[i] != None and visited[i] == 0:
            if dfs(i, visited, dfs_result) == False:
                return "IMPOSSIBLE"


    return dfs_result[::-1]        
            

print(DFS_topological_sort(adj_list, start))
        
#BFS 