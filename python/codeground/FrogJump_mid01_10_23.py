'''
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
'''

import sys

'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

# inf = open('input.txt');
inf = sys.stdin

T = inf.readline();






for t in range(0, int(T)):
    Answer = int(0);
    howmany = int(input())
    string = input()
    string = string.split(' ')
    results = []
    start = string[0]
    for i in range(len(string)):
        string[i] = int(string[i])
    start = string[0]
    jump = int(input())
    for i in range(howmany):
        for j in range(jump):
            long = jump - j
            place = start + long
            if place in string:
                start = place
                Answer = Answer + 1
                break
            if long == 0:
                start= -1
                break
        if start == -1:
            break
    if start == -1:
        Answer = start
    #############################################################################################
    #
    #  Implement your algorithm here.
    #  The answer to the case will be stored in variable Answer.
    #
    #############################################################################################
    print(howmany)
    print(string)
    print(start)
    print(jump)
    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()