#!/usr/bin/env python3



with open("myfile", "r") as f:
    f.readline()
    for line in f:
        print(line.rstrip())

lines = open("myfile", "r").readlines()
print(lines)
