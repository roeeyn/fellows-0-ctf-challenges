#!/usr/bin/env python2.7

def read_file(filename):
    with open(filename) as fp:
        content = fp.read()
    return content


if __name__ == '__main__':
    print "Welcome to the most secure server in the entire fellowship!\n"

    admin_pass = read_file("admin.txt")
    typed_pass = input("Type the admin password to login: ")

    if admin_pass == typed_pass:
        flag = read_file("flag.txt")
        print flag
    else:
        print "Password is incorrect!"




