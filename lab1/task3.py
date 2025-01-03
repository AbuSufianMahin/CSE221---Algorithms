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

    
for i in range(len(mark_arr)):
    max_mark_index = i
    for j in range(i+1, len(mark_arr)):
        if mark_arr[max_mark_index] < mark_arr[j]:
            max_mark_index = j

    mark_arr[i], mark_arr[max_mark_index] = mark_arr[max_mark_index], mark_arr[i]
    id_arr[i], id_arr[max_mark_index] = id_arr[max_mark_index], id_arr[i]


i = 0
while i < len(id_arr)-1:
    j = i+1
    lowest_id_index = i
    while j < len(id_arr):
        if mark_arr[i] != mark_arr[j]:
            break
        elif id_arr[lowest_id_index] > id_arr[j]:
            lowest_id_index = j
        
        j += 1

    id_arr[lowest_id_index], id_arr[i] = id_arr[i], id_arr[lowest_id_index]
    i += 1

for i in range(int(n)):
    output_file.write(f"ID: {id_arr[i]} Mark: {mark_arr[i]}\n")