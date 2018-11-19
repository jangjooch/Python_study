nums = [int(x) for x in input().split()]
#1차원 int형으로 리스트 생성 및 입력
nums.sort()
#크기순으로 정렬
sum01 = 1
sum02 = 1
if len(nums)-nums.count(0)<2:
    sum01 = 0
    sum02 = 0
elif nums.count(0)>0:
    nums.remove(0)
#0제거.

if len(nums)>2:
    for i in range(3):
        if i <2:
            sum01 = nums[i] * sum01
        else:
            sum01 = nums[-1] * sum01
        sum02 = sum02 * nums[len(nums)-i-1]
    if sum01<0 and sum02<0:
        sum01=1
        sum02=1
        for i in range(2):
            sum01 = sum01 * nums[i]
            sum02 = sum02 * nums[len(nums) - i - 1]
else:
    for i in range(2):
        sum01 = sum01 * nums[i]
        sum02 = sum02 * nums[len(nums)-i-1]
if sum01>sum02:
    print(sum01)
elif sum01<0 and sum02<0:
    print(0)
else:
    print(sum02)