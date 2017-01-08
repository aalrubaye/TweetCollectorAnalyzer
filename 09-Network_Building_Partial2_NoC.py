__author__ = 'Abduljaleel'
from db_sqlite3 import sqlite3
import networkx as nx
import csv
import numpy as np

SSS = 'Iowa'
LLL = 1500

db = sqlite3.connect(SSS)
c = db.cursor()

location = '/Users/Abduljaleel/Desktop/project/'+SSS+'/3h'

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

def Bigloop(g_i,BigArray):
    weightt = []
    from_X = []
    to_y = []
    maxB = BigArray[0][0]
    for x in range(0, g_i-1):
        for y in range(0, g_i-1):
            if BigArray[x][y] != 0:
                if BigArray[x][y] > maxB:
                    maxB = BigArray[x][y]
                weightt.append(BigArray[x][y])
                from_X.append(x)
                to_y.append(y)
            print str(x)+'    &    '+str(y)
    return (weightt,from_X,to_y,maxB)

def fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson):
    weight_heart = []
    weight_cancer = []
    weight_clrd = []
    weight_stroke = []
    weight_alzheimer = []
    weight_diabetes = []
    weight_flupne = []
    weight_kidney = []
    weight_septicemia = []
    weight_liver = []
    weight_hyper = []
    weight_parkinson = []

    from_X_heart = []
    from_X_cancer = []
    from_X_clrd = []
    from_X_stroke = []
    from_X_alzheimer = []
    from_X_diabetes = []
    from_X_flupne = []
    from_X_kidney = []
    from_X_septicemia = []
    from_X_liver = []
    from_X_hyper = []
    from_X_parkinson = []

    to_y_heart = []
    to_y_cancer = []
    to_y_clrd = []
    to_y_stroke = []
    to_y_alzheimer = []
    to_y_diabetes = []
    to_y_flupne = []
    to_y_kidney = []
    to_y_septicemia = []
    to_y_liver = []
    to_y_hyper = []
    to_y_parkinson = []

    maxB_heart = BigArray_heart[0][0]
    maxB_cancer = BigArray_cancer[0][0]
    maxB_clrd = BigArray_clrd[0][0]
    maxB_stroke = BigArray_stroke[0][0]
    maxB_alzheimer = BigArray_alzheimer[0][0]
    maxB_diabetes = BigArray_diabetes[0][0]
    maxB_flupne = BigArray_flupne[0][0]
    maxB_kidney = BigArray_kidney[0][0]
    maxB_septicemia = BigArray_septicemia[0][0]
    maxB_liver = BigArray_liver[0][0]
    maxB_hyper = BigArray_hyper[0][0]
    maxB_parkinson = BigArray_parkinson[0][0]


    for x in range(0, g_id-1):
        for y in range(0, g_id-1):

            if BigArray_heart[x][y] != 0:
                if BigArray_heart[x][y] > maxB_heart:
                    maxB_heart = BigArray_heart[x][y]
                weight_heart.append(BigArray_heart[x][y])
                from_X_heart.append(x)
                to_y_heart.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_cancer[x][y] != 0:
                if BigArray_cancer[x][y] > maxB_cancer:
                    maxB_cancer = BigArray_cancer[x][y]
                weight_cancer.append(BigArray_cancer[x][y])
                from_X_cancer.append(x)
                to_y_cancer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_clrd[x][y] != 0:
                if BigArray_clrd[x][y] > maxB_clrd:
                    maxB_clrd = BigArray_clrd[x][y]
                weight_clrd.append(BigArray_clrd[x][y])
                from_X_clrd.append(x)
                to_y_clrd.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_stroke[x][y] != 0:
                if BigArray_stroke[x][y] > maxB_stroke:
                    maxB_stroke = BigArray_stroke[x][y]
                weight_stroke.append(BigArray_stroke[x][y])
                from_X_stroke.append(x)
                to_y_stroke.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_alzheimer[x][y] != 0:
                if BigArray_alzheimer[x][y] > maxB_alzheimer:
                    maxB_alzheimer = BigArray_alzheimer[x][y]
                weight_alzheimer.append(BigArray_alzheimer[x][y])
                from_X_alzheimer.append(x)
                to_y_alzheimer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_diabetes[x][y] != 0:
                if BigArray_diabetes[x][y] > maxB_diabetes:
                    maxB_diabetes = BigArray_diabetes[x][y]
                weight_diabetes.append(BigArray_diabetes[x][y])
                from_X_diabetes.append(x)
                to_y_diabetes.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_flupne[x][y] != 0:
                if BigArray_flupne[x][y] > maxB_flupne:
                    maxB_flupne = BigArray_flupne[x][y]
                weight_flupne.append(BigArray_flupne[x][y])
                from_X_flupne.append(x)
                to_y_flupne.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_kidney[x][y] != 0:
                if BigArray_kidney[x][y] > maxB_kidney:
                    maxB_kidney = BigArray_kidney[x][y]
                weight_kidney.append(BigArray_kidney[x][y])
                from_X_kidney.append(x)
                to_y_kidney.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_septicemia[x][y] != 0:
                if BigArray_septicemia[x][y] > maxB_septicemia:
                    maxB_septicemia = BigArray_septicemia[x][y]
                weight_septicemia.append(BigArray_septicemia[x][y])
                from_X_septicemia.append(x)
                to_y_septicemia.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_liver[x][y] != 0:
                if BigArray_liver[x][y] > maxB_liver:
                    maxB_liver = BigArray_liver[x][y]
                weight_liver.append(BigArray_liver[x][y])
                from_X_liver.append(x)
                to_y_liver.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_hyper[x][y] != 0:
                if BigArray_hyper[x][y] > maxB_hyper:
                    maxB_hyper = BigArray_hyper[x][y]
                weight_hyper.append(BigArray_hyper[x][y])
                from_X_hyper.append(x)
                to_y_hyper.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_parkinson[x][y] != 0:
                if BigArray_parkinson[x][y] > maxB_parkinson:
                    maxB_parkinson = BigArray_parkinson[x][y]
                weight_parkinson.append(BigArray_parkinson[x][y])
                from_X_parkinson.append(x)
                to_y_parkinson.append(y)
            print str(x)+'    &    '+str(y)


    return (weight_heart,weight_cancer,weight_clrd,weight_stroke,weight_alzheimer,weight_diabetes,weight_flupne,weight_kidney,weight_septicemia,weight_liver,weight_hyper,weight_parkinson,
    from_X_heart,from_X_cancer,from_X_clrd,from_X_stroke,from_X_alzheimer,from_X_diabetes,from_X_flupne,from_X_kidney,from_X_septicemia,from_X_liver,from_X_hyper,from_X_parkinson,
    to_y_heart,to_y_cancer,to_y_clrd,to_y_stroke,to_y_alzheimer,to_y_diabetes,to_y_flupne,to_y_kidney,to_y_septicemia,to_y_liver,to_y_hyper,to_y_parkinson,
    maxB_heart,maxB_cancer,maxB_clrd,maxB_stroke,maxB_alzheimer,maxB_diabetes,maxB_flupne,maxB_kidney,maxB_septicemia,maxB_liver,maxB_hyper,maxB_parkinson)



heart_array = []
heart2_array = []
cancer_array = []
cancer2_array = []
clrd_array = []
clrd2_array = []
stroke_array = []
stroke2_array = []
alzheimer_array = []
alzheimer2_array = []
diabetes_array = []
diabetes2_array = []
flupne_array = []
flupne2_array = []
kidney_array = []
kidney2_array = []
septicemia_array = []
septicemia2_array = []
liver_array = []
liver2_array = []
hyper_array = []
hyper2_array = []
parkinson_array = []
parkinson2_array = []


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

    # cancer
    if ('cancer' in row[2]):
        cancer_array.append(g_id)
    else:
        cancer_array.append(0)

    # clrd
    if ('clrd' in row[2]):
        clrd_array.append(g_id)
    else:
        clrd_array.append(0)

    # stroke
    if ('stroke' in row[2]):
        stroke_array.append(g_id)
    else:
        stroke_array.append(0)

    # alzheimer
    if ('alzheimer' in row[2]):
        alzheimer_array.append(g_id)
    else:
        alzheimer_array.append(0)

    # diabetes
    if ('diabetes' in row[2]):
        diabetes_array.append(g_id)
    else:
        diabetes_array.append(0)

    # flu_or_pneumonia
    if ('flu_or_pneumonia' in row[2]):
        flupne_array.append(g_id)
    else:
        flupne_array.append(0)

    # kidney
    if ('kidney' in row[2]):
        kidney_array.append(g_id)
    else:
        kidney_array.append(0)

    # septicemia
    if ('septicemia' in row[2]):
        septicemia_array.append(g_id)
    else:
        septicemia_array.append(0)

    # liver
    if ('liver' in row[2]):
        liver_array.append(g_id)
    else:
        liver_array.append(0)

    # hyper
    if ('hyper' in row[2]):
        hyper_array.append(g_id)
    else:
        hyper_array.append(0)

    # parkinson
    if ('parkinson' in row[2]):
        parkinson_array.append(g_id)
    else:
        parkinson_array.append(0)

    g_id += 1
print 'finish LOOP ONE'

# BigArray_heart = [[0 for j in range(g_id)] for i in range(g_id)]
BigArray_heart = np.empty((g_id,g_id),dtype=np.int)
BigArray_cancer = np.empty((g_id,g_id),dtype=np.int)
BigArray_clrd = np.empty((g_id,g_id),dtype=np.int)
BigArray_stroke = np.empty((g_id,g_id),dtype=np.int)
BigArray_alzheimer = np.empty((g_id,g_id),dtype=np.int)
BigArray_diabetes = np.empty((g_id,g_id),dtype=np.int)
BigArray_flupne = np.empty((g_id,g_id),dtype=np.int)
BigArray_kidney = np.empty((g_id,g_id),dtype=np.int)
BigArray_septicemia = np.empty((g_id,g_id),dtype=np.int)
BigArray_liver = np.empty((g_id,g_id),dtype=np.int)
BigArray_hyper = np.empty((g_id,g_id),dtype=np.int)
BigArray_parkinson = np.empty((g_id,g_id),dtype=np.int)

# Defining a window of 3 hours
window = '000030000'
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
        loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
        cancer2_array = []
        loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
        clrd2_array = []
        loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
        stroke2_array = []
        loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
        alzheimer2_array = []
        loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
        diabetes2_array = []
        loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
        flupne2_array = []
        loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
        kidney2_array = []
        loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
        septicemia2_array = []
        loop(mn, mx, liver_array, liver2_array, BigArray_liver)
        liver2_array = []
        loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
        hyper2_array = []
        loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
        parkinson2_array = []

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
        # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        if (fff < LLL) and (fff > 0):

            loop(mn, mx, heart_array, heart2_array, BigArray_heart)
            heart2_array = []
            loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
            cancer2_array = []
            loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
            clrd2_array = []
            loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
            stroke2_array = []
            loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
            alzheimer2_array = []
            loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
            diabetes2_array = []
            loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
            flupne2_array = []
            loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
            kidney2_array = []
            loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
            septicemia2_array = []
            loop(mn, mx, liver_array, liver2_array, BigArray_liver)
            liver2_array = []
            loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
            hyper2_array = []
            loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
            parkinson2_array = []
            print str(mn)+'--->'+str(mx) +'  = ' +str(fff)
        # else:
            # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

    limit_1 = add_time(limit_1, in_case)
    limit_2 = add_time(limit_1, window)

    if limit_1 >= last_tweet_date:
        break


print "////////////////////////////////////////////////////////////////"

print 'enter Large Loop'


fibReturn = fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson)

weight_heart = fibReturn[0]
weight_cancer = fibReturn[1]
weight_clrd = fibReturn[2]
weight_stroke = fibReturn[3]
weight_alzheimer = fibReturn[4]
weight_diabetes = fibReturn[5]
weight_flupne = fibReturn[6]
weight_kidney = fibReturn[7]
weight_septicemia = fibReturn[8]
weight_liver = fibReturn[9]
weight_hyper = fibReturn[10]
weight_parkinson = fibReturn[11]


from_X_heart = fibReturn[12]
from_X_cancer = fibReturn[13]
from_X_clrd = fibReturn[14]
from_X_stroke = fibReturn[15]
from_X_alzheimer = fibReturn[16]
from_X_diabetes = fibReturn[17]
from_X_flupne = fibReturn[18]
from_X_kidney = fibReturn[19]
from_X_septicemia = fibReturn[20]
from_X_liver = fibReturn[21]
from_X_hyper = fibReturn[22]
from_X_parkinson = fibReturn[23]


to_y_heart = fibReturn[24]
to_y_cancer = fibReturn[25]
to_y_clrd = fibReturn[26]
to_y_stroke = fibReturn[27]
to_y_alzheimer = fibReturn[28]
to_y_diabetes = fibReturn[29]
to_y_flupne = fibReturn[30]
to_y_kidney = fibReturn[31]
to_y_septicemia = fibReturn[32]
to_y_liver = fibReturn[33]
to_y_hyper = fibReturn[34]
to_y_parkinson = fibReturn[35]


maxB_heart = fibReturn[36]
maxB_cancer = fibReturn[37]
maxB_clrd = fibReturn[38]
maxB_stroke = fibReturn[39]
maxB_alzheimer = fibReturn[40]
maxB_diabetes = fibReturn[41]
maxB_flupne = fibReturn[42]
maxB_kidney = fibReturn[43]
maxB_septicemia = fibReturn[44]
maxB_liver = fibReturn[45]
maxB_hyper = fibReturn[46]
maxB_parkinson = fibReturn[47]



print "////////////////////////////////////////////////////////////////"
print 'Finish i,j loops'
print "////////////////////////////////////////////////////////////////"

GI = nx.Graph()

heart_weight = csv.writer(open(location+"/weight/Heart_weight.csv", "wb"))
cancer_weight = csv.writer(open(location+"/weight/Cancer_weight.csv", "wb"))
clrd_weight = csv.writer(open(location+"/weight/Clrd_weight.csv", "wb"))
stroke_weight = csv.writer(open(location+"/weight/Stroke_weight.csv", "wb"))
alzheimer_weight = csv.writer(open(location+"/weight/Alzheimer_weight.csv", "wb"))
diabetes_weight = csv.writer(open(location+"/weight/Diabetes_weight.csv", "wb"))
flupne_weight = csv.writer(open(location+"/weight/Flupne_weight.csv", "wb"))
kidney_weight = csv.writer(open(location+"/weight/Kidney_weight.csv", "wb"))
septicemia_weight = csv.writer(open(location+"/weight/Septicemia_weight.csv", "wb"))
liver_weight = csv.writer(open(location+"/weight/Liver_weight.csv", "wb"))
hyper_weight = csv.writer(open(location+"/weight/Hyper_weight.csv", "wb"))
parkinson_weight = csv.writer(open(location+"/weight/Parkinson_weight.csv", "wb"))

Heart = open(location+'/degree/01-heart.txt', 'w')
Cancer = open(location+'/degree/02-cancer.txt', 'w')
Clrd = open(location+'/degree/03-clrd.txt', 'w')
Stroke = open(location+'/degree/04-stroke.txt', 'w')
Alzheimer = open(location+'/degree/05-alzheimer.txt', 'w')
Diabetes = open(location+'/degree/06-diabetes.txt', 'w')
Flupne = open(location+'/degree/07-flupne.txt', 'w')
Kidney = open(location+'/degree/08-kidney.txt', 'w')
Septicemia = open(location+'/degree/09-septicemia.txt', 'w')
Liver = open(location+'/degree/10-liver.txt', 'w')
Hyper = open(location+'/degree/11-hyper.txt', 'w')
Parkinson = open(location+'/degree/12-parkinson.txt', 'w')

put_into_Graph(weight_heart, maxB_heart, from_X_heart, to_y_heart, 'Heart', Heart, heart_weight)
print "finish Heart"
put_into_Graph(weight_cancer, maxB_cancer, from_X_cancer, to_y_cancer, 'Cancer', Cancer, cancer_weight)
print "finish Cancer"
put_into_Graph(weight_clrd, maxB_clrd, from_X_clrd, to_y_clrd, 'Clrd', Clrd, clrd_weight)
print "finish Clrd"
put_into_Graph(weight_stroke, maxB_stroke, from_X_stroke, to_y_stroke, 'Stroke', Stroke, stroke_weight)
print "finish Stroke"
put_into_Graph(weight_alzheimer, maxB_alzheimer, from_X_alzheimer, to_y_alzheimer, 'Alzheimer', Alzheimer, alzheimer_weight)
print "finish Alzheimer"
put_into_Graph(weight_diabetes, maxB_diabetes, from_X_diabetes, to_y_diabetes, 'Diabetes', Diabetes, diabetes_weight)
print "finish Diabetes"
put_into_Graph(weight_flupne, maxB_flupne, from_X_flupne, to_y_flupne, 'Flupne', Flupne, flupne_weight)
print "finish Flupne"
put_into_Graph(weight_kidney, maxB_kidney, from_X_kidney, to_y_kidney, 'Kidney', Kidney, kidney_weight)
print "finish Kidney"
put_into_Graph(weight_septicemia, maxB_septicemia, from_X_septicemia, to_y_septicemia, 'Septicemia', Septicemia, septicemia_weight)
print "finish Septicemia"
put_into_Graph(weight_liver, maxB_liver, from_X_liver, to_y_liver, 'Liver', Liver, liver_weight)
print "finish Liver"
put_into_Graph(weight_hyper, maxB_hyper, from_X_hyper, to_y_hyper, 'Hyper', Hyper, hyper_weight)
print "finish Hyper"
put_into_Graph(weight_parkinson, maxB_parkinson, from_X_parkinson, to_y_parkinson, 'Parkinson', Parkinson, parkinson_weight)
print "finish Parkinson"



###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################



db = sqlite3.connect(SSS)
c = db.cursor()

location = '/Users/Abduljaleel/Desktop/project/'+SSS+'/6h'

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

def Bigloop(g_i,BigArray):
    weightt = []
    from_X = []
    to_y = []
    maxB = BigArray[0][0]
    for x in range(0, g_i-1):
        for y in range(0, g_i-1):
            if BigArray[x][y] != 0:
                if BigArray[x][y] > maxB:
                    maxB = BigArray[x][y]
                weightt.append(BigArray[x][y])
                from_X.append(x)
                to_y.append(y)
            print str(x)+'    &    '+str(y)
    return (weightt,from_X,to_y,maxB)

def fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson):
    weight_heart = []
    weight_cancer = []
    weight_clrd = []
    weight_stroke = []
    weight_alzheimer = []
    weight_diabetes = []
    weight_flupne = []
    weight_kidney = []
    weight_septicemia = []
    weight_liver = []
    weight_hyper = []
    weight_parkinson = []

    from_X_heart = []
    from_X_cancer = []
    from_X_clrd = []
    from_X_stroke = []
    from_X_alzheimer = []
    from_X_diabetes = []
    from_X_flupne = []
    from_X_kidney = []
    from_X_septicemia = []
    from_X_liver = []
    from_X_hyper = []
    from_X_parkinson = []

    to_y_heart = []
    to_y_cancer = []
    to_y_clrd = []
    to_y_stroke = []
    to_y_alzheimer = []
    to_y_diabetes = []
    to_y_flupne = []
    to_y_kidney = []
    to_y_septicemia = []
    to_y_liver = []
    to_y_hyper = []
    to_y_parkinson = []

    maxB_heart = BigArray_heart[0][0]
    maxB_cancer = BigArray_cancer[0][0]
    maxB_clrd = BigArray_clrd[0][0]
    maxB_stroke = BigArray_stroke[0][0]
    maxB_alzheimer = BigArray_alzheimer[0][0]
    maxB_diabetes = BigArray_diabetes[0][0]
    maxB_flupne = BigArray_flupne[0][0]
    maxB_kidney = BigArray_kidney[0][0]
    maxB_septicemia = BigArray_septicemia[0][0]
    maxB_liver = BigArray_liver[0][0]
    maxB_hyper = BigArray_hyper[0][0]
    maxB_parkinson = BigArray_parkinson[0][0]


    for x in range(0, g_id-1):
        for y in range(0, g_id-1):

            if BigArray_heart[x][y] != 0:
                if BigArray_heart[x][y] > maxB_heart:
                    maxB_heart = BigArray_heart[x][y]
                weight_heart.append(BigArray_heart[x][y])
                from_X_heart.append(x)
                to_y_heart.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_cancer[x][y] != 0:
                if BigArray_cancer[x][y] > maxB_cancer:
                    maxB_cancer = BigArray_cancer[x][y]
                weight_cancer.append(BigArray_cancer[x][y])
                from_X_cancer.append(x)
                to_y_cancer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_clrd[x][y] != 0:
                if BigArray_clrd[x][y] > maxB_clrd:
                    maxB_clrd = BigArray_clrd[x][y]
                weight_clrd.append(BigArray_clrd[x][y])
                from_X_clrd.append(x)
                to_y_clrd.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_stroke[x][y] != 0:
                if BigArray_stroke[x][y] > maxB_stroke:
                    maxB_stroke = BigArray_stroke[x][y]
                weight_stroke.append(BigArray_stroke[x][y])
                from_X_stroke.append(x)
                to_y_stroke.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_alzheimer[x][y] != 0:
                if BigArray_alzheimer[x][y] > maxB_alzheimer:
                    maxB_alzheimer = BigArray_alzheimer[x][y]
                weight_alzheimer.append(BigArray_alzheimer[x][y])
                from_X_alzheimer.append(x)
                to_y_alzheimer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_diabetes[x][y] != 0:
                if BigArray_diabetes[x][y] > maxB_diabetes:
                    maxB_diabetes = BigArray_diabetes[x][y]
                weight_diabetes.append(BigArray_diabetes[x][y])
                from_X_diabetes.append(x)
                to_y_diabetes.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_flupne[x][y] != 0:
                if BigArray_flupne[x][y] > maxB_flupne:
                    maxB_flupne = BigArray_flupne[x][y]
                weight_flupne.append(BigArray_flupne[x][y])
                from_X_flupne.append(x)
                to_y_flupne.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_kidney[x][y] != 0:
                if BigArray_kidney[x][y] > maxB_kidney:
                    maxB_kidney = BigArray_kidney[x][y]
                weight_kidney.append(BigArray_kidney[x][y])
                from_X_kidney.append(x)
                to_y_kidney.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_septicemia[x][y] != 0:
                if BigArray_septicemia[x][y] > maxB_septicemia:
                    maxB_septicemia = BigArray_septicemia[x][y]
                weight_septicemia.append(BigArray_septicemia[x][y])
                from_X_septicemia.append(x)
                to_y_septicemia.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_liver[x][y] != 0:
                if BigArray_liver[x][y] > maxB_liver:
                    maxB_liver = BigArray_liver[x][y]
                weight_liver.append(BigArray_liver[x][y])
                from_X_liver.append(x)
                to_y_liver.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_hyper[x][y] != 0:
                if BigArray_hyper[x][y] > maxB_hyper:
                    maxB_hyper = BigArray_hyper[x][y]
                weight_hyper.append(BigArray_hyper[x][y])
                from_X_hyper.append(x)
                to_y_hyper.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_parkinson[x][y] != 0:
                if BigArray_parkinson[x][y] > maxB_parkinson:
                    maxB_parkinson = BigArray_parkinson[x][y]
                weight_parkinson.append(BigArray_parkinson[x][y])
                from_X_parkinson.append(x)
                to_y_parkinson.append(y)
            print str(x)+'    &    '+str(y)


    return (weight_heart,weight_cancer,weight_clrd,weight_stroke,weight_alzheimer,weight_diabetes,weight_flupne,weight_kidney,weight_septicemia,weight_liver,weight_hyper,weight_parkinson,
    from_X_heart,from_X_cancer,from_X_clrd,from_X_stroke,from_X_alzheimer,from_X_diabetes,from_X_flupne,from_X_kidney,from_X_septicemia,from_X_liver,from_X_hyper,from_X_parkinson,
    to_y_heart,to_y_cancer,to_y_clrd,to_y_stroke,to_y_alzheimer,to_y_diabetes,to_y_flupne,to_y_kidney,to_y_septicemia,to_y_liver,to_y_hyper,to_y_parkinson,
    maxB_heart,maxB_cancer,maxB_clrd,maxB_stroke,maxB_alzheimer,maxB_diabetes,maxB_flupne,maxB_kidney,maxB_septicemia,maxB_liver,maxB_hyper,maxB_parkinson)



heart_array = []
heart2_array = []
cancer_array = []
cancer2_array = []
clrd_array = []
clrd2_array = []
stroke_array = []
stroke2_array = []
alzheimer_array = []
alzheimer2_array = []
diabetes_array = []
diabetes2_array = []
flupne_array = []
flupne2_array = []
kidney_array = []
kidney2_array = []
septicemia_array = []
septicemia2_array = []
liver_array = []
liver2_array = []
hyper_array = []
hyper2_array = []
parkinson_array = []
parkinson2_array = []


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

    # cancer
    if ('cancer' in row[2]):
        cancer_array.append(g_id)
    else:
        cancer_array.append(0)

    # clrd
    if ('clrd' in row[2]):
        clrd_array.append(g_id)
    else:
        clrd_array.append(0)

    # stroke
    if ('stroke' in row[2]):
        stroke_array.append(g_id)
    else:
        stroke_array.append(0)

    # alzheimer
    if ('alzheimer' in row[2]):
        alzheimer_array.append(g_id)
    else:
        alzheimer_array.append(0)

    # diabetes
    if ('diabetes' in row[2]):
        diabetes_array.append(g_id)
    else:
        diabetes_array.append(0)

    # flu_or_pneumonia
    if ('flu_or_pneumonia' in row[2]):
        flupne_array.append(g_id)
    else:
        flupne_array.append(0)

    # kidney
    if ('kidney' in row[2]):
        kidney_array.append(g_id)
    else:
        kidney_array.append(0)

    # septicemia
    if ('septicemia' in row[2]):
        septicemia_array.append(g_id)
    else:
        septicemia_array.append(0)

    # liver
    if ('liver' in row[2]):
        liver_array.append(g_id)
    else:
        liver_array.append(0)

    # hyper
    if ('hyper' in row[2]):
        hyper_array.append(g_id)
    else:
        hyper_array.append(0)

    # parkinson
    if ('parkinson' in row[2]):
        parkinson_array.append(g_id)
    else:
        parkinson_array.append(0)

    g_id += 1
print 'finish LOOP ONE'

# BigArray_heart = [[0 for j in range(g_id)] for i in range(g_id)]
BigArray_heart = np.empty((g_id,g_id),dtype=np.int)
BigArray_cancer = np.empty((g_id,g_id),dtype=np.int)
BigArray_clrd = np.empty((g_id,g_id),dtype=np.int)
BigArray_stroke = np.empty((g_id,g_id),dtype=np.int)
BigArray_alzheimer = np.empty((g_id,g_id),dtype=np.int)
BigArray_diabetes = np.empty((g_id,g_id),dtype=np.int)
BigArray_flupne = np.empty((g_id,g_id),dtype=np.int)
BigArray_kidney = np.empty((g_id,g_id),dtype=np.int)
BigArray_septicemia = np.empty((g_id,g_id),dtype=np.int)
BigArray_liver = np.empty((g_id,g_id),dtype=np.int)
BigArray_hyper = np.empty((g_id,g_id),dtype=np.int)
BigArray_parkinson = np.empty((g_id,g_id),dtype=np.int)

# Defining a window of 3 hours
window = '000060000'
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
        loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
        cancer2_array = []
        loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
        clrd2_array = []
        loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
        stroke2_array = []
        loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
        alzheimer2_array = []
        loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
        diabetes2_array = []
        loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
        flupne2_array = []
        loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
        kidney2_array = []
        loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
        septicemia2_array = []
        loop(mn, mx, liver_array, liver2_array, BigArray_liver)
        liver2_array = []
        loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
        hyper2_array = []
        loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
        parkinson2_array = []

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
        # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        if (fff < LLL) and (fff > 0):

            loop(mn, mx, heart_array, heart2_array, BigArray_heart)
            heart2_array = []
            loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
            cancer2_array = []
            loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
            clrd2_array = []
            loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
            stroke2_array = []
            loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
            alzheimer2_array = []
            loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
            diabetes2_array = []
            loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
            flupne2_array = []
            loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
            kidney2_array = []
            loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
            septicemia2_array = []
            loop(mn, mx, liver_array, liver2_array, BigArray_liver)
            liver2_array = []
            loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
            hyper2_array = []
            loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
            parkinson2_array = []
            print str(mn)+'--->'+str(mx) +'  = ' +str(fff)
        # else:
            # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

    limit_1 = add_time(limit_1, in_case)
    limit_2 = add_time(limit_1, window)

    if limit_1 >= last_tweet_date:
        break


print "////////////////////////////////////////////////////////////////"

print 'enter Large Loop'


fibReturn = fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson)

weight_heart = fibReturn[0]
weight_cancer = fibReturn[1]
weight_clrd = fibReturn[2]
weight_stroke = fibReturn[3]
weight_alzheimer = fibReturn[4]
weight_diabetes = fibReturn[5]
weight_flupne = fibReturn[6]
weight_kidney = fibReturn[7]
weight_septicemia = fibReturn[8]
weight_liver = fibReturn[9]
weight_hyper = fibReturn[10]
weight_parkinson = fibReturn[11]


from_X_heart = fibReturn[12]
from_X_cancer = fibReturn[13]
from_X_clrd = fibReturn[14]
from_X_stroke = fibReturn[15]
from_X_alzheimer = fibReturn[16]
from_X_diabetes = fibReturn[17]
from_X_flupne = fibReturn[18]
from_X_kidney = fibReturn[19]
from_X_septicemia = fibReturn[20]
from_X_liver = fibReturn[21]
from_X_hyper = fibReturn[22]
from_X_parkinson = fibReturn[23]


to_y_heart = fibReturn[24]
to_y_cancer = fibReturn[25]
to_y_clrd = fibReturn[26]
to_y_stroke = fibReturn[27]
to_y_alzheimer = fibReturn[28]
to_y_diabetes = fibReturn[29]
to_y_flupne = fibReturn[30]
to_y_kidney = fibReturn[31]
to_y_septicemia = fibReturn[32]
to_y_liver = fibReturn[33]
to_y_hyper = fibReturn[34]
to_y_parkinson = fibReturn[35]


maxB_heart = fibReturn[36]
maxB_cancer = fibReturn[37]
maxB_clrd = fibReturn[38]
maxB_stroke = fibReturn[39]
maxB_alzheimer = fibReturn[40]
maxB_diabetes = fibReturn[41]
maxB_flupne = fibReturn[42]
maxB_kidney = fibReturn[43]
maxB_septicemia = fibReturn[44]
maxB_liver = fibReturn[45]
maxB_hyper = fibReturn[46]
maxB_parkinson = fibReturn[47]



print "////////////////////////////////////////////////////////////////"
print 'Finish i,j loops'
print "////////////////////////////////////////////////////////////////"

GI = nx.Graph()

heart_weight = csv.writer(open(location+"/weight/Heart_weight.csv", "wb"))
cancer_weight = csv.writer(open(location+"/weight/Cancer_weight.csv", "wb"))
clrd_weight = csv.writer(open(location+"/weight/Clrd_weight.csv", "wb"))
stroke_weight = csv.writer(open(location+"/weight/Stroke_weight.csv", "wb"))
alzheimer_weight = csv.writer(open(location+"/weight/Alzheimer_weight.csv", "wb"))
diabetes_weight = csv.writer(open(location+"/weight/Diabetes_weight.csv", "wb"))
flupne_weight = csv.writer(open(location+"/weight/Flupne_weight.csv", "wb"))
kidney_weight = csv.writer(open(location+"/weight/Kidney_weight.csv", "wb"))
septicemia_weight = csv.writer(open(location+"/weight/Septicemia_weight.csv", "wb"))
liver_weight = csv.writer(open(location+"/weight/Liver_weight.csv", "wb"))
hyper_weight = csv.writer(open(location+"/weight/Hyper_weight.csv", "wb"))
parkinson_weight = csv.writer(open(location+"/weight/Parkinson_weight.csv", "wb"))

Heart = open(location+'/degree/01-heart.txt', 'w')
Cancer = open(location+'/degree/02-cancer.txt', 'w')
Clrd = open(location+'/degree/03-clrd.txt', 'w')
Stroke = open(location+'/degree/04-stroke.txt', 'w')
Alzheimer = open(location+'/degree/05-alzheimer.txt', 'w')
Diabetes = open(location+'/degree/06-diabetes.txt', 'w')
Flupne = open(location+'/degree/07-flupne.txt', 'w')
Kidney = open(location+'/degree/08-kidney.txt', 'w')
Septicemia = open(location+'/degree/09-septicemia.txt', 'w')
Liver = open(location+'/degree/10-liver.txt', 'w')
Hyper = open(location+'/degree/11-hyper.txt', 'w')
Parkinson = open(location+'/degree/12-parkinson.txt', 'w')

put_into_Graph(weight_heart, maxB_heart, from_X_heart, to_y_heart, 'Heart', Heart, heart_weight)
print "finish Heart"
put_into_Graph(weight_cancer, maxB_cancer, from_X_cancer, to_y_cancer, 'Cancer', Cancer, cancer_weight)
print "finish Cancer"
put_into_Graph(weight_clrd, maxB_clrd, from_X_clrd, to_y_clrd, 'Clrd', Clrd, clrd_weight)
print "finish Clrd"
put_into_Graph(weight_stroke, maxB_stroke, from_X_stroke, to_y_stroke, 'Stroke', Stroke, stroke_weight)
print "finish Stroke"
put_into_Graph(weight_alzheimer, maxB_alzheimer, from_X_alzheimer, to_y_alzheimer, 'Alzheimer', Alzheimer, alzheimer_weight)
print "finish Alzheimer"
put_into_Graph(weight_diabetes, maxB_diabetes, from_X_diabetes, to_y_diabetes, 'Diabetes', Diabetes, diabetes_weight)
print "finish Diabetes"
put_into_Graph(weight_flupne, maxB_flupne, from_X_flupne, to_y_flupne, 'Flupne', Flupne, flupne_weight)
print "finish Flupne"
put_into_Graph(weight_kidney, maxB_kidney, from_X_kidney, to_y_kidney, 'Kidney', Kidney, kidney_weight)
print "finish Kidney"
put_into_Graph(weight_septicemia, maxB_septicemia, from_X_septicemia, to_y_septicemia, 'Septicemia', Septicemia, septicemia_weight)
print "finish Septicemia"
put_into_Graph(weight_liver, maxB_liver, from_X_liver, to_y_liver, 'Liver', Liver, liver_weight)
print "finish Liver"
put_into_Graph(weight_hyper, maxB_hyper, from_X_hyper, to_y_hyper, 'Hyper', Hyper, hyper_weight)
print "finish Hyper"
put_into_Graph(weight_parkinson, maxB_parkinson, from_X_parkinson, to_y_parkinson, 'Parkinson', Parkinson, parkinson_weight)
print "finish Parkinson"



###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################


db = sqlite3.connect(SSS)
c = db.cursor()

location = '/Users/Abduljaleel/Desktop/project/'+SSS+'/12h'

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

def Bigloop(g_i,BigArray):
    weightt = []
    from_X = []
    to_y = []
    maxB = BigArray[0][0]
    for x in range(0, g_i-1):
        for y in range(0, g_i-1):
            if BigArray[x][y] != 0:
                if BigArray[x][y] > maxB:
                    maxB = BigArray[x][y]
                weightt.append(BigArray[x][y])
                from_X.append(x)
                to_y.append(y)
            print str(x)+'    &    '+str(y)
    return (weightt,from_X,to_y,maxB)

def fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson):
    weight_heart = []
    weight_cancer = []
    weight_clrd = []
    weight_stroke = []
    weight_alzheimer = []
    weight_diabetes = []
    weight_flupne = []
    weight_kidney = []
    weight_septicemia = []
    weight_liver = []
    weight_hyper = []
    weight_parkinson = []

    from_X_heart = []
    from_X_cancer = []
    from_X_clrd = []
    from_X_stroke = []
    from_X_alzheimer = []
    from_X_diabetes = []
    from_X_flupne = []
    from_X_kidney = []
    from_X_septicemia = []
    from_X_liver = []
    from_X_hyper = []
    from_X_parkinson = []

    to_y_heart = []
    to_y_cancer = []
    to_y_clrd = []
    to_y_stroke = []
    to_y_alzheimer = []
    to_y_diabetes = []
    to_y_flupne = []
    to_y_kidney = []
    to_y_septicemia = []
    to_y_liver = []
    to_y_hyper = []
    to_y_parkinson = []

    maxB_heart = BigArray_heart[0][0]
    maxB_cancer = BigArray_cancer[0][0]
    maxB_clrd = BigArray_clrd[0][0]
    maxB_stroke = BigArray_stroke[0][0]
    maxB_alzheimer = BigArray_alzheimer[0][0]
    maxB_diabetes = BigArray_diabetes[0][0]
    maxB_flupne = BigArray_flupne[0][0]
    maxB_kidney = BigArray_kidney[0][0]
    maxB_septicemia = BigArray_septicemia[0][0]
    maxB_liver = BigArray_liver[0][0]
    maxB_hyper = BigArray_hyper[0][0]
    maxB_parkinson = BigArray_parkinson[0][0]


    for x in range(0, g_id-1):
        for y in range(0, g_id-1):

            if BigArray_heart[x][y] != 0:
                if BigArray_heart[x][y] > maxB_heart:
                    maxB_heart = BigArray_heart[x][y]
                weight_heart.append(BigArray_heart[x][y])
                from_X_heart.append(x)
                to_y_heart.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_cancer[x][y] != 0:
                if BigArray_cancer[x][y] > maxB_cancer:
                    maxB_cancer = BigArray_cancer[x][y]
                weight_cancer.append(BigArray_cancer[x][y])
                from_X_cancer.append(x)
                to_y_cancer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_clrd[x][y] != 0:
                if BigArray_clrd[x][y] > maxB_clrd:
                    maxB_clrd = BigArray_clrd[x][y]
                weight_clrd.append(BigArray_clrd[x][y])
                from_X_clrd.append(x)
                to_y_clrd.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_stroke[x][y] != 0:
                if BigArray_stroke[x][y] > maxB_stroke:
                    maxB_stroke = BigArray_stroke[x][y]
                weight_stroke.append(BigArray_stroke[x][y])
                from_X_stroke.append(x)
                to_y_stroke.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_alzheimer[x][y] != 0:
                if BigArray_alzheimer[x][y] > maxB_alzheimer:
                    maxB_alzheimer = BigArray_alzheimer[x][y]
                weight_alzheimer.append(BigArray_alzheimer[x][y])
                from_X_alzheimer.append(x)
                to_y_alzheimer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_diabetes[x][y] != 0:
                if BigArray_diabetes[x][y] > maxB_diabetes:
                    maxB_diabetes = BigArray_diabetes[x][y]
                weight_diabetes.append(BigArray_diabetes[x][y])
                from_X_diabetes.append(x)
                to_y_diabetes.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_flupne[x][y] != 0:
                if BigArray_flupne[x][y] > maxB_flupne:
                    maxB_flupne = BigArray_flupne[x][y]
                weight_flupne.append(BigArray_flupne[x][y])
                from_X_flupne.append(x)
                to_y_flupne.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_kidney[x][y] != 0:
                if BigArray_kidney[x][y] > maxB_kidney:
                    maxB_kidney = BigArray_kidney[x][y]
                weight_kidney.append(BigArray_kidney[x][y])
                from_X_kidney.append(x)
                to_y_kidney.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_septicemia[x][y] != 0:
                if BigArray_septicemia[x][y] > maxB_septicemia:
                    maxB_septicemia = BigArray_septicemia[x][y]
                weight_septicemia.append(BigArray_septicemia[x][y])
                from_X_septicemia.append(x)
                to_y_septicemia.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_liver[x][y] != 0:
                if BigArray_liver[x][y] > maxB_liver:
                    maxB_liver = BigArray_liver[x][y]
                weight_liver.append(BigArray_liver[x][y])
                from_X_liver.append(x)
                to_y_liver.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_hyper[x][y] != 0:
                if BigArray_hyper[x][y] > maxB_hyper:
                    maxB_hyper = BigArray_hyper[x][y]
                weight_hyper.append(BigArray_hyper[x][y])
                from_X_hyper.append(x)
                to_y_hyper.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_parkinson[x][y] != 0:
                if BigArray_parkinson[x][y] > maxB_parkinson:
                    maxB_parkinson = BigArray_parkinson[x][y]
                weight_parkinson.append(BigArray_parkinson[x][y])
                from_X_parkinson.append(x)
                to_y_parkinson.append(y)
            print str(x)+'    &    '+str(y)


    return (weight_heart,weight_cancer,weight_clrd,weight_stroke,weight_alzheimer,weight_diabetes,weight_flupne,weight_kidney,weight_septicemia,weight_liver,weight_hyper,weight_parkinson,
    from_X_heart,from_X_cancer,from_X_clrd,from_X_stroke,from_X_alzheimer,from_X_diabetes,from_X_flupne,from_X_kidney,from_X_septicemia,from_X_liver,from_X_hyper,from_X_parkinson,
    to_y_heart,to_y_cancer,to_y_clrd,to_y_stroke,to_y_alzheimer,to_y_diabetes,to_y_flupne,to_y_kidney,to_y_septicemia,to_y_liver,to_y_hyper,to_y_parkinson,
    maxB_heart,maxB_cancer,maxB_clrd,maxB_stroke,maxB_alzheimer,maxB_diabetes,maxB_flupne,maxB_kidney,maxB_septicemia,maxB_liver,maxB_hyper,maxB_parkinson)



heart_array = []
heart2_array = []
cancer_array = []
cancer2_array = []
clrd_array = []
clrd2_array = []
stroke_array = []
stroke2_array = []
alzheimer_array = []
alzheimer2_array = []
diabetes_array = []
diabetes2_array = []
flupne_array = []
flupne2_array = []
kidney_array = []
kidney2_array = []
septicemia_array = []
septicemia2_array = []
liver_array = []
liver2_array = []
hyper_array = []
hyper2_array = []
parkinson_array = []
parkinson2_array = []


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

    # cancer
    if ('cancer' in row[2]):
        cancer_array.append(g_id)
    else:
        cancer_array.append(0)

    # clrd
    if ('clrd' in row[2]):
        clrd_array.append(g_id)
    else:
        clrd_array.append(0)

    # stroke
    if ('stroke' in row[2]):
        stroke_array.append(g_id)
    else:
        stroke_array.append(0)

    # alzheimer
    if ('alzheimer' in row[2]):
        alzheimer_array.append(g_id)
    else:
        alzheimer_array.append(0)

    # diabetes
    if ('diabetes' in row[2]):
        diabetes_array.append(g_id)
    else:
        diabetes_array.append(0)

    # flu_or_pneumonia
    if ('flu_or_pneumonia' in row[2]):
        flupne_array.append(g_id)
    else:
        flupne_array.append(0)

    # kidney
    if ('kidney' in row[2]):
        kidney_array.append(g_id)
    else:
        kidney_array.append(0)

    # septicemia
    if ('septicemia' in row[2]):
        septicemia_array.append(g_id)
    else:
        septicemia_array.append(0)

    # liver
    if ('liver' in row[2]):
        liver_array.append(g_id)
    else:
        liver_array.append(0)

    # hyper
    if ('hyper' in row[2]):
        hyper_array.append(g_id)
    else:
        hyper_array.append(0)

    # parkinson
    if ('parkinson' in row[2]):
        parkinson_array.append(g_id)
    else:
        parkinson_array.append(0)

    g_id += 1
print 'finish LOOP ONE'

# BigArray_heart = [[0 for j in range(g_id)] for i in range(g_id)]
BigArray_heart = np.empty((g_id,g_id),dtype=np.int)
BigArray_cancer = np.empty((g_id,g_id),dtype=np.int)
BigArray_clrd = np.empty((g_id,g_id),dtype=np.int)
BigArray_stroke = np.empty((g_id,g_id),dtype=np.int)
BigArray_alzheimer = np.empty((g_id,g_id),dtype=np.int)
BigArray_diabetes = np.empty((g_id,g_id),dtype=np.int)
BigArray_flupne = np.empty((g_id,g_id),dtype=np.int)
BigArray_kidney = np.empty((g_id,g_id),dtype=np.int)
BigArray_septicemia = np.empty((g_id,g_id),dtype=np.int)
BigArray_liver = np.empty((g_id,g_id),dtype=np.int)
BigArray_hyper = np.empty((g_id,g_id),dtype=np.int)
BigArray_parkinson = np.empty((g_id,g_id),dtype=np.int)

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
        loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
        cancer2_array = []
        loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
        clrd2_array = []
        loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
        stroke2_array = []
        loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
        alzheimer2_array = []
        loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
        diabetes2_array = []
        loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
        flupne2_array = []
        loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
        kidney2_array = []
        loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
        septicemia2_array = []
        loop(mn, mx, liver_array, liver2_array, BigArray_liver)
        liver2_array = []
        loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
        hyper2_array = []
        loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
        parkinson2_array = []

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
        # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

        if (fff < LLL) and (fff > 0):

            loop(mn, mx, heart_array, heart2_array, BigArray_heart)
            heart2_array = []
            loop(mn, mx, cancer_array, cancer2_array, BigArray_cancer)
            cancer2_array = []
            loop(mn, mx, clrd_array, clrd2_array, BigArray_clrd)
            clrd2_array = []
            loop(mn, mx, stroke_array, stroke2_array, BigArray_stroke)
            stroke2_array = []
            loop(mn, mx, alzheimer_array, alzheimer2_array, BigArray_alzheimer)
            alzheimer2_array = []
            loop(mn, mx, diabetes_array, diabetes2_array, BigArray_diabetes)
            diabetes2_array = []
            loop(mn, mx, flupne_array, flupne2_array, BigArray_flupne)
            flupne2_array = []
            loop(mn, mx, kidney_array, kidney2_array, BigArray_kidney)
            kidney2_array = []
            loop(mn, mx, septicemia_array, septicemia2_array, BigArray_septicemia)
            septicemia2_array = []
            loop(mn, mx, liver_array, liver2_array, BigArray_liver)
            liver2_array = []
            loop(mn, mx, hyper_array, hyper2_array, BigArray_hyper)
            hyper2_array = []
            loop(mn, mx, parkinson_array, parkinson2_array, BigArray_parkinson)
            parkinson2_array = []
            print str(mn)+'--->'+str(mx) +'  = ' +str(fff)
        # else:
            # print str(mn)+'--->'+str(mx) +'  = ' +str(fff)

    limit_1 = add_time(limit_1, in_case)
    limit_2 = add_time(limit_1, window)

    if limit_1 >= last_tweet_date:
        break


print "////////////////////////////////////////////////////////////////"

print 'enter Large Loop'


fibReturn = fibloop(g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson)

weight_heart = fibReturn[0]
weight_cancer = fibReturn[1]
weight_clrd = fibReturn[2]
weight_stroke = fibReturn[3]
weight_alzheimer = fibReturn[4]
weight_diabetes = fibReturn[5]
weight_flupne = fibReturn[6]
weight_kidney = fibReturn[7]
weight_septicemia = fibReturn[8]
weight_liver = fibReturn[9]
weight_hyper = fibReturn[10]
weight_parkinson = fibReturn[11]


from_X_heart = fibReturn[12]
from_X_cancer = fibReturn[13]
from_X_clrd = fibReturn[14]
from_X_stroke = fibReturn[15]
from_X_alzheimer = fibReturn[16]
from_X_diabetes = fibReturn[17]
from_X_flupne = fibReturn[18]
from_X_kidney = fibReturn[19]
from_X_septicemia = fibReturn[20]
from_X_liver = fibReturn[21]
from_X_hyper = fibReturn[22]
from_X_parkinson = fibReturn[23]


to_y_heart = fibReturn[24]
to_y_cancer = fibReturn[25]
to_y_clrd = fibReturn[26]
to_y_stroke = fibReturn[27]
to_y_alzheimer = fibReturn[28]
to_y_diabetes = fibReturn[29]
to_y_flupne = fibReturn[30]
to_y_kidney = fibReturn[31]
to_y_septicemia = fibReturn[32]
to_y_liver = fibReturn[33]
to_y_hyper = fibReturn[34]
to_y_parkinson = fibReturn[35]


maxB_heart = fibReturn[36]
maxB_cancer = fibReturn[37]
maxB_clrd = fibReturn[38]
maxB_stroke = fibReturn[39]
maxB_alzheimer = fibReturn[40]
maxB_diabetes = fibReturn[41]
maxB_flupne = fibReturn[42]
maxB_kidney = fibReturn[43]
maxB_septicemia = fibReturn[44]
maxB_liver = fibReturn[45]
maxB_hyper = fibReturn[46]
maxB_parkinson = fibReturn[47]



print "////////////////////////////////////////////////////////////////"
print 'Finish i,j loops'
print "////////////////////////////////////////////////////////////////"

GI = nx.Graph()

heart_weight = csv.writer(open(location+"/weight/Heart_weight.csv", "wb"))
cancer_weight = csv.writer(open(location+"/weight/Cancer_weight.csv", "wb"))
clrd_weight = csv.writer(open(location+"/weight/Clrd_weight.csv", "wb"))
stroke_weight = csv.writer(open(location+"/weight/Stroke_weight.csv", "wb"))
alzheimer_weight = csv.writer(open(location+"/weight/Alzheimer_weight.csv", "wb"))
diabetes_weight = csv.writer(open(location+"/weight/Diabetes_weight.csv", "wb"))
flupne_weight = csv.writer(open(location+"/weight/Flupne_weight.csv", "wb"))
kidney_weight = csv.writer(open(location+"/weight/Kidney_weight.csv", "wb"))
septicemia_weight = csv.writer(open(location+"/weight/Septicemia_weight.csv", "wb"))
liver_weight = csv.writer(open(location+"/weight/Liver_weight.csv", "wb"))
hyper_weight = csv.writer(open(location+"/weight/Hyper_weight.csv", "wb"))
parkinson_weight = csv.writer(open(location+"/weight/Parkinson_weight.csv", "wb"))

Heart = open(location+'/degree/01-heart.txt', 'w')
Cancer = open(location+'/degree/02-cancer.txt', 'w')
Clrd = open(location+'/degree/03-clrd.txt', 'w')
Stroke = open(location+'/degree/04-stroke.txt', 'w')
Alzheimer = open(location+'/degree/05-alzheimer.txt', 'w')
Diabetes = open(location+'/degree/06-diabetes.txt', 'w')
Flupne = open(location+'/degree/07-flupne.txt', 'w')
Kidney = open(location+'/degree/08-kidney.txt', 'w')
Septicemia = open(location+'/degree/09-septicemia.txt', 'w')
Liver = open(location+'/degree/10-liver.txt', 'w')
Hyper = open(location+'/degree/11-hyper.txt', 'w')
Parkinson = open(location+'/degree/12-parkinson.txt', 'w')

put_into_Graph(weight_heart, maxB_heart, from_X_heart, to_y_heart, 'Heart', Heart, heart_weight)
print "finish Heart"
put_into_Graph(weight_cancer, maxB_cancer, from_X_cancer, to_y_cancer, 'Cancer', Cancer, cancer_weight)
print "finish Cancer"
put_into_Graph(weight_clrd, maxB_clrd, from_X_clrd, to_y_clrd, 'Clrd', Clrd, clrd_weight)
print "finish Clrd"
put_into_Graph(weight_stroke, maxB_stroke, from_X_stroke, to_y_stroke, 'Stroke', Stroke, stroke_weight)
print "finish Stroke"
put_into_Graph(weight_alzheimer, maxB_alzheimer, from_X_alzheimer, to_y_alzheimer, 'Alzheimer', Alzheimer, alzheimer_weight)
print "finish Alzheimer"
put_into_Graph(weight_diabetes, maxB_diabetes, from_X_diabetes, to_y_diabetes, 'Diabetes', Diabetes, diabetes_weight)
print "finish Diabetes"
put_into_Graph(weight_flupne, maxB_flupne, from_X_flupne, to_y_flupne, 'Flupne', Flupne, flupne_weight)
print "finish Flupne"
put_into_Graph(weight_kidney, maxB_kidney, from_X_kidney, to_y_kidney, 'Kidney', Kidney, kidney_weight)
print "finish Kidney"
put_into_Graph(weight_septicemia, maxB_septicemia, from_X_septicemia, to_y_septicemia, 'Septicemia', Septicemia, septicemia_weight)
print "finish Septicemia"
put_into_Graph(weight_liver, maxB_liver, from_X_liver, to_y_liver, 'Liver', Liver, liver_weight)
print "finish Liver"
put_into_Graph(weight_hyper, maxB_hyper, from_X_hyper, to_y_hyper, 'Hyper', Hyper, hyper_weight)
print "finish Hyper"
put_into_Graph(weight_parkinson, maxB_parkinson, from_X_parkinson, to_y_parkinson, 'Parkinson', Parkinson, parkinson_weight)
print "finish Parkinson"



###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################
###################