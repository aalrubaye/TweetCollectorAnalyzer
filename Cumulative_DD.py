__author__ = 'Abduljaleel'
import csv
import os, sys


states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '
STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

di = ["","heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]

def dd(SSS,dis,location):

    try:
        Degree = open(location+'/weighted_degree/'+dis+'_wd.txt', 'r')
    except:
        Degree = open(location+'/weighted_degree/'+dis+'_wd.txt', 'w')

    # try:
    #     Degree = open(location+'/degree/'+dis+'_degree.txt', 'r')
    # except:
    #     Degree = open(location+'/degree/'+dis+'_degree.txt', 'w')


    data = []
    try:
        for row in Degree:
            if row != '':
                data.append(int(row))
    except:
        print 'nothing'

    if len(data) == 0:
        return ([1],[0])

    DD = open(location+'/WDD/'+dis+'_wdd.txt', 'w')
    # DD = open(location+'/DegreeDistribution/'+dis+'_dd.txt', 'w')

    j_array = []
    count_array = []

    for i in range (0,max(data)):
        j = i+1

        count = 0
        for k in range (0,len(data)):
            if data[k] == j:
                count +=1
        DD.write(str(j)+'\t'+str(count)+'\n')
        j_array.append(j)
        count_array.append(count)
    return (j_array,count_array)

# this function should be optimized
def sm(c):
    su = []
    for i in range (0,len(c)):
        s =0
        for j in range (i,len(c)):
            s+=c[j]
        su.append(str(s))
    return su

def DD(SSS,dis):
    locc = '/Users/Abduljaleel/Desktop/project/'

    location1 = locc+SSS+'/1h'
    location2 = locc+SSS+'/2h'
    location3 = locc+SSS+'/3h'
    location4 = locc+SSS+'/4h'
    location5 = locc+SSS+'/5h'
    location6 = locc+SSS+'/6h'

    # p1 = locc+SSS+'/Cumulative_DD'
    #
    # try:
    #     os.stat(p1)
    #
    # except:
    #     os.mkdir(p1)


    e = dd(SSS,dis,location6)
    c0 = e[0]
    c6 = e[1]

    e = dd(SSS,dis,location1)
    k1 = e[0]
    c1 = e[1]

    e = dd(SSS,dis,location2)
    k2 = e[0]
    c2 = e[1]

    e = dd(SSS,dis,location3)
    k3 = e[0]
    c3 = e[1]

    e = dd(SSS,dis,location4)
    k4 = e[0]
    c4 = e[1]

    e = dd(SSS,dis,location5)
    k5 = e[0]
    c5 = e[1]

    path = locc+SSS+'/'

    s1 = sm(c1)
    # rrr = csv.writer(open(path+'wCDD_1_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_1_'+dis+'.txt', "w")
    rows = zip(k1,s1)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row[1])+'\n')
    for ii in range (len(s1)-1,len(c0)):
        s1.append('')


    s2 = sm(c2)
    # rrr = csv.writer(open(path+'wCDD_2_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_2_'+dis+'.txt', "w")
    rows = zip(k2,s2)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row)+'\n')
    for ii in range (len(s2)-1,len(c0)):
        s2.append('')


    s3 = sm(c3)
    # rrr = csv.writer(open(path+'wCDD_3_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_3_'+dis+'.txt', "w")

    rows = zip(k3,s3)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row)+'\n')
    for ii in range (len(s3)-1,len(c0)):
        s3.append('')


    s4 = sm(c4)
    # rrr = csv.writer(open(path+'wCDD_4_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_4_'+dis+'.txt', "w")

    rows = zip(k4,s4)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row)+'\n')
    for ii in range (len(s4)-1,len(c0)):
        s4.append('')


    s5 = sm(c5)
    # rrr = csv.writer(open(path+'wCDD_5_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_5_'+dis+'.txt', "w")

    rows = zip(k5,s5)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row)+'\n')
    for ii in range (len(s5)-1,len(c0)):
        s5.append('')


    s6 = sm(c6)
    # rrr = csv.writer(open(path+'wCDD_6_'+dis+'.csv', "wb"))
    rrr = open(path+'wCDD_6_'+dis+'.txt', "w")

    rows = zip(c0,s6)
    for row in rows:
        # rrr.writerow(row)
        rrr.write(str(row)+'\n')

    # rrr = csv.writer(open(path+'CWDD.csv', "wb"))
    # rrr = csv.writer(open(path+'WCDD.csv', "wb"))
    # # rrr.writerow(('k','1h','2h','3h','4h','5h','6h'))
    # rows = zip(c0,s1,s2,s3,s4,s5,s6)
    # for row in rows:
    #     # rrr.writerow(row)
    #     rrr.write(str(row)+'\n')
    # print SSS+' : '+dis




def extract_CDD(SSS):
    # DD(SSS,"heart")
    # DD(SSS,"cancer")
    # DD(SSS,"clrd")
    # DD(SSS,"stroke")
    # DD(SSS,"alzheimer")
    DD(SSS,"diabetes")
    # DD(SSS,"flu_or_pneumonia")
    # DD(SSS,"kidney")
    # DD(SSS,"septicemia")
    # DD(SSS,"liver")
    # DD(SSS,"hyper")
    # DD(SSS,"parkinson")

# for i in range (0,len(STATE)):
#     fff(STATE[i])

extract_CDD("Arizona")
