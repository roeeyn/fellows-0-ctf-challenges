#!/usr/bin/env python2.7
# TODO: remove flag.txt from sum.py's directory
import os

def add_points(filename, points):
    with open(filename, 'r') as fp:  # read contents
        curr_points = fp.read().strip()

    new_points = eval("%s + %s" % (curr_points, points))

    with open(filename, 'w') as fp:  # write and truncate
        fp.write(str(new_points))

    return new_points


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))

    points = raw_input()
    filename = 'will.txt'

    total_points = add_points(filename, points)
    print "Total points:", total_points
