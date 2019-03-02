#!/usr/bin/python3
import os
import sys
import fileinput

with open('a-frame.txt','r+') as f:
    exit_char = '{', ';'
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

# f = open('a-frame.txt', 'r+')


f.close()

