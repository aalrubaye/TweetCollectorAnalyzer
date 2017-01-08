__author__ = 'Abduljaleel'
import igraph
from db_sqlite3 import sqlite3
import networkx as nx
import igraph
import fib4
import matplotlib.pyplot as plt
import time

# Net1 = nx.Graph()
Net1 = igraph.Graph()

def firstdate(ddb,cc):
    sql = "SELECT min(date) FROM NODES"
    try:
        cc.execute(sql)
        ddb.commit()
    except:
        ddb.rollback()

    results = cc.fetchall()
    for r in results:
        first = r[0]
    return first
def lastdate(ddb,cc):
    sql = "SELECT max(date) FROM NODES"
    try:
        cc.execute(sql)
        ddb.commit()
    except:
        ddb.rollback()

    results = cc.fetchall()
    for r in results:
        last = r[0]

    return last
def add_time(time,add):
    Time = str(time)

    month = Time[0:1]
    day = Time[1:3]
    hour = Time[3:5]
    minute = Time[5:7]
    second = Time[7:9]

    month_a = add[0:1]
    day_a = add[1:3]
    hour_a = add[3:5]
    minute_a = add[5:7]
    second_a = add[7:9]

    sec_sum = int(second)+int(second_a)
    div_s = sec_sum / 60
    remainder_s = sec_sum % 60
    if len(str(remainder_s)) == 1:
        S = '0'+str(remainder_s)
    else:
        S = str(remainder_s)

    min_sum = int(minute) + int(minute_a) + int(div_s)
    div_m = min_sum / 60
    remainder_m = min_sum % 60
    if len(str(remainder_m)) == 1:
        M = '0'+str(remainder_m)
    else:
        M = str(remainder_m)

    hour_sum = int(hour) + int (hour_a) + int(div_m)
    div_h = hour_sum / 24
    remainder_h = hour_sum % 24
    if len(str(remainder_h)) == 1:
        H = '0'+str(remainder_h)
    else:
        H = str(remainder_h)

    day_sum = int(day) + int (day_a) + int (div_h)
    remainder_d = 0
    if month == '2':
        div_d = day_sum / 29
        remainder_d = day_sum % 29
    elif month == '3':
        div_d = day_sum / 32
        remainder_d = day_sum % 32
    else:
        div_d = day_sum / 31
        remainder_d = day_sum % 31

    if len(str(remainder_d)) == 1:
        D = '0'+str(remainder_d)
    else:
        D = str(remainder_d)

    mon_sum = int(month) + int(month_a) + int(div_d)
    if D == '00':
        D = '01'
    return int(str(mon_sum) + D+H+M+S)
def next_event(d,ddb,cc):
    sql = "SELECT min(date) FROM NODES WHERE DATE >"+str(d)
    try:
        cc.execute(sql)
        ddb.commit()
    except:
        ddb.rollback()
    results = cc.fetchall()
    for r in results:
        next = r[0]
    return next
def add_vertex(g, name,added_vertices):
    if name not in added_vertices:
        added_vertices.add(name)
        g.add_vertex(name)
def loop(N,aa,added_vertices):
    for j in range (0,len(aa)):
        for jj in range (j+1,len(aa)):
            add_vertex(N,str(aa[j]),added_vertices)
            add_vertex(N,str(aa[jj]),added_vertices)
            N.add_edge(str(aa[j]),str(aa[jj]))
def degrees(N,dd):
    for node in N.degree():
        dd.write(str(node)+'\n')
def weighted_degree(N,dd):
    # a = []
    for node in N.nodes():
        n = N[node]

        sum=0
        for r in n:
            sum +=n[r]['weight']
        dd.write(str(sum)+'\n')
        # a.append(sum)
    # return a
def degree_dist(data,loc):
    aj = []
    ac = []
    for i in range (0,max(data)):
        j = i+1
        count = 0
        for k in range (0,len(data)):
            if data[k] == j:
                count +=1
        loc.write(str(j)+'\t'+str(count)+'\n')
        aj.append(j)
        ac.append(count)
    return (aj,ac)
def build(state,Time,dis,window,in_case):
    added_vertices = set()
    db = '/Users/Abduljaleel/Desktop/project1/'+state+'/SQLite/'+state+'_'+dis
    ddb = sqlite3.connect(db)
    cc = ddb.cursor()

    cc.execute("SELECT * FROM NODES order by date")
    ddb.commit()
    results = cc.fetchall()
    all = len(results)

    limit_1 = firstdate(ddb,cc)
    window_time = add_time(limit_1, window)
    limit_2 = add_time(limit_1, in_case)
    last_tweet_date = lastdate(ddb,cc)

    if (all>=30):
        while True:
            cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
            ddb.commit()
            rs = cc.fetchall()
            aa=[]
            for i in range (0,len(rs)):
                aa.append(rs[i][0])
            fib4.loop(Net1,aa,added_vertices)

            limit_2 = add_time(limit_2, in_case)

            if limit_2 > window_time:
                break

        limit_1 = next_event(limit_1,ddb,cc)

        while True:
            cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
            ddb.commit()
            rs = cc.fetchall()
            aa=[]

            try:
                d = int(rs[0][0])
                e = float(d*100)/all
                print int(e)
            except:
                pr=1

            for i in range (0,len(rs)):
                aa.append(rs[i][0])

            fib4.loop(Net1,aa,added_vertices)

            limit_1 = add_time(limit_1, in_case)
            limit_2 = add_time(limit_1, window)

            if limit_1 >= last_tweet_date:
                break
        added_vertices = set()
        print 'finish creating'

        # print '------degree start------'
        # location = '/Users/Abduljaleel/Desktop/project/degrees/'+state+'/'+Time
        # de = open(location+'/degree/'+dis+'_degree.txt','a')
        # wde = open(location+'/weighted_degree/'+dis+'_wd.txt','a')
        #
        # degrees(Net1,de)
        # weighted_degree(Net1,wde)

        print '------Writing Graphml start------'+ state+'---'+Time+'----'+dis
        # nx.write_graphml(Net1, '/Users/Abduljaleel/Desktop/project/graphs/'+state+'/'+Time+'/'+dis+'_'+Time+'.graphml')
        Net1.write_graphml('/Users/Abduljaleel/Desktop/project/graphs/'+state+'/'+Time+'/'+dis+'_'+Time+'.graphml')


def window(state,h):
    Time = h+'h'
    w = '0000'+h+'0000'
    i = '000001000'
    build(state,Time,'heart',w,i)
    build(state,Time,'cancer',w,i)
    build(state,Time,'clrd',w,i)
    build(state,Time,'stroke',w,i)
    build(state,Time,'alzheimer',w,i)
    build(state,Time,'diabetes',w,i)
    build(state,Time,'flu_or_pneumonia',w,i)
    build(state,Time,'kidney',w,i)
    build(state,Time,'septicemia',w,i)
    build(state,Time,'liver',w,i)
    build(state,Time,'hyper',w,i)
    build(state,Time,'parkinson',w,i)

def do(state):
    window(state,'1')
    # window(state,'2')
    # window(state,'3')
    # window(state,'4')
    # window(state,'5')
    # window(state,'6')


state = 'Alabama'
do(state)
# state = 'Alaska'
# do(state)
