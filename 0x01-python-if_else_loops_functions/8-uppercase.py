#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        n = ord(ch)
        cap = n - 32 if n >= 97 and n <= 122 else n
        print("{:c}".format(cap), end='')
    print('')
