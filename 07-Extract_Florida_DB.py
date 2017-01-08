__author__ = 'Abduljaleel'

from pymongo import *

#connecting to MongoDB 1 (THE MAIN DB - USA)
connection = Connection()
db = connection.twit_usa
t_u = db.tu
tw = t_u.find()
print tw.count()


t_1 = db.mississippi
t_2 = db.missouri
t_3 = db.montana
t_4 = db.nebraska
t_5 = db.nevada
t_6 = db.hampshire
t_7 = db.jersey
t_8 = db.mexico
t_9 = db.york
t_10 = db.ncarolina
t_11 = db.ndakota
t_12 = db.ohio
t_13 = db.oklahoma
t_14 = db.oregon
t_15 = db.penna
t_16 = db.rhodeisland
t_17 = db.scarolina
t_18 = db.sdakota
t_19 = db.tennessee
t_20 = db.texas
t_21 = db.utah
t_22 = db.vermont
t_23 = db.virginia
t_24 = db.washington
t_25 = db.wvirginia
t_26 = db.wisconsin
t_27 = db.wyoming
t_28 = db.dc



n=0
for row in tw:
    if row['state'] == "Mississippi":
        t_1.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Missouri":
        t_2.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Montana":
        t_3.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Nebraska":
        t_4.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Nevada":
        t_5.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "New Hampshire":
        t_6.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "New Jersey":
        t_7.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "New Mexico":
        t_8.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "New York":
        t_9.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "North Carolina":
        t_10.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "North Dakota":
        t_11.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Ohio":
        t_12.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Oklahoma":
        t_13.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Oregon":
        t_14.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "penna":
        t_15.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Rhode Island":
        t_16.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "South Carolina":
        t_17.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "South Dakota":
        t_18.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Tennessee":
        t_19.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Texas":
        t_20.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Utah":
        t_21.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Vermont":
        t_22.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Virginia":
        t_23.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Washington":
        t_24.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "West Virginia":
        t_25.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Wisconsin":
        t_26.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "Wyoming":
        t_27.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    if row['state'] == "District of Columbia":
        t_28.insert({'city': row['city'], 'state': row['state'], 'data': row['data']})
    n+=1
    print n
