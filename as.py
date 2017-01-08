__author__ = 'Abduljaleel'
import os, sys


states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '
STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

def do(state):
    path = '/Users/Abduljaleel/Desktop/project/degrees/'+state
    path1 = path+'/1h'
    path2 = path+'/2h'
    path3 = path+'/3h'
    path4 = path+'/4h'
    path5 = path+'/5h'
    path6 = path+'/6h'

    p11 = path1+'/degree'
    p12 = path1+'/weighted_degree'

    p21 = path2+'/degree'
    p22 = path2+'/weighted_degree'

    p31 = path3+'/degree'
    p32 = path3+'/weighted_degree'

    p41 = path4+'/degree'
    p42 = path4+'/weighted_degree'

    p51 = path5+'/degree'
    p52 = path5+'/weighted_degree'

    p61 = path6+'/degree'
    p62 = path6+'/weighted_degree'


    try:
        os.stat(path)
        os.stat(path1)
        os.stat(path2)
        os.stat(path3)
        os.stat(path4)
        os.stat(path5)
        os.stat(path6)
        os.stat(p11)
        os.stat(p12)
        os.stat(p21)
        os.stat(p22)
        os.stat(p31)
        os.stat(p32)
        os.stat(p41)
        os.stat(p42)
        os.stat(p51)
        os.stat(p52)
        os.stat(p61)
        os.stat(p62)

    except:
        os.mkdir(path)
        os.mkdir(path1)
        os.mkdir(path2)
        os.mkdir(path3)
        os.mkdir(path4)
        os.mkdir(path5)
        os.mkdir(path6)
        os.mkdir(p11)
        os.mkdir(p12)
        os.mkdir(p21)
        os.mkdir(p22)
        os.mkdir(p31)
        os.mkdir(p32)
        os.mkdir(p41)
        os.mkdir(p42)
        os.mkdir(p51)
        os.mkdir(p52)
        os.mkdir(p61)
        os.mkdir(p62)

def do2(state):
    path = '/Users/Abduljaleel/Desktop/project/graphs/'+state
    path1 = path+'/1h'
    path2 = path+'/2h'
    path3 = path+'/3h'
    path4 = path+'/4h'
    path5 = path+'/5h'
    path6 = path+'/6h'


    try:
        os.stat(path)
        os.stat(path1)
        os.stat(path2)
        os.stat(path3)
        os.stat(path4)
        os.stat(path5)
        os.stat(path6)

    except:
        os.mkdir(path)
        os.mkdir(path1)
        os.mkdir(path2)
        os.mkdir(path3)
        os.mkdir(path4)
        os.mkdir(path5)
        os.mkdir(path6)

#
for i in range (len(STATE)):
    do(STATE[i])

for i in range (len(STATE)):
    do2(STATE[i])