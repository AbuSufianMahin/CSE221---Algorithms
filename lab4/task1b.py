

input_file = open(r"Python\cse221\lab4\task1b_input.txt", 'r')
output_file = open(r"Python\cse221\lab4\task1b_output.txt", 'w')

n, m = list(map(int, input_file.readline().strip().split())) 

adj_list = {}

for i in range(n+1):
    adj_list[i] = None

for i in range(m):
    source, destination, weight = list(map(int, input_file.readline().strip().split())) 

    if adj_list[source] == None:
        adj_list[source] = [(destination, weight)]
    else:
        adj_list[source].append((destination, weight))

for key, val in adj_list.items():
    if val == None:
        output_file.write(f"{key} : ")
    else:
        output_file.write(f"{key} : ")
        for tup in range(len(val)):
            output_file.write(f"{val[tup]} ")

    output_file.write("\n")

input_file.close()
output_file.close()