import numpy as np

input_file = open(r"Python\cse221\lab4\task1a_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task1a_output.txt", 'w')

n, m = list(map(int, input_file.readline().strip().split())) #string

adj_matrix = np.zeros((n+1,n+1), dtype = int)

for i in range(m):
    source, destination, weight = list(map(int, input_file.readline().strip().split()))
    adj_matrix[source][destination] = weight

for i in range(n+1):
    for j in range(n+1):
        output_file.write(f"{adj_matrix[i][j]} ")

    output_file.write("\n")

input_file.close()
output_file.close()