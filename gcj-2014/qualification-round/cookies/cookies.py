#!/usr/bin/python

import sys

def readinputs():
    t = int(sys.stdin.readline())
    inputs = []
    for i in range(t):
        words = sys.stdin.readline().split()
        inputs.append({
                'c': float(words[0]),
                'f': float(words[1]),
                'x': float(words[2])
            })
    return inputs

def solve(c, f, x):
    rate = 2.0
    if x <= c:
        return x / rate

    y = 0.0
    while True:
        time_current_rate = x / rate
        time_with_farm = c / rate + x / (rate + f)
        # print "Y %f, Rate %f : Times %f, %f" %(y, rate, time_current_rate, time_with_farm)
        if time_current_rate < time_with_farm:
            y += x / rate
            break
        else:
            y += c / rate
            rate += f

    return y


def main():
    index = 1
    for data in readinputs():
        res = solve(data['c'], data['f'], data['x'])
        print "Case #%d: %f" %(index, res)
        index += 1
    
main()

