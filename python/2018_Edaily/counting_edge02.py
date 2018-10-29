

init = input()
init = int(init)
array = list()
sum = int(0)
contents = int(1)
for i in range(init):
    for j in range(init):
        array.append(contents)
        contents = contents + 1
print(array)
for i in range(init):
    array.remove(i+1)
print(array)
for i in range(init):
    max = array[-1]
    array.remove(max)
print(array)
idx = int(0)
