__author__ = 'Abduljaleel'

from pymongo import *
from db_sqlite3 import sqlite3

#connecting to FL MongoDB
connection = Connection()
dbf = connection.twit_usa
t_uf = dbf.tu
tw = t_uf.find()

db = sqlite3.connect('USA')
c = db.cursor()

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

def is_stroke(txt):
    if ("stroke" in txt) or ("brain attack" in txt) or ("cerebrovascular" in txt):
        return True
    else:
        return False

def is_diabetes(txt):
    if ("diabetes" in txt) or ("diabetic" in txt):
        return True
    else:
        return False

def is_hyper(txt):
    if ("hypertension" in txt) or ("hypertensive" in txt) or ("blood pressure" in txt):
        return True
    else:
        return False

def distext(tweet):
    txt = ''
    if (is_heart(tweet)):
        txt += "heart "
    if (is_stroke(tweet)):
        txt += "stroke "
    if (is_diabetes(tweet)):
        txt += "diabetes "
    if (is_hyper(tweet)):
        txt += "hyper "
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


c.execute("DROP TABLE IF EXISTS NODES")
sql = "CREATE TABLE NODES (ID INTEGER, USER TEXT,DISEASES TEXT, DATE INTEGER)"
c.execute(sql)

n = 0
for row in tw:
    user = row['data']['user']['screen_name']
    txt = distext(row['data']['text'].lower())
    date = disdate(row['data']['created_at'])
    if txt != '':
        try:
            sql = "INSERT INTO NODES VALUES ("+str(n)+",'" + user + "','" + txt + "'," + str(date)+")"
            c.execute(sql)
            db.commit()
            n += 1
            print n
        except:
            db.rollback()


print "---------------------------------------------------------------------------"
print str(n) + " elements are inserted into the db"
print "---------------------------------------------------------------------------"

#
# for row in tw:
#     print row['city'] + ' , ' + row['data']['user']['location']
#     # if row['city'].lower() == "Old Philadelphia Church Cemetery".lower() :
#     #     id = row['_id']
#     #     dbf.fl.remove( { '_id': id } )
#     #     print 'removed'
#     #
