#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        cap = ord(ch) if ord(ch) < 97 else ord(ch) - 32
        print(f"{chr(cap)}", end='')
    print('')
