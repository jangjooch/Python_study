nums = [int(x) for x in input().split()]
#1차원 int형으로 리스트 생성 및 입력
nums.sort()
#크기순으로 정렬
if nums.count(0)>0:
    nums.remove(0)
#0제거.
underz = filter(lambda x:x<0,nums)
upprtz = [x for x in nums if x>0]
sum01 = 1
sum02 = 1
selected01=[]
selected02=[]
counting01 = lambda x,y:x*y,selected01
counting02 = lambda x,y:x*y,selected02
if len(nums)>2:
    for i in range(3):
        if i <2:
            selected01.append(nums[i])
        else:
            selected01.append(nums[-1])
        selected02.append(nums[len(nums)-1-i])
else:
    for i in range(2):
        selected02.append(nums[len(nums)-1-i])
        selected01.append(nums[i])
print(counting02)
print(counting01)