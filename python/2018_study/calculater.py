
line = input("type what you want to calculate :")
numbers = []
tools = ''
line = line.split(' ')
print(line)
result = 0
i = 0
for i in range(0,len(line)-1,1):
    if i == 1:
        if line[i] == '+':
            result = int(line[0]) + int(line[2])
        elif line[i] == '-':
            result = int(line[0]) - int(line[2])
        elif line[i] == '/':
            result = int(line[0]) / int(line[2])
        elif line[i] == '*':
            result = int(line[0]) * int(line[2])
    else:
        if line[i] == '+':
            result = result + int(line[i+1])
        elif line[i] == '-':
            result = result - int(line[i+1])
        elif line[i] == '/':
            result = result / int(line[i+1])
        elif line[i] == '*':
            result = result * int(line[i+1])


print("result = {0}".format(result))