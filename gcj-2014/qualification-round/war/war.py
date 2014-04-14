#!/usr/bin/python

import sys
import logging

def readinputs():
    return [ {
        'count': int(sys.stdin.readline()),
        'naomi': [float(p) for p in sys.stdin.readline().split()],
        'ken': [float(p) for p in sys.stdin.readline().split()]
    } for i in range(int(sys.stdin.readline()))]


def solve(count, naomi_org, ken_org):
    naomi = sorted(naomi_org)
    ken = sorted(ken_org)
    fair_score_naomi = 0

    for i in range(count):
        logging.debug("Round %d" %i)
        logging.debug(naomi)
        logging.debug(ken)
        if naomi[-1] > ken[-1]:
            fair_score_naomi += 1
            logging.debug("naomi scores with %f against %f" %(naomi[-1], ken[0]))
            del naomi[-1]
            del ken[0]
        else:
            kenlist = filter(lambda x: x > naomi[-1], ken)
            index = ken.index(kenlist[0])
            logging.debug("naomi loses with %f against %f" %(naomi[-1], ken[index]))
            del ken[index]
            del naomi[-1]

    logging.debug("fair_score_naomi %d\n" %fair_score_naomi)

    naomi = sorted(naomi_org)
    ken = sorted(ken_org)
    cheat_score_naomi = 0


    for i in range(count):
        logging.debug("Cheating Round %d" %i)
        logging.debug(naomi)
        logging.debug(ken)
        if len(naomi) == 1:
            if naomi[0] > ken[0]:
                logging.debug("naomi wins last round")
                cheat_score_naomi += 1
            else:
                logging.debug("naomi loses last round")
            break

        if naomi[-1] > ken[-1]:
            cheatlist = filter(lambda x: x > ken[0], naomi)
            index = naomi.index(cheatlist[0])
            cheat_score_naomi += 1
            logging.debug("naomi cheats with %f against %f" %(naomi[index], ken[0]))
            del naomi[index]
            del ken[0]
        else:
            cheatlist = filter(lambda x: x > ken[0] and x < ken[-1], naomi)
            if cheatlist:
                logging.debug("naomi cheats with %f against %f" %(naomi[0], ken[-1]))
                del naomi[0]
                del ken[-1]
            else:
                del naomi[0]
                del ken[0]
        

    return cheat_score_naomi, fair_score_naomi

def run():
    index = 1
    for data in readinputs():
        res = solve(data['count'], data['naomi'], data['ken'])
        print "Case #%d: %d %d" %(index, res[0], res[1])
        index += 1

def test():
    pass

def main():
    if 1:
        # logging.basicConfig(level=logging.DEBUG)
        run()
    else:
        logging.basicConfig(level=logging.DEBUG)
        test()

main()
