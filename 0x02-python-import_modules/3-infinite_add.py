#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    counter = 0

    for i in range(1, argc):
        counter = counter + int(argv[i])

    print(counter)
