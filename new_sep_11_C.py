__author__ = 'Abduljaleel'
import igraph
from db_sqlite3 import sqlite3
import networkx as nx
import fib3
from time import gmtime, strftime

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
def build(Time,dis):


    location = '/Users/Abduljaleel/Desktop/project/USA/'+Time+'/'+dis+'/'


    db = '/Users/Abduljaleel/Desktop/project/USA/SQLite/USA_'+dis
    ddb = sqlite3.connect(db)

    cc = ddb.cursor()

    twit_line = []
    heart2_array = []

    cc.execute("SELECT * FROM NODES order by date")
    ddb.commit()
    results = cc.fetchall()
    all = len(results)

    window = '000010000'
    in_case ='000001500'
    limit_1 = firstdate(ddb,cc)
    window_time = add_time(limit_1, window)
    limit_2 = add_time(limit_1, in_case)
    last_tweet_date = lastdate(ddb,cc)


    tt1 = strftime("%a, %d %b %Y %X +0000", gmtime())

    while True:
        cc.execute("select * from nodes where date between " + str(limit_1) + " and " + str(limit_2) + " order by date")
        ddb.commit()
        rs = cc.fetchall()
        aa=[]
        for i in range (0,len(rs)):
            aa.append(rs[i][0])

        # for j in range (0,len(aa)):
        #     for jj in range (j+1,len(aa)):
        #         insert_edge(Net1,aa[j],aa[jj])
        #         # print str(aa[j])+','+str(aa[jj])

        fib3.loop(Net1,aa)

        limit_2 = add_time(limit_2, in_case)

        if limit_2 > window_time:
            break


    limit_1 = next_event(limit_1,ddb,cc)

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

        # for j in range (0,len(aa)):
        #     for jj in range (j+1,len(aa)):
        #         insert_edge(Net1,aa[j],aa[jj])
        #         # print str(aa[j])+','+str(aa[jj])

        fib3.loop(Net1,aa)

        limit_1 = add_time(limit_1, in_case)
        limit_2 = add_time(limit_1, window)

        if limit_1 >= last_tweet_date:
            break
    # print 'start creating'
    # nx.write_graphml(Net1, location+"Net1.graphml")
    print 'finish creating'
    # k =nx.read_graphml(location+"Net1.graphml")
    # # k = igraph.read(location+"test.graphml")


    # a = Net1.get_edgelist()

    # print k.edge[0][1]['weight']
    # c3=str(nx.average_clustering(Net1))

    X=[]
    Y=[]
    W=[]
    a = Net1.edges()

    fib3.app(X,Y,W,a,Net1)
    # for i in range (0,len(a)-1):
    #     x = a[i][0]
    #     y = a[i][1]
    #     w = Net1.edge[x][y]['weight']
    #     # print '('+str(x)+','+str(y)+','+str(w)+')'
    #     X.append(x)
    #     Y.append(y)
    #     W.append(w)

    # fib3.create(X,Y,W,Net2)
    mx = max(W)

    cc = open(location+'Net1.csv', 'a')
    print 'start writing to csv'
    for i in range(0, len(W)):
        norm = float(W[i])/mx
        if (norm >= 0.8):
            Net2.add_edge(str(X[i]),str(Y[i]))
            cc.write(str(X[i])+'\t'+str(Y[i])+'\n')
            print str(X[i])+','+str(Y[i])

    'finish writing to csv'

    print '------degree start'
    deg = open(location+'degree.txt', 'a')
    # st = open(location+'statistics.txt', 'a')
    # DD = open(location+'DD.txt', 'a')
    #
    # # Net22 = igraph.Graph(Net2)
    #
    # data = []


    for s in nx.degree(Net2):
        deg.write(str(nx.degree(Net2, s))+"\n")
    #     data.append(nx.degree(Net2, s))
    #     # deg.write(str(data[i])+'\n')
    #
    # for i in range (0,max(data)):
    #     j = i+1
    #     count = 0
    #     for k in range (0,len(data)):
    #         if data[k] == j:
    #             count +=1
    #     DD.write(str(j)+'\t'+str(count)+'\n')
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
    #
    # #
    # st.write('cluster  :'+str(cluster)+'\n')
    # st.write('path_Len :'+str(summ)+'\n')

    # nx.write_graphml(Net2, location+"Net2.graphml")
    # Net2.write_graphml(location+dis+"Net2.graphml")
    st = open(location+'log.txt', 'a')

    st.write(str(tt1)+'\n')
    st.write(str(strftime("%a, %d %b %Y %X +0000", gmtime()))+'\n')
    st.write(str('------------')+'\n')



Time = '1h'

# dis = 'heart'
# dis = 'cancer'
# dis = 'clrd'
# dis = 'stroke'
# dis = 'alzheimer'
# dis = 'diabetes'
# dis = 'flu_or_pneumonia'

build(Time,'clrd')
build(Time,'cancer')
build(Time,'clrd')
build(Time,'stroke')
build(Time,'alzheimer')
build(Time,'diabetes')
build(Time,'flu_or_pneumonia')
build(Time,'kidney')
build(Time,'septicemia')
build(Time,'liver')
build(Time,'hyper')
build(Time,'parkinson')