'''
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
'''

import sys

maxlength = input()
stone = input()
stack = input()
stack=stack.split(' ')
maxroute = stack[-1]
maxlength = int(maxlength)
seat = int(stack[0])
routin = 0
for i in range(len(stack)):
    for j in range(int(maxlength)):
        counting = seat + maxlength - j
        scounting = str(counting)
        if str(counting) in stack:
            location = stack.index(scounting)
            seat = stack[location]
            routin = routin + 1
        if counting == 0:
            seat = -1

    if seat == -1:
        print("can't go to the end")
        break

if seat == -1:
    print("-1")
else:
    print(routin)

'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

# inf = open('input.txt');


'''
inf = sys.stdin

T = inf.readline();

for t in range(0, int(T)):
    Answer = 0;

    #############################################################################################
    #
    #  Implement your algorithm here.
    #  The answer to the case will be stored in variable Answer.
    #
    #############################################################################################

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()
'''