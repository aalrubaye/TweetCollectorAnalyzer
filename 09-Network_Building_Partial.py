__author__ = 'Abduljaleel'
from db_sqlite3 import sqlite3
import networkx as nx
import csv
import numpy as np
import fib


db = sqlite3.connect('FLdb_Partial')
c = db.cursor()

location = '/Users/Abduljaleel/Desktop/project'
edge_weight = csv.writer(open(location+"/edge_weight.csv", "wb"))

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

def put_into_Graph(weight, maxB, from_X, to_y, Name,D, csvout):
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

    csvout.writerow(('---', Name))

    ir = 1
    for nnn in sorted(weight, reverse=True):
        fraction = float(ir)/float(len(weight))
        csvout.writerow((fraction, nnn))
        ir += 1

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

    nx.write_graphml(GI, location+"/graph/"+Name+"_Graph.graphml")

    for s in nx.degree(GI):
        D.write(str(nx.degree(GI, s))+"\n")

    # print 'ave  : '+str(nx.average_clustering(GI))

    GI.clear()


heart_array = []
heart2_array = []
stroke_array = []
stroke2_array = []
diabetes_array = []
diabetes2_array = []
hyper_array = []
hyper2_array = []


c.execute("SELECT * FROM NODES order by date")
db.commit()
results = c.fetchall()

# LOOP ONE
g_id = 0
for row in results:
    # heart
    if ('heart' in row[2]):
        heart_array.append(g_id)
    else:
        heart_array.append(0)

    # stroke
    if ('stroke' in row[2]):
        stroke_array.append(g_id)
    else:
        stroke_array.append(0)

    # diabetes
    if ('diabetes' in row[2]):
        diabetes_array.append(g_id)
    else:
        diabetes_array.append(0)

    # hyper
    if ('hyper' in row[2]):
        hyper_array.append(g_id)
    else:
        hyper_array.append(0)

    g_id += 1
print 'finish LOOP ONE'

# BigArray_heart = [[0 for j in range(g_id)] for i in range(g_id)]
BigArray_heart = np.empty((g_id,g_id),dtype=np.int)
BigArray_stroke = np.empty((g_id,g_id),dtype=np.int)
BigArray_diabetes = np.empty((g_id,g_id),dtype=np.int)
BigArray_hyper = np.empty((g_id,g_id),dtype=np.int)


# Defining a window of 3 hours
window = '000120000'
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

        loop(mn, mx, heart_array, heart2_array, BigArray_heart)
        heart2_array = []
        loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
        stroke2_array = []
        loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
        diabetes2_array = []
        loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
        hyper2_array = []

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
        fff = mx-mn
        # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        if (fff < 2500):
            loop(mn, mx, heart_array, heart2_array, BigArray_heart)
            heart2_array = []
            loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
            stroke2_array = []
            loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
            diabetes2_array = []
            loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
            hyper2_array = []
            print str(mn)+'--->'+str(mx) +'  = ' +str(fff)
        else:
            print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

    limit_1 = add_time(limit_1, in_case)
    limit_2 = add_time(limit_1, window)

    if limit_1 >= last_tweet_date:
        break


print "////////////////////////////////////////////////////////////////"

print 'enter Large Loop'

fibReturn = fib.loop(g_id,BigArray_heart,BigArray_stroke,BigArray_diabetes,BigArray_hyper)

weight_heart = fibReturn[0]
weight_stroke = fibReturn[1]
weight_diabetes = fibReturn[2]
weight_hyper = fibReturn[3]

from_X_heart = fibReturn[4]
from_X_stroke = fibReturn[5]
from_X_diabetes = fibReturn[6]
from_X_hyper = fibReturn[7]

to_y_heart = fibReturn[8]
to_y_stroke = fibReturn[9]
to_y_diabetes = fibReturn[10]
to_y_hyper = fibReturn[11]

maxB_heart = fibReturn[12]
maxB_stroke = fibReturn[13]
maxB_diabetes = fibReturn[14]
maxB_hyper = fibReturn[15]

print "////////////////////////////////////////////////////////////////"
print 'Finish i,j loops'
print "////////////////////////////////////////////////////////////////"

GI = nx.Graph()

heart_weight = csv.writer(open(location+"/weight/Heart_weight.csv", "wb"))
stroke_weight = csv.writer(open(location+"/weight/Stroke_weight.csv", "wb"))
diabetes_weight = csv.writer(open(location+"/weight/Diabetes_weight.csv", "wb"))
hyper_weight = csv.writer(open(location+"/weight/Hyper_weight.csv", "wb"))

Heart = open(location+'/degree/heart.txt', 'w')
Stroke = open(location+'/degree/stroke.txt', 'w')
Diabetes = open(location+'/degree/diabetes.txt', 'w')
Hyper = open(location+'/degree/hyper.txt', 'w')

put_into_Graph(weight_heart, maxB_heart, from_X_heart, to_y_heart, 'Heart', Heart, heart_weight)
print "finish Heart"
put_into_Graph(weight_stroke, maxB_stroke, from_X_stroke, to_y_stroke, 'Stroke', Stroke, stroke_weight)
print "finish Stroke"
put_into_Graph(weight_diabetes, maxB_diabetes, from_X_diabetes, to_y_diabetes, 'Diabetes', Diabetes, diabetes_weight)
print "finish Diabetes"
put_into_Graph(weight_hyper, maxB_hyper, from_X_hyper, to_y_hyper, 'Hyper', Hyper, hyper_weight)
print "finish Hyper"
