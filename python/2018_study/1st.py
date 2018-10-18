
print("start")

say = " "
last = ""
say = input("input words : ")
last = say[-1]
print("Last word = {0}".format(last))
while(True):
    say = input("input words : ")
    while(not(last in say[1])):
        print("Worng")
        say = input("input words : ")
# while(True):
#     say = input("input words : ")
#     if()
#     i = 0
#     while (say[i] == ' '):
#         i = i + 1
#     print(i)
#     print("last word = {0}".format(say[i - 1]))
