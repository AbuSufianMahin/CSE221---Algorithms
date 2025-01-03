input_file = open(r"Python\cse221\lab4\task7_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task7_output.txt", 'w')

n = int(input_file.readline().strip())

adj_list = {}

for i in range(n+1):
    adj_list[i] = None #initiation of adjacency list

for i in range(n-1):
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
    
    #population of adjacency list is done

for key, val in adj_list.items():
    if val == None:
        output_file.write(f"{key} : ")
    else:
        output_file.write(f"{key} : ")
        for tup in range(len(val)):
            output_file.write(f"{val[tup]} ")

    output_file.write("\n")

    #printed the GRAPH for satisfaction


def DFS(adj, start):
    def dfs_visit(adj_list, u, visited, result):
        visited[u] = True
        result.append(u)

        if adj_list[u] != None:
            for v in adj_list[u]:
                if visited[v] == False:
                    dfs_visit(adj_list, v, visited, result)


    visited = [False] * len(adj)
    dfs_result = []
    dfs_visit(adj_list, start, visited, dfs_result)

    for u, v in adj_list.items():
        if visited[u] == False and v != None:
            dfs_visit(adj_list, start, visited, dfs_result)
    return dfs_result

dfs1 = DFS(adj_list,5)
start_city = dfs1[-1]

dfs2 = DFS(adj_list, start_city)
end_city = dfs2[-1]

print(start_city, end_city)