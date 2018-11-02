
routin = input()
routin = int(routin)
contents = list()
storage = list()
counting = list()
for i in range(routin):
    typing = input()
    storage.insert(i,typing)
for i in range(routin):
    contents.append(storage[i].split(' '))

for i in range(routin):
    Wcount = int(0)
    for j in range(routin):
        if contents[i][j] == 'W':
            Wcount=Wcount+1
    if Wcount>1:
        for h in range(routin):
            if contents[i][h] == 'B':
                contents[i][h] = 'W'
            else:
                contents[i][h] = 'B'
print(contents)