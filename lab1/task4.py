import numpy as np

def lexicographical_order(str1, str2): #returns what comes first
    if len(str1) > len(str2):
        big_str = str1
        small_str = str2

    else:
        big_str = str2
        small_str = str1

    i = 0
    while i < len(small_str):
        if small_str[i].lower() < big_str[i].lower():
            return small_str
        elif small_str[i].lower() > big_str[i].lower():
            return big_str
        
        i += 1
    
    return small_str

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left = np.zeros(mid, dtype = list)
    right = np.zeros(len(arr)-mid, dtype = list)
    
    j = 0
    for i in range(len(arr)):
        if i < mid:
            left[i] = arr[i]
        else:
            right[j] = arr[i]
            j += 1


    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)


    return conquer_part(sorted_left, sorted_right)

def conquer_part(arr1, arr2): 
    #arr1 = [['ABCD', 'will', 'departure', 'for', 'Mymensingh', 'at', '00:30']]
    #arr2 = [['DhumketuExpress', 'will', 'departure', 'for', 'Chittagong', 'at', '02:30']]

    output_arr = np.zeros(len(arr1)+len(arr2), dtype = object)
    indx = 0

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):

        first_train = lexicographical_order(arr1[i][0], arr2[j][0])
        
        if first_train == arr1[i][0]:
            output_arr[indx] = arr1[i]
            indx += 1
            i += 1
        else:
            output_arr[indx] = arr2[j]
            indx += 1
            j += 1

        

        while i < len(arr1):
            output_arr[indx] = arr1[i]
            indx += 1
            i += 1

        while j < len(arr2):
            output_arr[indx] = arr2[j]
            indx += 1
            j += 1

    return output_arr


input_file = open(r"Python\cse221\lab1\task4_input.txt", 'r')
output_file = open(r"Python\cse221\lab1\task4_output.txt", 'w')

n = int(input_file.readline().strip())

schedule = np.zeros(n, dtype = list)

for i in range(n):
    schedule[i] = input_file.readline().strip().split()


print(merge_sort(schedule))