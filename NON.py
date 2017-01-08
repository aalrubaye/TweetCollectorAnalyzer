__author__ = 'Abduljaleel'
import networkx as nx
from db_sqlite3 import sqlite3
import csv
GI = nx.Graph()


states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '
STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

#
# def ch(dis,loc,SSS):
#
#     location3 = loc+SSS+'/3h/graph/'
#     location6 = loc+SSS+'/6h/graph/'
#     location12 = loc+SSS+'/12h/graph/'
#
#     mg3 =nx.read_graphml(location3+dis+".graphml")
#     mg6 =nx.read_graphml(location6+dis+".graphml")
#     mg12 =nx.read_graphml(location12+dis+".graphml")
#
#     print ' ___ pl ' + str(nx.density(mg3))
#     print ' ___ pl ' + str(nx.density(mg6))
#     print ' ___ pl ' + str(nx.density(mg12))
#
#     try:
#         mg3 =nx.read_graphml(location3+dis+".graphml")
#         mg6 =nx.read_graphml(location6+dis+".graphml")
#         mg12 =nx.read_graphml(location12+dis+".graphml")
#
#
#
#         db = sqlite3.connect(loc+SSS+'/SQLite/'+SSS+'_'+dis)
#         c = db.cursor()
#         c.execute("SELECT * FROM NODES order by date")
#         db.commit()
#         results = c.fetchall()
#
#         print dis+' 3 :   '+str(len(results))+' ---> ('+str(mg3.number_of_nodes())+') ' +str(nx.average_clustering(mg3))
#         print dis+' 6 :   '+str(len(results))+' ---> ('+str(mg6.number_of_nodes())+') ' +str(nx.average_clustering(mg6))
#         print dis+' 12:   '+str(len(results))+' ---> ('+str(mg12.number_of_nodes())+') ' +str(nx.average_clustering(mg12))
#         print '----------------------------------------'
#     except:
#         print dis + " No such graph"
#         print '----------------------------------------'

def ch(dis,loc,SSS):

    location3 = loc+SSS+'/3h/graph/'
    location6 = loc+SSS+'/6h/graph/'
    location12 = loc+SSS+'/12h/graph/'

    try:
        mg3 =nx.read_graphml(location3+dis+".graphml")
        mg6 =nx.read_graphml(location6+dis+".graphml")
        mg12 =nx.read_graphml(location12+dis+".graphml")

        db = sqlite3.connect(loc+SSS+'/SQLite/'+SSS+'_'+dis)
        c = db.cursor()
        c.execute("SELECT * FROM NODES order by date")
        db.commit()
        results = c.fetchall()

        print SSS+ " : "+dis+' 3'
        print SSS+ " : "+dis+' 6'
        print SSS+ " : "+dis+' 12'
        print '----------------------------------------'
        return (str(mg3.number_of_nodes()),str(mg6.number_of_nodes()),str(mg12.number_of_nodes()),str(mg3.number_of_edges()),str(mg6.number_of_edges()),str(mg12.number_of_edges()))

    except:
        print SSS+" : "+dis + "(No such graph)"
        print '----------------------------------------'
        return ("-","-","-","-","-","-")


ff = csv.writer(open('/Users/Abduljaleel/Desktop/project/no.csv', "wb"))


def dod(SSS):

    loc = '/Users/Abduljaleel/Desktop/project/'
    ret = []

    for i in range(80):
      ret.append(" ")

    # DD = open(loc+'ccc.txt', 'a')

    r = ch("heart",loc,SSS);            ret[0]  = r[0]; ret[1]  = r[1]; ret[2]  = r[2]; ret[3]  = r[3]; ret[4]  = r[4]; ret[5]  = r[5];
    r = ch("cancer",loc,SSS);           ret[6]  = r[0]; ret[7]  = r[1]; ret[8]  = r[2]; ret[9]  = r[3]; ret[10] = r[4]; ret[11] = r[5];
    r = ch("clrd",loc,SSS) ;            ret[12] = r[0]; ret[13] = r[1]; ret[14] = r[2]; ret[15] = r[3]; ret[16] = r[4]; ret[17] = r[5];
    r = ch("stroke",loc,SSS);           ret[18] = r[0]; ret[19] = r[1]; ret[20] = r[2]; ret[21] = r[3]; ret[22] = r[4]; ret[23] = r[5];
    r = ch("alzheimer",loc,SSS);        ret[24] = r[0]; ret[25] = r[1]; ret[26] = r[2]; ret[27] = r[3]; ret[28] = r[4]; ret[29] = r[5];
    r = ch("diabetes",loc,SSS);         ret[30] = r[0]; ret[31] = r[1]; ret[32] = r[2]; ret[33] = r[3]; ret[34] = r[4]; ret[35] = r[5];
    r = ch("flu_or_pneumonia",loc,SSS); ret[36] = r[0]; ret[37] = r[1]; ret[38] = r[2]; ret[39] = r[3]; ret[40] = r[4]; ret[41] = r[5];
    r = ch("kidney",loc,SSS);           ret[42] = r[0]; ret[43] = r[1]; ret[44] = r[2]; ret[45] = r[3]; ret[46] = r[4]; ret[47] = r[5];
    r = ch("septicemia",loc,SSS);       ret[48] = r[0]; ret[49] = r[1]; ret[50] = r[2]; ret[51] = r[3]; ret[52] = r[4]; ret[53] = r[5];
    r = ch("liver",loc,SSS);            ret[54] = r[0]; ret[55] = r[1]; ret[56] = r[2]; ret[57] = r[3]; ret[58] = r[4]; ret[59] = r[5];
    r = ch("hyper",loc,SSS);            ret[60] = r[0]; ret[61] = r[1]; ret[62] = r[2]; ret[63] = r[3]; ret[64] = r[4]; ret[65] = r[5];
    r = ch("parkinson",loc,SSS);        ret[66] = r[0]; ret[67] = r[1]; ret[68] = r[2]; ret[69] = r[3]; ret[70] = r[4]; ret[71] = r[5];
    #
    ff.writerow((SSS,ret[0],ret[1],ret[2],ret[6],ret[7],ret[8],ret[12],ret[13],ret[14],ret[18],ret[19],ret[20],
                 ret[24],ret[25],ret[26],ret[30],ret[31],ret[32],ret[36],ret[37],ret[38],ret[42],ret[43],ret[44],
                ret[48],ret[49],ret[50],ret[54],ret[55],ret[56],ret[60],ret[61],ret[62],ret[66],ret[67],ret[68]))
    ff.writerow((" ",ret[3],ret[4],ret[5],ret[9],ret[10],ret[11],ret[15],ret[16],ret[17],ret[21],ret[22],ret[23],ret[27],
                ret[28],ret[29],ret[33],ret[34],ret[35],ret[39],ret[40],ret[41],ret[45],ret[46],ret[47],ret[51],
                ret[52],ret[53],ret[57],ret[58],ret[59],ret[63],ret[64],ret[65],ret[69],ret[70],ret[71]))

    # DD.write(SSS+"\t"+ret[0]+"\t"+ret[1]+"\t"+ret[2]+"\t"+ret[6]+"\t"+ret[7]+"\t"+ret[8]+"\t"+ret[12]+"\t"+ret[13]
    #             +"\t"+ret[14]+"\t"+ret[18]+"\t"+ret[19]+"\t"+ret[20]+"\t"+ret[24]+"\t"+ret[25]+"\t"+ret[26]+"\t"+ret[30]
    #             +"\t"+ret[31]+"\t"+ret[32]+"\t"+ret[36]+"\t"+ret[37]+"\t"+ret[38]+"\t"+ret[42]+"\t"+ret[43]+"\t"+ret[44]
    #             +"\t"+ret[48]+"\t"+ret[49]+"\t"+ret[50]+"\t"+ret[54]+"\t"+ret[55]+"\t"+ret[56]+"\t"+ret[60]+"\t"+ret[61]
    #             +"\t"+ret[62]+"\t"+ret[66]+"\t"+ret[67]+"\t"+ret[68]+"\n")
    # DD.write(" "+"\t"+ret[3]+"\t"+ret[4]+"\t"+ret[5]+"\t"+ret[9]+"\t"+ret[10]+"\t"+ret[11]+"\t"+ret[15]+"\t"+ret[16]
    #             +"\t"+ret[17]+"\t"+ret[21]+"\t"+ret[22]+"\t"+ret[23]+"\t"+ret[27]+"\t"+ret[28]+"\t"+ret[29]+"\t"+ret[33]
    #             +"\t"+ret[34]+"\t"+ret[35]+"\t"+ret[39]+"\t"+ret[40]+"\t"+ret[41]+"\t"+ret[45]+"\t"+ret[46]+"\t"+ret[47]
    #             +"\t"+ret[51]+"\t"+ret[52]+"\t"+ret[53]+"\t"+ret[57]+"\t"+ret[58]+"\t"+ret[59]+"\t"+ret[63]+"\t"+ret[64]
    #             +"\t"+ret[65]+"\t"+ret[69]+"\t"+ret[70]+"\t"+ret[71]+"\n")

# def dod(SSS):
#
#     loc = '/Users/Abduljaleel/Desktop/project/'
#
#     r = ch("heart",loc,SSS);
#     # r = ch("cancer",loc,SSS);
#     r = ch("clrd",loc,SSS) ;
#     r = ch("stroke",loc,SSS);
#     r = ch("alzheimer",loc,SSS);
#     r = ch("diabetes",loc,SSS);
#     r = ch("flu_or_pneumonia",loc,SSS);
#     r = ch("kidney",loc,SSS);
#     r = ch("septicemia",loc,SSS);
#     r = ch("liver",loc,SSS);
#     r = ch("hyper",loc,SSS);
#     r = ch("parkinson",loc,SSS);


for i in range (0, len(STATE)):
    dod(STATE[i])

# dod("Florida")