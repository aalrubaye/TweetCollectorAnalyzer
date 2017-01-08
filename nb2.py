__author__ = 'Abduljaleel'
from db_sqlite3 import sqlite3
import networkx as nx
import csv
import numpy as np
import fib2

def firstdate():
    sql = "SELECT min(date) FROM NODES"
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

    results = c.fetchall()
    for r in results:
        first = r[0]
    return first

def lastdate():
    sql = "SELECT max(date) FROM NODES"
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()

    results = c.fetchall()
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

def loop(mn, mx, array, array2, BigArray):
    for ddd in range(mn, mx):
        if (array[ddd] != 0):
            array2.append(ddd)
    for si in range(0,len(array2)):
        for sj in range(si+1,len(array2)):
            BigArray[array2[si]][array2[sj]] += 1

def next_event(d):
    sql = "SELECT min(date) FROM NODES WHERE DATE >"+str(d)
    try:
        c.execute(sql)
        db.commit()
    except:
        db.rollback()
    results = c.fetchall()
    for r in results:
        next = r[0]
    return next

def put_into_Graph(weight, maxB, from_X, to_y, Name,D):
    c0_1 = 0
    c0_2 = 0
    c0_3 = 0
    c0_4 = 0
    c0_5 = 0
    c0_6 = 0
    c0_7 = 0
    c0_8 = 0
    c0_9 = 0
    c0_10 = 0

    forgraph = []
    graphX = []
    graphY = []

    forgraph2 = []
    graphX2 = []
    graphY2 = []

    for iar in range(0,len(weight)):
        # forgraph2.append(weight[iar])
        # graphX2.append(from_X[iar])
        # graphY2.append(to_y[iar])

        norm = float(weight[iar])/maxB



        if (norm >= 0) and (norm < 0.1):
            c0_1 += 1
        else:
            if (norm >= 0.1) and (norm < 0.2):
                c0_2 += 1
            else:
                if (norm >= 0.2) and (norm < 0.3):
                    c0_3 += 1
                else:
                    if (norm >= 0.3) and (norm < 0.4):
                        c0_4 += 1
                    else:
                        if (norm >= 0.4) and (norm < 0.5):
                            c0_5 += 1
                        else:
                            if (norm >= 0.5) and (norm < 0.6):
                                c0_6 += 1
                            else:
                                if (norm >= 0.6) and (norm < 0.7):
                                    c0_7 += 1
                                else:
                                    if (norm >= 0.7) and (norm < 0.8):
                                        c0_8 += 1
                                    else:
                                        if (norm >= 0.8) and (norm < 0.9):

                                            forgraph.append(weight[iar])
                                            graphX.append(from_X[iar])
                                            graphY.append(to_y[iar])

                                            c0_9 += 1
                                        else:
                                            if (norm >= 0.9) and (norm <= 1):
                                                forgraph.append(weight[iar])
                                                graphX.append(from_X[iar])
                                                graphY.append(to_y[iar])
                                                c0_10 += 1
    print "////////////////////////////////////////////////////////////////"
    print "finish Big loop for "+Name
    print "////////////////////////////////////////////////////////////////"

    edge_weight.writerow(('---', Name))
    edge_weight.writerow(('0.1', c0_1))
    edge_weight.writerow(('0.2', c0_2))
    edge_weight.writerow(('0.3', c0_3))
    edge_weight.writerow(('0.4', c0_4))
    edge_weight.writerow(('0.5', c0_5))
    edge_weight.writerow(('0.6', c0_6))
    edge_weight.writerow(('0.7', c0_7))
    edge_weight.writerow(('0.8', c0_8))
    edge_weight.writerow(('0.9', c0_9))
    edge_weight.writerow(('1.0', c0_10))

    minG = maxB

    for iar in range(0,len(forgraph)):
        if forgraph[iar] < minG:
            minG = forgraph[iar]

    # print "minG" + str(minG)

    # print graphX
    for iar in range(0,len(forgraph)):
            www = int(forgraph[iar]-minG)
            GI.add_edge(graphX[iar],graphY[iar],weight= www)

    nx.write_graphml(GI, location+"/graph/"+Name+".graphml")

    for s in nx.degree(GI):
        D.write(str(nx.degree(GI, s))+"\n")

    # print 'ave  : '+str(nx.average_clustering(GI))

    GI.clear()

def create(disease,TIME):

    disease_array = []
    disease2_array = []

    c.execute("SELECT * FROM NODES order by date")
    db.commit()
    results = c.fetchall()

    # LOOP ONE
    g_id = 0
    for row in results:
        if (disease in row[2]):
            disease_array.append(g_id)
        else:
            disease_array.append(0)

        g_id += 1

    print 'finish LOOP ONE'


    BigArray = np.empty((g_id,g_id),dtype=np.int)

    window = TIME
    in_case = '000001000'
    limit_1 = firstdate()
    window_time = add_time(limit_1, window)
    limit_2 = add_time(limit_1, in_case)
    last_tweet_date = lastdate()


    while True:
        c.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
        db.commit()
        rs = c.fetchall()

        if len(rs) > 1:
            mn = rs[0][0]
            mx = rs[len(rs)-1][0]

            print str(mn)+'--->'+str(mx)

            loop(mn, mx, disease_array, disease2_array, BigArray)
            disease2_array = []

        limit_2 = add_time(limit_2, in_case)

        if limit_2 > window_time:
            break
    print "FINISH @!"

    limit_1 = next_event(limit_1)

    while True:
        c.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
        db.commit()
        rs = c.fetchall()

        if len(rs) > 1:

            mn = rs[0][0]
            mx = rs[len(rs)-1][0]
            if mx>g_id:
                mx = g_id
            fff = mx-mn

            if (fff < LLL) and (fff > 0):

                loop(mn, mx, disease_array, disease2_array, BigArray)
                heart2_array = []
                print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        limit_1 = add_time(limit_1, in_case)
        limit_2 = add_time(limit_1, window)

        if limit_1 >= last_tweet_date:
            break


    print "////////////////////////////////////////////////////////////////"

    print 'enter Large Loop'

    fibReturn = fib2.loop(g_id,BigArray)

    weight = fibReturn[0]
    from_X = fibReturn[1]
    to_y = fibReturn[2]
    maxB = fibReturn[3]

    print "////////////////////////////////////////////////////////////////"
    print 'Finish i,j loops'
    print "////////////////////////////////////////////////////////////////"


    deg = open(location+'/degree/'+disease+'.txt', 'w')

    put_into_Graph(weight, maxB, from_X, to_y, disease, deg)
    print "finish "+disease


SSS = 'North Dakota'
LLL = 1500

GI = nx.Graph()
db = sqlite3.connect('/Users/Abduljaleel/Desktop/project/SQLite/'+SSS)
c = db.cursor()
location = '/Users/Abduljaleel/Desktop/project/'+SSS+'/3h'
edge_weight = csv.writer(open(location+"/edge_weight.csv", "wb"))




create('heart','000030000')