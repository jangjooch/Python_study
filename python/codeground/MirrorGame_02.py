
routin = int(input())

for i in range(routin):
    inputsize = int(input())
    borad = [[int(x) for x in input().split()]for y in range(inputsize)]
    # 2 차원 리스트형 입력받고 int형으로 바꾸기
    numbering = int(0)
    mapping = []
    for i in range(inputsize):
        inside = []
        for j in range(inputsize):
            inside.append(numbering)
            numbering = numbering +1
        mapping.append(inside)
    print(mapping)
    #위치 저장 기준이 될 map 생성
    start = int(0)
    xlocate = int(0)
    ylocate = int(0)
    road = []
    state = "a"
    #road.append(mapping[xlocate][ylocate])
    while xlocate<inputsize and xlocate>-1 and ylocate<inputsize and ylocate>-1:
        '''
        각 상태에 따라 X축과 Y축을 변경토록한다.
        예로 +x형태의 움직임은 형태2의 거울과 만나면  +y방향으로 움직인다.
        그렇기에 borad상에서는 x의 값이 증가한다
        그래서 나는 움직이는 방향에 따른 상태를 a,b,c,d라 칭하고 이에따른
        어떠한 형태의 거울을 만나는지에 따라 좌표에 변화를 주었다.
        '''
        mirror = borad[xlocate][ylocate]
        if state =="a":
            if mirror==0:
                ylocate=ylocate+1
            elif mirror==1:
                road.append(mapping[xlocate][ylocate])
                xlocate=xlocate-1
                state="d"
            elif mirror==2:
                road.append(mapping[xlocate][ylocate])
                xlocate=xlocate+1
                state="c"
        elif state == "b":
            if mirror==0:
                ylocate=ylocate-1
            elif mirror==1:
                road.append(mapping[xlocate][ylocate])
                xlocate=xlocate+1
                state="c"
            elif mirror==2:
                road.append(mapping[xlocate][ylocate])
                xlocate=xlocate-1
                state="d"
        elif state == "c":
            if mirror == 0:
                xlocate=xlocate+1
            elif mirror == 1:
                road.append(mapping[xlocate][ylocate])
                ylocate=ylocate-1
                state="b"
            elif mirror == 2:
                road.append(mapping[xlocate][ylocate])
                ylocate=ylocate+1
                state="a"
        elif state == "d":
            if mirror == 0:
                xlocate=xlocate-1
            elif mirror == 1:
                road.append(mapping[xlocate][ylocate])
                ylocate=ylocate+1
                state="a"
            elif mirror == 2:
                road.append(mapping[xlocate][ylocate])
                ylocate=ylocate-1
                state="b"
    print("number of reflected : %d" % (len(road)))