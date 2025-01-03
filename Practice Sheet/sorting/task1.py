input_file = open(r"Python\cse221\Practice Sheet\sorting\input.txt", 'r')

N = int(input_file.readline().strip())
arr = list(map(int, input_file.readline().strip().split()))

swap_count = 0
for i in range(len(arr)):
    min_indx = i
    for j in range(i+1, len(arr)):
        if arr[min_indx] > arr[j]:
            min_indx = j
    
    if min_indx != i:
        swap_count += 1
        arr[min_indx], arr[i] = arr[i], arr[min_indx]


print(arr)
print(swap_count)
            