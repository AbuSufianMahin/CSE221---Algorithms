input_file = open(r"Python\cse221\Practice Sheet\Divide and Conquer\input.txt", 'r')
x = int(input_file.readline().strip())
input_arr = list(map(int, input_file.readline().strip().split()))


def binary_even_search(arr):
    found = False

    low = 0 
    high = len(input_arr)-1
    while low <= high:
        mid = (low+high)//2

        if input_arr[mid]%2 == 0:
            found = True
            first_even = mid #index
            high = mid-1
             
        else:
            low = mid + 1

    if found:
        return first_even
    else:
        return None
    

if binary_even_search(input_arr) == None:
    even_count = 0
else:
    even_count = len(input_arr) - binary_even_search(input_arr)

odd_count = len(input_arr) - even_count

print(odd_count, even_count)