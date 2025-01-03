input_file = open(r"Python\cse221\lab1\task1a_input.txt", 'r')
numOfLines = input_file.readline().strip()

output_file = open(r"Python\cse221\lab1\task1a_output.txt", 'w')

for i in range(int(numOfLines)):
    num = input_file.readline().strip() #strip removing \n
    
    if int(num)%2 == 0:
        output_file.write(f"{num} is an Even number.\n")
        #print(f"{num} is an Even number.")
    else:
        output_file.write(f"{num} is an Odd number.\n")
        #print(f"{num} is an Odd number")

input_file.close()
output_file.close()