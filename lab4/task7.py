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


def dfs_farthest_node(adj, start):
    visited = [False] * len(adj)
    
    visited[start] = True
    farthest_node = start
    max_distance = 0

    stack = [(start, 0)]  # Stack stores (node, distance)

    while stack:
        node, dist = stack.pop()

        if dist > max_distance:
            max_distance = dist
            farthest_node = node

        for neighbor in adj[node]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                stack.append((neighbor, dist + 1))

    return farthest_node

starting = dfs_farthest_node(adj_list, start)
ending = dfs_farthest_node(adj_list, starting)
print(starting, ending)

input_file.close()
output_file.close()