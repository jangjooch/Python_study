repeat = input()
rights = []
for i in range(0,int(repeat),1):

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ganet01 = (x1 - x2)**2
    ganet02 = (y1 - y2)**2
    if(x2>x1):
        ganet01 = (x2 - x1)**2
    else:
        ganet01 = (x1 - x2)**2
    if(y2>y1):
        ganet02 = (y2-y1)**2
    else:
        ganet02 = (y1 - y2)**2

    halfs = (r1 + r2)**2
    center = ganet01 + ganet02

    if(halfs > center):
        state = 2

    if(halfs == center):
        state = 1

    if(center>halfs):
        state=0

    if((center == 0) and not(r1 == r2)):
        state = 0

    if((x1 == x2) and (y1 == y2) and (r1 == r2)):
        state = -1

    rights.append(state)

for i in rights:
    print(i)