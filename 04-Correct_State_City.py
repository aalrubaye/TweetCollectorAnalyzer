__author__ = 'Abduljaleel'
from pymongo import *
from db_sqlite3 import sqlite3
import sys

reload(sys)
sys.setdefaultencoding("utf8")


#connecting to MongoDB 1 (THE MAIN DB - USA)
connection = Connection()
db = connection.twit_usa
t_u = db.tu
tw = t_u.find()
print tw.count()


# SQLite DB for matching loc and address
db_match = sqlite3.connect('matchdb')
c_m = db_match.cursor()

def abv_to_state(kk):
    kk = kk.lower()
    if kk == "al":
        return "Alabama"
    if kk == "ak":
        return "Alaska"
    if kk == "az":
        return "Arizona"
    if kk == "ar":
        return "Arkansas"
    if kk == "ca":
        return "California"
    if kk == "co":
        return "Colorado"
    if kk == "ct":
        return "Connecticut"
    if kk == "de":
        return "Delaware"
    if kk == "fl":
        return "Florida"
    if kk == "ga":
        return "Georgia"
    if kk == "hi":
        return "Hawaii"
    if kk == "id":
        return "Idaho"
    if kk == "il":
        return "Illinois"
    if kk == "in":
        return "Indiana"
    if kk == "ia":
        return "Iowa"
    if kk == "ks":
        return "Kansas"
    if kk == "ky":
        return "Kentucky"
    if kk == "la":
        return "Louisiana"
    if kk == "me":
        return "Maine"
    if kk == "md":
        return "Maryland"
    if kk == "ma":
        return "Massachusetts"
    if kk == "mi":
        return "Michigan"
    if kk == "mn":
        return "Minnesota"
    if kk == "ms":
        return "Mississippi"
    if kk == "mo":
        return "Missouri"
    if kk == "mt":
        return "Montana"
    if kk == "ne":
        return "Nebraska"
    if kk == "nv":
        return "Nevada"
    if kk == "nh":
        return "New Hampshire"
    if kk == "nj":
        return "New Jersey"
    if kk == "nm":
        return "New Mexico"
    if kk == "ny":
        return "New York"
    if kk == "nc":
        return "North Carolina"
    if kk == "nd":
        return "North Dakota"
    if kk == "oh":
        return "Ohio"
    if kk == "ok":
        return "Oklahoma"
    if kk == "or":
        return "Oregon"
    if kk == "pa":
        return "penna"
    if kk == "ri":
        return "Rhode Island"
    if kk == "sc":
        return "South Carolina"
    if kk == "sd":
        return "South Dakota"
    if kk == "tn":
        return "Tennessee"
    if kk == "tx":
        return "Texas"
    if kk == "ut":
        return "Utah"
    if kk == "vt":
        return "Vermont"
    if kk == "va":
        return "Virginia"
    if kk == "wa":
        return "Washington"
    if kk == "wv":
        return "West Virginia"
    if kk == "wi":
        return "Wisconsin"
    if kk == "wy":
        return "Wyoming"
    if kk == "dc":
        return "District of Columbia"
    else:
        return kk

def pars_address(usadd):

    spli = usadd.split(',')
    g_len = len(spli)

    state = ''
    city = ''
    if spli[g_len-1] == " United States of America":
        for x in range(0,g_len-1):
            if spli[x].lower().strip() == 'washington':
                if spli[x+1].strip() == 'District of Columbia':
                    state = 'District of Columbia'
                    city = 'Washington'
                else:
                    state = spli[x]
                    if (x!=0):
                        if 'County' in spli[x-1]:
                            if (x-1!=0):
                                city = spli[x-2]
                                break
                        else:
                            city = spli[x-1]
                            break

    ddd = [city,state]
    return ddd

def check_s(s):
    slen = len(s)
    if slen == 2:
        s = abv_to_state(s)
        return s
    else:
        if s.lower() == 'pennsylvania' or s.lower() == 'penna':
            s = 'penna'
            return s
        elif s.lower() == 'd.c.' or s.lower() == 'd.c' == 'district of columbia':
            s = 'District of Columbia'
            return s
        return s

def check_c(c):
        if c.lower() == 'new york' or c.lower() == 'nyc':
            c = 'NYC'
            return c
        elif c.lower() == 'sf':
            c = 'SF'
            return c
        elif c.lower() == 'pgh':
            c = 'PGH'
            return c
        elif c.lower() == 'la' or c.lower() == 'los angeles':
            c = 'LA'
            return c
        elif c.lower() == 'usa':
            c = ''
            return c
        return c

def find_in_match(loc_find):
    uu = ''
    sql = "SELECT * FROM MATCH WHERE LOC = '"+str(loc_find)+"'"
    try:
        c_m.execute(sql)
        db_match.commit()
    except:
        db_match.rollback()

    results = c_m.fetchall()
    for res in results:
        uu = res[1]
    return uu


# Correcting data

n=0
for row in tw:
    # c = row['city'].strip().title()
    # s = row['state'].strip().title()
    c = row['city']
    s = row['state']
    # if s.lower() == "new mexico":
    #     print 'n'
    if s.lower() == 'cali':
        s = 'California'
        db.tu.update(
            { '_id': row['_id'] },
            {
                 '_id': row['_id'],
                 'city': c,
                 'state': s,
                 'data': row['data']
            }
        )
        print 'Cal'
    if s.lower() == 'mass':
        s = 'Massachusetts'
        db.tu.update(
            { '_id': row['_id'] },
            {
                 '_id': row['_id'],
                 'city': c,
                 'state': s,
                 'data': row['data']
            }
        )
        print 'Mas'
    # if s.lower() == 'd.c':
    #     s = 'District of Columbia'
    #     db.tu.update(
    #         { '_id': row['_id'] },
    #         {
    #              '_id': row['_id'],
    #              'city': c,
    #              'state': s,
    #              'data': row['data']
    #         }
    #     )
    #     print 'DC'

    # c = check_c(c)
    # s = check_s(s)
    # if s.lower().strip() == 'washington':
    #     g = ''
    #     g = find_in_match(row['data']['user']['location'])
    #     if g != '':
    #         ctst = pars_address(g)
    #         c = ctst[0].strip().title()
    #         s = ctst[1].strip().title()
    # if s=='District Of Columbia':
    #    s = 'District of Columbia'
    # db.tu.update(
    #     { '_id': row['_id'] },
    #     {
    #          '_id': row['_id'],
    #          'city': c,
    #          'state': s,
    #          'data': row['data']
    #     }
    # )
    # print n
    # n+=1
    # if n>100:
    #     break
