#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nprinted = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            nprinted += 1
        print("")
    except:
        print("")
        pass
    return nprinted
