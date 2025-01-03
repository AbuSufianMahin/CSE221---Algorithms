def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    i = 0
    j = 0
    merged_list = []

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged_list.append(left_sorted[i])
            i += 1
        else:
            merged_list.append(right_sorted[j]) 
            j += 1

    
    while i < len(left_sorted):
        merged_list.append(left_arr[i])
        i += 1       
    while j < len(right_sorted):
        merged_list.append(right_sorted[j])
        j += 1

    return merged_list

input_file = open(r"Python\cse221\Practice Sheet\Divide and Conquer\input.txt", 'r')
x = int(input_file.readline().strip())

input_arr = list(map(int, input_file.readline().strip().split()))

element = []
zeros = []

for i in input_arr:
    if i == 0:
        zeros.append(i)
    else:
        element.append(i)
print(element)
result = merge_sort(element) + zeros

print(result)

