__author__ = 'Abduljaleel'

import powerlaw
import plfit
import matplotlib.pyplot as plt
from collections import Counter
from pylab import *
import networkx as nx
import csv

states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '
STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

loc = '/Users/Abduljaleel/Desktop/project/Diseases_Net/'

bet = csv.writer(open(loc+'betweenness.csv', "wb"))
cls = csv.writer(open(loc+'closeness.csv', "wb"))


def centrality(SSS):



    try:
        graph =nx.read_graphml(loc+"graph/ND_"+SSS+".graphml")

        b = nx.betweenness_centrality(graph)
        c = nx.closeness_centrality(graph)

        bet.writerow((SSS,b["0"],b["1"],b["2"],b["3"],b["4"],b["5"],b["6"],b["7"],b["8"],b["9"],b["10"],b["11"],b["12"]))
        cls.writerow((SSS,c["0"],c["1"],c["2"],c["3"],c["4"],c["5"],c["6"],c["7"],c["8"],c["9"],c["10"],c["11"],c["12"]))

    except:
        print "Error in " + SSS
        found = False


for i in range (0,len(STATE)):
    centrality (STATE[i])

