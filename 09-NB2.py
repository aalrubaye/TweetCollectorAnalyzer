__author__ = 'Abduljaleel'
from db_sqlite3 import sqlite3
import networkx as nx
import csv
import numpy as np
import fib2
import os, sys
GI = nx.Graph()

SSS = 'District of Columbia'
LLL = 500
# db = sqlite3.connect('/Users/Abduljaleel/Desktop/project/SQLite/'+SSS)
loc = '/Users/Abduljaleel/Desktop/project/'
location3 = loc+SSS+'/3h'
location6 = loc+SSS+'/6h'
location12 = loc+SSS+'/12h'

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
def loop(mn, mx, array, array2, BigArray):
    for ddd in range(mn, mx):
        if (array[ddd] != 0):
            array2.append(ddd)
    for si in range(0,len(array2)):
        for sj in range(si+1,len(array2)):
            BigArray[array2[si]][array2[sj]] += 1
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
def put_into_Graph(weight, maxB, from_X, to_y, Name,D,location):
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

    edge_weight = csv.writer(open(location+"/edge_weight.csv", "wb"))
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
            # GI.add_edge(graphX[iar],graphY[iar],weight= www)

    nx.write_graphml(GI, location+"/graph/"+Name+".graphml")

    for s in nx.degree(GI):
        D.write(str(nx.degree(GI, s))+"\n")

    GI.clear()
def create(disease,TIME,location):

    ddb = sqlite3.connect(loc+SSS+'/SQLite/'+SSS+'_'+disease)
    # ddb = sqlite3.connect('/Users/Abduljaleel/Desktop/project/SQLite/'+SSS+'2')
    cc = ddb.cursor()

    heart_array = []
    heart2_array = []

    cc.execute("SELECT * FROM NODES order by date")
    ddb.commit()
    results = cc.fetchall()

    # LOOP ONE
    g_id = 0
    for row in results:
        # heart
        if (disease in row[2]):
            heart_array.append(g_id)
        else:
            heart_array.append(0)

        g_id += 1

    print g_id

    print 'finish LOOP ONE'

    # BigArray_heart = [[0 for j in range(g_id)] for i in range(g_id)]
    # BigArray_heart = np.empty((g_id,g_id),dtype=np.int)

    BigArray_heart = np.zeros((g_id,g_id))

    # Defining a window of 3 hours
    # window = '000030000'
    window = TIME
    in_case = '000001000'
    limit_1 = firstdate(ddb,cc)
    window_time = add_time(limit_1, window)
    limit_2 = add_time(limit_1, in_case)
    last_tweet_date = lastdate(ddb,cc)


    while True:
        cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
        ddb.commit()
        rs = cc.fetchall()

        if len(rs) > 1:
            mn = rs[0][0]
            mx = rs[len(rs)-1][0]

            print str(mn)+'--->'+str(mx)

            loop(mn, mx, heart_array, heart2_array, BigArray_heart)
            heart2_array = []

        limit_2 = add_time(limit_2, in_case)

        if limit_2 > window_time:
            break
    print "FINISH @!"

    limit_1 = next_event(limit_1,ddb,cc)

    while True:
        cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
        ddb.commit()
        rs = cc.fetchall()

        if len(rs) > 1:

            mn = rs[0][0]
            mx = rs[len(rs)-1][0]
            if mx>g_id:
                mx = g_id
            fff = mx-mn

            if (fff < LLL) and (fff > 0):

                loop(mn, mx, heart_array, heart2_array, BigArray_heart)
                heart2_array = []
                print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        limit_1 = add_time(limit_1, in_case)
        limit_2 = add_time(limit_1, window)

        if limit_1 >= last_tweet_date:
            break


    print "////////////////////////////////////////////////////////////////"

    print 'enter Large Loop'

    fibReturn = fib2.loop(g_id,BigArray_heart)

    weight_heart = fibReturn[0]
    from_X_heart = fibReturn[1]
    to_y_heart = fibReturn[2]
    maxB_heart = fibReturn[3]

    print "////////////////////////////////////////////////////////////////"
    print 'Finish i,j loops'
    print "////////////////////////////////////////////////////////////////"


    Heart = open(location+'/degree/'+disease+'.txt', 'w')

    put_into_Graph(weight_heart, maxB_heart, from_X_heart, to_y_heart, disease, Heart,location)
    log = open(loc+'log.txt', 'a')
    log.write("finish .... "+ SSS+ "_"+disease+" TW= "+TIME+"\n")
    print "finish "+ SSS+ "_"+disease

#
# create('heart','000030000',location3); create('heart','000060000',location6); create('heart','000120000',location12)
#
# create('cancer','000030000',location3);
create('cancer','000060000',location6);
# create('cancer','000120000',location12)

# create('clrd','000030000',location3); create('clrd','000060000',location6); create('clrd','000120000',location12)
#
# create('stroke','000030000',location3);create('stroke','000060000',location6);create('stroke','000120000',location12)

# create('alzheimer','000030000',location3); create('alzheimer','000060000',location6); create('alzheimer','000120000',location12)
#
# create('diabetes','000030000',location3); create('diabetes','000060000',location6); create('diabetes','000120000',location12)
#
# create('flu_or_pneumonia','000030000',location3); create('flu_or_pneumonia','000060000',location6);create('flu_or_pneumonia','000120000',location12)
#
# create('kidney','000030000',location3); create('kidney','000060000',location6); create('kidney','000120000',location12)

# create('septicemia','000030000',location3); create('septicemia','000060000',location6); create('septicemia','000120000',location12)
# # # #
# create('liver','000030000',location3); create('liver','000060000',location6); create('liver','000120000',location12)
#
# create('hyper','000030000',location3); create('hyper','000060000',location6); create('hyper','000120000',location12)
# #
# create('parkinson','000030000',location3); create('parkinson','000060000',location6); create('parkinson','000120000',location12)
#
