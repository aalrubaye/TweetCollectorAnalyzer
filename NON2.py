__author__ = 'Abduljaleel'
import networkx as nx
from db_sqlite3 import sqlite3
import powerlaw
import plfit
import matplotlib.pyplot as plt
from collections import Counter
from pylab import *

GI = nx.Graph()


states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '
STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()


def ch(dis,loc,SSS):

    location3 = loc+SSS+'/3h/graph/'
    location6 = loc+SSS+'/6h/graph/'
    location12 = loc+SSS+'/12h/graph/'

    try:
        mg3 =nx.read_graphml(location3+dis+".graphml")
        mg6 =nx.read_graphml(location6+dis+".graphml")
        mg12 =nx.read_graphml(location12+dis+".graphml")



        db = sqlite3.connect(loc+SSS+'/SQLite/'+SSS+'_'+dis)
        c = db.cursor()
        c.execute("SELECT * FROM NODES order by date")
        db.commit()
        results = c.fetchall()

        print dis+' 3 :   '+str(len(results))+' ---> ('+str(mg3.number_of_nodes())+')   CC : ' +str(nx.average_clustering(mg3))
        print dis+' 6 :   '+str(len(results))+' ---> ('+str(mg6.number_of_nodes())+')   CC : ' +str(nx.average_clustering(mg6))
        print dis+' 12:   '+str(len(results))+' ---> ('+str(mg12.number_of_nodes())+')   CC : ' +str(nx.average_clustering(mg12))
        print '----------------------------------------'
    except:
        print dis + " No such graph"
        print '----------------------------------------'

locc = '/Users/Abduljaleel/Desktop/project/'


def alpha(SSS,dis):
    location3 = locc+SSS+'/3h'
    location6 = locc+SSS+'/6h'
    location12 = locc+SSS+'/12h'

    try:
        Degree = open(location3+'/degree/'+dis+'.txt', 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        three = fit.power_law.alpha

    except:
        print "Error"

    try:
        Degree = open(location6+'/degree/'+dis+'.txt', 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        six = fit.power_law.alpha

    except:
        print "Error"

    try:
        Degree = open(location12+'/degree/'+dis+'.txt', 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        twelve = fit.power_law.alpha

    except:
        print "Error"

    return (three,six,twelve)
    # R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
    # print R,p

def dod(SSS,dis):
    loc = '/Users/Abduljaleel/Desktop/project/'
    r = ch(dis,loc,SSS) ;


di = ["","heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]


###################################################
State = "Michigan"
dis = di[9]
###################################################

# 1 - # nodes + clustering
print '----------------------------------------'
dod(State,dis)
print '----------------------------------------'

# 2 - alpha
a = alpha(State,dis)
print '----------------------------------------'

print a
if (a[0] < a[1]) and (a[0] < a[2]):
    print '----------------------------------------'
    print "* * * * * * * : "+State
    print '----------------------------------------'

