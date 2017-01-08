__author__ = 'Abduljaleel'
import os, sys
from pymongo import *
from db_sqlite3 import sqlite3


#connecting to FL MongoDB
connection = Connection()
dbf = connection.twit_usa


def is_heart(txt):
    if ("heart disease" in txt) or ("diseases of heart" in txt) or ("coronary artery" in txt) or \
            ("heart failure" in txt) or ("heart attack" in txt) or ("acute coronary" in txt) or ("angina" in txt) or \
            ("atrial fib" in txt) or ("arrhythmias" in txt) or ("atherosclerotic cardiovascular" in txt) or \
            ("congenital heart" in txt) or ("peripheral arterial disease" in txt) or ("pericardial" in txt) or \
            ("myocardial infarction" in txt) or ("endocarditis" in txt) or ("pericardium" in txt) or \
            ("myocarditis" in txt) or ("cardiac arrest" in txt) or ("congestive heart" in txt) or \
            ("heart block" in txt) or ("chd" in txt) or ("ihd" in txt) or ("cad" in txt):
                return True
    else:
        return False

def is_cancer(txt):
    if ("malignant" in txt) or ("cancer" in txt) or ("tumor" in txt) or ("malignancy" in txt):
        return True
    else:
        return False

def is_clrd(txt):
    if ("lower respiratory" in txt) or ("chronic obstructive pulmonary" in txt) or ("copd" in txt) or \
            ("asthma" in txt) or ("bronchitis" in txt) or ("emphysema" in txt):
                return True
    else:
        return False

def is_stroke(txt):
    if ("stroke" in txt) or ("brain attack" in txt) or ("cerebrovascular" in txt):
        return True
    else:
        return False

def is_alzheimer(txt):
    if ("alzheimer" in txt):
        return True
    else:
        return False

def is_diabetes(txt):
    if ("diabetes" in txt) or ("diabetic" in txt):
        return True
    else:
        return False

def is_flu_or_pneumonia(txt):
    if ("influenza" in txt) or ("pneumonia" in txt) or ("flu" in txt) or ("h1n1" in txt) or ("h5n1" in txt):
        return True
    else:
        return False

def is_kidney(txt):
    if ("nephritis" in txt) or ("nephrotic" in txt) or ("nephrosis" in txt) or ("nephritic" in txt) or \
            ("renal failure" in txt) or ("kidney disorder" in txt) or ("disorders of kidney" in txt) or \
            ("kidney failure" in txt) or ("kidney disease" in txt) or ("esrd" in txt) or \
            ("end stage renal" in txt) or ("dialysis" in txt):
                return True
    else:
        return False

def is_septicemia(txt):
    if ("septicemia" in txt) or ("blood poisoning" in txt) or ("bacteraemia" in txt) or \
            ("bacteremia" in txt) or ("sepsis" in txt):
                return True
    else:
        return False

def is_liver(txt):
    if ("chronic liver" in txt) or ("liver disease" in txt) or ("cirrhosis" in txt) or ("liver cirrhosis" in txt):
                return True
    else:
        return False

def is_hyper(txt):
    if ("hypertension" in txt) or ("hypertensive" in txt) or ("blood pressure" in txt):
        return True
    else:
        return False

def is_parkinson(txt):
    if ("parkinson" in txt) or ("paralysis agitans" in txt) or ("shaking palsy" in txt):
        return True
    else:
        return False

def is_penumonitis(txt):
    if ("aspiration pneumonia" in txt) or ("pulmonary aspiration" in txt) or ("inhalation pneumonia" in txt) or ("endotracheal aspiration" in txt):
        return True
    else:
        return False

def distext(tweet):
    txt = ''
    if (is_heart(tweet)):
        txt += "heart "
    if (is_cancer(tweet)):
        txt += "cancer "
    if (is_clrd(tweet)):
        txt += "clrd "
    if (is_stroke(tweet)):
        txt += "stroke "
    if (is_alzheimer(tweet)):
        txt += "alzheimer "
    if (is_diabetes(tweet)):
        txt += "diabetes "
    if (is_flu_or_pneumonia(tweet)):
        txt += "flu_or_pneumonia "
    if (is_kidney(tweet)):
        txt += "kidney "
    if (is_septicemia(tweet)):
        txt += "septicemia "
    if (is_liver(tweet)):
        txt += "liver "
    if (is_hyper(tweet)):
        txt += "hyper "
    if (is_parkinson(tweet)):
        txt += "parkinson "
    if (is_penumonitis(tweet)):
        txt += "penumonitis "
    return txt

def disdate(d):
    if d[4:7]=='Feb':
        m = str(2)
    elif d[4:7]=='Mar':
        m = str(3)
    else:
        m = str(4)

    day = int(m+str(d[8:10])+str(d[11:13])+str(d[14:16])+str(d[17:19]))
    return day

def do(sss):
    t_uf = dbf.tu
    tw = t_uf.find()


    SSS = sss

    location = '/Users/Abduljaleel/Desktop/project/'+SSS+'/SQLite/'

    heart = "heart"
    cancer = "cancer"
    clrd = "clrd"
    stroke = "stroke"
    alz = "alzheimer"
    diabetes = "diabetes"
    flupne = "flu_or_pneumonia"
    kidney = "kidney"
    septicemia = "septicemia"
    liver = "liver"
    hyper = "hyper"
    parkinson = "parkinson"

    db1 = sqlite3.connect(location+SSS+'_'+heart)
    c1 = db1.cursor()

    db2 = sqlite3.connect(location+SSS+'_'+cancer)
    c2 = db2.cursor()

    db3 = sqlite3.connect(location+SSS+'_'+clrd)
    c3 = db3.cursor()

    db4 = sqlite3.connect(location+SSS+'_'+stroke)
    c4 = db4.cursor()

    db5 = sqlite3.connect(location+SSS+'_'+alz)
    c5 = db5.cursor()

    db6 = sqlite3.connect(location+SSS+'_'+diabetes)
    c6 = db6.cursor()

    db7 = sqlite3.connect(location+SSS+'_'+flupne)
    c7 = db7.cursor()

    db8 = sqlite3.connect(location+SSS+'_'+kidney)
    c8 = db8.cursor()

    db9 = sqlite3.connect(location+SSS+'_'+septicemia)
    c9 = db9.cursor()

    db10 = sqlite3.connect(location+SSS+'_'+liver)
    c10 = db10.cursor()

    db11 = sqlite3.connect(location+SSS+'_'+hyper)
    c11 = db11.cursor()

    db12 = sqlite3.connect(location+SSS+'_'+parkinson)
    c12 = db12.cursor()

    sql = "CREATE TABLE NODES (ID INTEGER, USER TEXT,DISEASES TEXT, DATE INTEGER)"

    c1.execute("DROP TABLE IF EXISTS NODES")
    c1.execute(sql)

    c2.execute("DROP TABLE IF EXISTS NODES")
    c2.execute(sql)

    c3.execute("DROP TABLE IF EXISTS NODES")
    c3.execute(sql)

    c4.execute("DROP TABLE IF EXISTS NODES")
    c4.execute(sql)

    c5.execute("DROP TABLE IF EXISTS NODES")
    c5.execute(sql)

    c6.execute("DROP TABLE IF EXISTS NODES")
    c6.execute(sql)

    c7.execute("DROP TABLE IF EXISTS NODES")
    c7.execute(sql)

    c8.execute("DROP TABLE IF EXISTS NODES")
    c8.execute(sql)

    c9.execute("DROP TABLE IF EXISTS NODES")
    c9.execute(sql)

    c10.execute("DROP TABLE IF EXISTS NODES")
    c10.execute(sql)

    c11.execute("DROP TABLE IF EXISTS NODES")
    c11.execute(sql)

    c12.execute("DROP TABLE IF EXISTS NODES")
    c12.execute(sql)

    n=0
    n1=0; n2=0; n3=0; n4=0; n5=0; n6=0; n7=0; n8=0; n9=0; n10=0; n11=0; n12=0

    for row in tw:
        state = row['state'].strip()

        # if (state == SSS):
        user = row['data']['user']['screen_name']
        tt = row['data']['text'].lower()
        txt = distext(row['data']['text'].lower())
        date = disdate(row['data']['created_at'])
        if state != '':
            if (is_heart(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n1)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c1.execute(sql)
                    db1.commit()
                    n1 += 1
                except:
                    db1.rollback()

            if (is_cancer(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n2)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c2.execute(sql)
                    db2.commit()
                    n2 += 1
                except:
                    db2.rollback()


            if (is_clrd(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n3)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c3.execute(sql)
                    db3.commit()
                    n3 += 1
                except:
                    db3.rollback()

            if (is_stroke(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n4)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c4.execute(sql)
                    db4.commit()
                    n4 += 1
                except:
                    db4.rollback()

            if (is_alzheimer(txt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n5)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c5.execute(sql)
                    db5.commit()
                    n5 += 1
                except:
                    db5.rollback()

            if (is_diabetes(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n6)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c6.execute(sql)
                    db6.commit()
                    n6 += 1
                except:
                    db6.rollback()


            if (is_flu_or_pneumonia(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n7)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c7.execute(sql)
                    db7.commit()
                    n7 += 1
                except:
                    db7.rollback()

            if (is_kidney(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n8)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c8.execute(sql)
                    db8.commit()
                    n8 += 1
                except:
                    db8.rollback()

            if (is_septicemia(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n9)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c9.execute(sql)
                    db9.commit()
                    n9 += 1
                except:
                    db9.rollback()

            if (is_liver(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n10)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c10.execute(sql)
                    db10.commit()
                    n10 += 1
                except:
                    db10.rollback()


            if (is_hyper(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n11)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c11.execute(sql)
                    db11.commit()
                    n11 += 1
                except:
                    db11.rollback()

            if (is_parkinson(tt)):
                try:
                    sql = "INSERT INTO NODES VALUES ("+str(n12)+",'" + user + "','" + txt + "'," + str(date)+")"
                    c12.execute(sql)
                    db12.commit()
                    n12 += 1
                except:
                    db12.rollback()

            n+=1
            print n


    print "---------------------------------------------------------------------------"
    print str(n1) + "  " + heart
    print "---------------------------------------------------------------------------"
    print str(n2) + "  " + cancer
    print "---------------------------------------------------------------------------"
    print str(n3) + "  " + clrd
    print "---------------------------------------------------------------------------"
    print str(n4) + "  " + stroke
    print "---------------------------------------------------------------------------"
    print str(n5) + "  " + alz
    print "---------------------------------------------------------------------------"
    print str(n6) + "  " + diabetes
    print "---------------------------------------------------------------------------"
    print str(n7) + "  " + flupne
    print "---------------------------------------------------------------------------"
    print str(n8) + "  " + kidney
    print "---------------------------------------------------------------------------"
    print str(n9) + "  " + septicemia
    print "---------------------------------------------------------------------------"
    print str(n10) + "  " + liver
    print "---------------------------------------------------------------------------"
    print str(n11) + "  " + hyper
    print "---------------------------------------------------------------------------"
    print str(n12) + "  " + parkinson
    print "---------------------------------------------------------------------------"
#
#
# # do("California")
do("USA")



