#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    if arglen < 2:
        print("{} arguments.".format(arglen - 1))
    else:
        if arglen == 2:
            print("{} argument:".format(arglen - 1))
        else:
            print("{} arguments:".format(arglen - 1))
    for n in range(1, arglen):
        print("{}: {}".format(n, argv[n]))
