input_file = open(r"Python\cse221\Practice Sheet\Divide and Conquer\input.txt", 'r')
x = int(input_file.readline().strip())
input_arr = list(map(int, input_file.readline().strip().split()))

max_combo = 0
indx1 = -1
indx2 = -1
for i in range(x):
    for j in range(i+1, x):
        iteration = input_arr[i] ** 2 + input_arr[j] **3
        if iteration > max_combo:
            indx1 = i
            indx2 = j
            max_combo = iteration
print(indx1, indx2)
