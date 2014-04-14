#!/usr/bin/python

import sys

def readinputs():
    inputs = [[{
        'choice': int(sys.stdin.readline()),
        'matrix': [[int(p) for p in sys.stdin.readline().split()] for i in range(4)]
    } for i in range(2)] for i in range(int(sys.stdin.readline()))]
    return inputs

def solve(data):
    first_set = data[0]['matrix'][data[0]['choice'] - 1]
    second_set = data[1]['matrix'][data[1]['choice'] - 1]
    intersection = filter(lambda x: x in second_set, first_set)
    if len(intersection) == 1:
        return intersection[0]
    elif len(intersection) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def main():
    index = 1
    for data in readinputs():
        res = solve(data)
        print "Case #%d: %s" %(index, res)
        index += 1
    
main()

