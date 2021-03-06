__author__ = 'Abduljaleel'
import igraph
from db_sqlite3 import sqlite3
import networkx as nx
import fib3
import time

Net1 = nx.Graph()
Net2 = nx.Graph()

Net22 = igraph.Graph()

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
def insert_edge(N,x,y):
    try:
        w = N[x][y]['weight']
        w+=1
    except:
        w=1
    N.add_edge(x,y,weight= w)
    return w
def loop(N,aa,w):
    for j in range (0,len(aa)):
        for jj in range (j+1,len(aa)):
            wmax = insert_edge(N,aa[j],aa[jj])
            if w<wmax:
                w = wmax
    return w
def build(state,Time,dis,window,in_case):

    location = '/Users/Abduljaleel/Desktop/project/'+state+'/'+Time+'/'

    st = open(location+'log_where.txt', 'a')
    st.write(str(dis+'_'+Time)+'\n')
    db = '/Users/Abduljaleel/Desktop/project/'+state+'/SQLite/'+state+'_'+dis
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

    start = time.time()
    w=1
    if (all>=30):
        while True:
            cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
            ddb.commit()
            rs = cc.fetchall()
            aa=[]

            for i in range (0,len(rs)):
                aa.append(rs[i][0])


            # w = loop(Net1,aa,w)
            w = fib3.loop(Net1,aa,w)

            limit_2 = add_time(limit_2, in_case)

            if limit_2 > window_time:
                break
        limit_1 = next_event(limit_1,ddb,cc)

        w=1
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

            # w = loop(Net1,aa,w)
            w = fib3.loop(Net1,aa,w)

            limit_1 = add_time(limit_1, in_case)
            limit_2 = add_time(limit_1, window)

            if limit_1 >= last_tweet_date:
                break

        print 'finish creating'

        threshold = w*0.79
        H = nx.Graph([(u,v,d) for (u,v,d) in  Net1.edges_iter(data=True) if d['weight']>threshold])

        print '------degree start------'
        deg = open(location+'degree/'+dis+'_degree.txt', 'a')
        DD = open(location+'DegreeDistribution/'+dis+'_DD.txt', 'a')

        data = []
        DDD = H.degree()
        for s in DDD:
            deg.write(str(nx.degree(H, s))+"\n")
            data.append(nx.degree(H, s))

        for i in range (0,max(data)):
            j = i+1
            count = 0
            for k in range (0,len(data)):
                if data[k] == j:
                    count +=1
            DD.write(str(j)+'\t'+str(count)+'\n')
        print '------degree finsished------'

        # st = open(location+'statistics.txt', 'a')
        # print 'cluster start'
        # cluster = nx.average_clustering(Net2)
        # print 'pl start'
        # pl = Net22.average_path_length()
        # n=0
        # summ=0
        # for g in nx.connected_component_subgraphs(Net2):
        #     summ+=float(nx.average_shortest_path_length(g))
        #     n+=1
        # summ = float(summ)/n
        # st.write('cluster  :'+str(cluster)+'\n')
        # st.write('path_Len :'+str(summ)+'\n')

        print '------Writing Graphml start------'
        nx.write_graphml(H, location+'graph/'+dis+'_graph.graphml')

        sts = open(location+'log_sec.txt', 'a')
        end = time.time() - start
        sts.write(str(dis+'_'+Time)+'\t'+str(end)+'\n')

def window(state,h):
    Time = h+'h'
    w = '0000'+h+'0000'
    i = '000001000'
    build(state,Time,'heart',w,i)
    # build(state,Time,'cancer',w,i)
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
    window(state,'2')
    window(state,'3')
    window(state,'4')
    window(state,'5')
    window(state,'6')


state = 'Illinois'
do(state)
state = 'New York'
do(state)
state = 'Texas'
do(state)
# state = 'Oklahoma'
# do(state)
# state = 'Oregon'
# do(state)
# state = 'penna'
# do(state)
# state = 'Rhode Island'
# do(state)
# state = 'South Carolina'
# do(state)
# state = 'South Dakota'
# do(state)
# state = 'Tennessee'
# do(state)
# state = 'Utah'
# do(state)
# state = 'Vermont'
# do(state)
# state = 'Virginia'
# do(state)
# state = 'Washington'
# do(state)
# state = 'West Virginia'
# do(state)
# state = 'Wisconsin'
# do(state)
# state = 'Wyoming'
# do(state)
# state = 'District of Columbia'
# do(state)