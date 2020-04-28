#!/usr/bin/python

def num2(b1, b2):


    b3 = list(set(b1).intersection(set(b2)))
    b4 = list(set(b1)-set(b3))
    b5 = b1 + b2
    b6 = list(set(b5))
    print('union [',end='')
    for i in range(len(b6)-1):
        print(b6[i],end=',')
    print(b6[len(b6)-1],end='')
    print(']')
    print('intersection [',end='')
    for i in range(len(b3)-1):
        print(b3[i],end=',')
    print(b3[len(b3)-1],end='')
    print(']')
