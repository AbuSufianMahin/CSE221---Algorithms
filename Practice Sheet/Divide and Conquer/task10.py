
def divide_conquer(string):
    if len(string) <= 1:
        if int(string) == 1:
            return 1
        else:
            return 0
        
    mid = len(string)//2
    left_part = string[:mid]
    right_part = string[mid:]

    return divide_conquer(left_part) + divide_conquer(right_part)


print(divide_conquer('1110'))