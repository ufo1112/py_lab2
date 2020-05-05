#!/usr/bin/python
def num1(n):
    num=int(n,2)
    num8 = format(num,'o')
    num16 = format(num, 'X')
    return("=> OCT> %s \n=> DEC> %s \n=> HEX> %s" %(num8,num,num16))

if __name__=='__main__':
        print("exit")

