import numpy as np

input_file = open(r"Python\cse221\lab1\task3_input.txt", 'r')
output_file = open(r"Python\cse221\lab1\task3_output.txt", 'w')

n = input_file.readline().strip()
first_line = input_file.readline().strip().split()
second_line = input_file.readline().strip().split()

id_arr = np.zeros(int(n), dtype = int)
mark_arr = np.zeros(int(n), dtype = int)

for i in range(int(n)):
    id_arr[i] = int(first_line[i])
    mark_arr[i] = int(second_line[i])


for i in range(int(n)):
    temp = i
    for j in range(i+1, int(n)):
        if mark_arr[temp] < mark_arr[j]:
            temp = j 
        elif mark_arr[temp] == mark_arr[j]:
            if id_arr[j] < id_arr[temp]:
                temp = j

    mark_arr[temp], mark_arr[i] = mark_arr[i], mark_arr[temp]
    id_arr[temp], id_arr[i] = id_arr[i], id_arr[temp]

for i in range(int(n)):
    output_file.write(f"ID: {id_arr[i]} Mark: {mark_arr[i]}\n")