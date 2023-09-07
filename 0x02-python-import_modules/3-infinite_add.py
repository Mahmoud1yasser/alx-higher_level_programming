#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    sumation = 0
    for n in range (1, arglen):
        sumation = int(argv[n]) + sumation
    print("{}".format(sumation))
    
