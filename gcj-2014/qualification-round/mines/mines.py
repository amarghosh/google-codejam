#!/usr/bin/python

import sys
import re
import logging

def readinputs():
    return [[int(p) for p in sys.stdin.readline().split()] for i in range(int(sys.stdin.readline()))] 

def solve(r, c, m):
    logging.debug("%d %d %d" %(r, c, m))
    matrix = [['.' for i in range(c)] for j in range(r)]
    matrix[r-1][c-1] = 'c'

    if m > r * c:
        raise "m > r * c"

    if r == 1:
        for i in range(m):
            matrix[0][i] = '*'
        if m == c:
            return 'Impossible'
        return matrix

    if m == r * c - 1:
        for i in range(r):
            max_c = c if i < r - 1 else c - 1
            for j in range(max_c):
                matrix[i][j] = '*'
        logging.debug('full house')
        return matrix

    if m <= (r - 2) * c:
        for x in range(m):
            i = x / c
            j = x % c
            if j == c - 2 and x == m - 1:
                if j == 0:
                    logging.debug("oops j == 0")
                    return 'Impossible'
                i += 1
                j = 0
                matrix[i][j] = '*'
                if i == r - 2:
                    if (x - 1) % c == 0:
                        logging.debug("oops x - 1 % c")
                        return 'Impossible'
                    matrix[(x-1) / c][(x-1) % c] = '.'
                    matrix[i+1][j] = '*'
                    logging.debug('adjusted')
                    return matrix
            else:
                matrix[i][j] = '*'
        logging.debug('natural')
        return matrix

    if r > 1 and (m - (r - 2) * c) % 2 == 0:
        for i in range((r - 2) * c):
            matrix[i/c][i%c] = '*'
        remaining = m - (r - 2) * c
        for x in range(remaining):
            i = r - 2 + x % 2
            j = x / 2
            matrix[i][j] = '*'
        if r * c - m >= 4:
            logging.debug('just fits in')
            return matrix
    elif r > 3 and (m - (r - 3) * c) % 3 == 0:
        for i in range((r - 3) * c):
            matrix[i/c][i%c] = '*'
        remaining = m - (r - 3) * c
        for x in range(remaining):
            i = r - 3 + x % 3
            j = x / 3
            matrix[i][j] = '*'
        if r * c - m >= 6:
            logging.debug('just fits in 3')
            return matrix
        

    logging.debug("oops at the end")
    return 'Impossible'

def run():
    index = 1
    for data in readinputs():
        res = solve(data[0], data[1], data[2])
        dbg = ''
        if type(res) is str:
            output = res #+ " : %d, %d, %d" %(data[0], data[1], data[2])
        else:
            # dbg = "Success: %d, %d, %d" %(data[0], data[1], data[2])
            output = ''
            for row in res:
                output += ''.join(row) + '\n'
        print "Case #%d:%s\n%s" %(index, dbg, output.strip())
        index += 1
    print 
    

def test():
    r = 2
    c = 5
    # values = [6, 7, 8, 9, 14, 15, 16, 23, 24, 25, 32, 33, 39, 40]
    values = [1]
    for i in range(len(values)):
        res = solve(r, c, values[i])
        if type(res) is str:
            output = res
        else:
            output = ''
            for row in res:
                output += ' '.join(row) + '\n'

        print "Case #%d:\n%s" %(values[i], output.strip())


def main():
    if 1:
        run()
    else:
        logging.basicConfig(level=logging.DEBUG)
        test()

main()
