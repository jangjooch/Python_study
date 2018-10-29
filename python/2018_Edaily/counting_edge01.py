

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
maxidx = len(array)-1
storage = list()
for i in range((init*2)):
    if i<init :
        storage.append(array[i])
        array.remove(i)
    else:
        storage.append(array[maxidx])
        array.remove(maxidx)
        maxidx = maxidx - 1
print(storage)
print(array)