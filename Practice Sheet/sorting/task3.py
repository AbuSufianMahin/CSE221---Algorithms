input_file = open(r"Python\cse221\Practice Sheet\sorting\input.txt", 'r')


N = int(input_file.readline().strip())
arr = list(map(int, input_file.readline().strip().split()))

brr = []
j = N-1

for i in range(N):
    first = arr[0]
    last = arr[len(arr)-1]

    if first < last: 
        brr.append(first)
        arr.pop(0)
        
    else:
        brr.append(last)
        arr.pop(len(arr)-1)
    
    j -= 1

print(brr)
print("=============TASK3 ANSWER==============")
sorted = True
for i in range(len(brr)-1):
    if brr[i] > brr[i+1]:
        sorted = False
        break

if sorted:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")