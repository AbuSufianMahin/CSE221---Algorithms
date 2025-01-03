input_file = open(r"Python\cse221\Practice Sheet\sorting\input.txt", 'r')


N = int(input_file.readline().strip())
arr = input_file.readline().strip().split()

letter = []
arr_int = []

for i in range(N):
    if 48 <= ord(arr[i][0]) <= 57:
        arr_int.append(int(arr[i]))
    else:
        letter.append(arr[i])


for i in range(len(arr_int)):
    min_indx = i
    for j in range(i+1, len(arr_int)):
        if arr_int[min_indx] > arr_int[j]:
            min_indx = j
    
    if min_indx != i:
        arr_int[min_indx], arr_int[i] = arr_int[i], arr_int[min_indx]

output = arr_int + letter

print(output)