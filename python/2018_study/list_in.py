

list_num = [1, 2, 3, 4]

changes01 = [x * 2 for x in list_num]

changes02 = [x * 2 for x in list_num if x%2==1]
print(changes01)
print(changes02)
print()
tuple_num = [("book",1),("apple",2),("water",3)]
for product, logo in tuple_num:
    print("name : {0}, number : {1}".format(product,logo))


print()
dict_num = [{"name":"Kim","height":160},{"name":"Lee","height":170},{"name":"Han","height":180}]
for state in dict_num:
    print("name : %(name)s, height:%(height)d"% state)

print()

lambda_ex01 = [0, 2, 3, 5, 7]
lambda_ex02 = [1, 4, 6, 8, 9]
for i in range(len(lambda_ex01)):
    print(lambda x: x % 2 == 1, lambda_ex01[i])
    print(lambda x, y: x + y, lambda_ex01[i], lambda_ex02[i])

suming = lambda a,b: a+b
print(suming(5,10))
list01 = [1,2,3,8,9,10,5]
test_filter = list(filter(lambda x:x<5,list01))
#간단한 함수 생성가능. return기능포함
print(test_filter)

