def bubbleSort(arr):   
    best_case = True
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                best_case = False

        if best_case == True:
            return arr

    return arr

input_file = open(r"Python\cse221\lab1\task2_input.txt", 'r')
output_file = open(r"Python\cse221\lab1\task2_output.txt", 'w')
    
n = int(input_file.readline().strip())
#print(n)
input_arr = input_file.readline().strip().split(" ")
for i in range(n):
    input_arr[i] = int(input_arr[i])

sorted_arr = bubbleSort(input_arr)

for i in range(len(sorted_arr)):
    output_file.write(f"{sorted_arr[i]} ")