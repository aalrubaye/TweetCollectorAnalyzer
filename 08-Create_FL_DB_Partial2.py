__author__ = 'Abduljaleel'

from pymongo import *
from db_sqlite3 import sqlite3

#connecting to FL MongoDB
connection = Connection()
dbf = connection.florida
t_uf = dbf.fl
tw = t_uf.find()

db = sqlite3.connect('FLdb_Partial10_penumonitis')
c = db.cursor()

def is_penumonitis(txt):
    if ("aspiration pneumonia" in txt) or ("pulmonary aspiration" in txt) or ("inhalation pneumonia" in txt) or ("endotracheal aspiration" in txt):
        return True
    else:
        return False

def distext(tweet):
    txt = ''
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
