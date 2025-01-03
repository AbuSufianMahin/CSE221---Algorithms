input_file = open(r"Python\cse221\lab1\task1b_input.txt", 'r')
n = input_file.readline().strip()

output_file = open(r"Python\cse221\lab1\task1b_output.txt", 'w')

for i in range(int(n)):
    line_elem = input_file.readline().strip().split(" ") #list
    num1 = int(line_elem[1])
    num2 = int(line_elem[3])
    
    if line_elem[2] == '+':
        output_file.write(f"The result of {num1} + {num2} is {num1 + num2}\n") 
    elif line_elem[2] == '-':
        output_file.write(f"The result of {num1} - {num2} is {num1 - num2}\n")
    elif line_elem[2] == '*':
        output_file.write(f"The result of {num1} * {num2} is {num1 * num2}\n")
    else:
        output_file.write(f"The result of {num1} / {num2} is {num1 / num2}\n")

input_file.close()
output_file.close()