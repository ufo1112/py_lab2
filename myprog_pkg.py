#!/usr/bin/python

import my_pkg
from my_pkg.num2 import num2

a = 0

while a != 3:
    print("<Select menu>")
    print("1) conversion")
    print("2) union/intersection")
    print("3) exit")
    a = int(input("what is your choice: "))

    if a == 1:
        b = input("input binary number: ")
        print(my_pkg.num1(b))
    if a == 2:
        b1 = input("1st list: ").replace('[',' ').replace(']',' ').replace(',',' ').split()
        b2 = input("2nd list : ").replace('[',' ').replace(']',' ').replace(',',' ').split()
        my_pkg.num2(b1, b2)
    if a == 3:
        exit(0)
