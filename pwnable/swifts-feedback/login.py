#!/usr/bin/env python2.7

import os

def read_file(filename):
    with open(filename) as fp:
        content = fp.read()
    return content


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))  # change working dir

    admin_pass = read_file("admin.txt")
    typed_pass = input()

    if admin_pass == typed_pass:
        flag = read_file("flag.txt")
        print flag
    else:
        print "Password is incorrect!"




