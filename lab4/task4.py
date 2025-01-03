input_file = open(r"Python\cse221\lab4\task4_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task4_output.txt", 'w')

N, M = list(map(int, input_file.readline().strip().split()))

adj_list = {}  #directed + unweighted

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

#cycle detection using DFS

def dfs_visit(adj_list, u, visited):
    visited[u] = True
    #result is not needed

    if adj_list[u] != None:
        for v in adj_list[u]:
            if visited[v] == False:
                dfs_visit(adj_list, v, visited)
            else:
                return True
    return False 


visited = [False] * (N+1)

cycle = dfs_visit(adj_list, start, visited)

if cycle:
    output_file.write("YES")
else:
    output_file.write("NO")


input_file.close()
output_file.close()