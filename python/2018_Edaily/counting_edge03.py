
init = input()
init = int(init)
array = list()
sum = int(0)
contents = int(1)
for i in range(init):
    for j in range(init):
        array.append(contents)
        contents = contents + 1
for i in range(init):
    array.remove(i+1)
for i in range(init):
    max = array[-1]
    array.remove(max)
del array[0]
del array[-1]
idx = int(0)
exclusive = int(init - 2)
for i in range(len(array)):
    if(idx<exclusive):
        idx = idx + 1
    elif (idx==(exclusive+2)):
        idx = 1
    elif (idx>=exclusive):
        array[i] = 0
        idx = idx +1
for i in range(len(array)):
    sum = sum + array[i]

init = init * init
ori = int((init*(init+1))/2)
print(ori - sum)