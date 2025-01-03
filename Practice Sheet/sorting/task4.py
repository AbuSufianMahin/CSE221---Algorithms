input_file = open(r"Python\cse221\Practice Sheet\sorting\input.txt", 'r')


N = int(input_file.readline().strip())
arr = list(map(int, input_file.readline().strip().split()))


for i in range(N):
    min_indx = i

    for j in range(i+1, N):
        if arr[min_indx] > arr[j]:
            if min_indx%2 == j%2:
                min_indx = j

    arr[min_indx], arr[i] = arr[i], arr[min_indx]

print(arr)

print("=============TASK4 ANSWER==============")
sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted = False
        break

if sorted:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")