a = input(" input : ")
dic01={}
for i in range(len(a)):
    dic01[i] = a[i]
store = {}
for i in range(len(a)):
    if(not(a in store)):
        store[a]=int(0)
    else:
        store[a(i)] =int(store[a(i)]+1)
key = list(store.keys())
print(key)
print(dic01)
print(store)
# for i in range(len(key)):
#     print(key(i))
#     print(dic01[i])
#     print()


# keys = dic01.keys()
# lvalues = list(values)
# lkeys = list(keys)
# store = {}
