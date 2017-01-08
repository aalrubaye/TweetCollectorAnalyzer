# __author__ = 'Abduljaleel'
# import networkx as nx
# from db_sqlite3 import sqlite3
# import csv
# import igraph
# GI = nx.Graph()
#
# states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
#          ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
#          ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
#          ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
#          ' Wisconsin, Wyoming, District of Columbia '
#
# STATE = states.split(',')
# for i in range (0,len(STATE)):
#     STATE[i] = STATE[i].strip()
#
#
#
# def ch(SSS,dis):
#     clustering = open('/Users/Abduljaleel/Desktop/project/clustering/'+dis+'_clustering2.txt', 'a')
#     path_length = open('/Users/Abduljaleel/Desktop/project/path_length/'+dis+'_path_length2.txt', 'a')
#
#     loc = '/Users/Abduljaleel/Desktop/project/graphs/'+SSS
#
#
#     location1 = loc+'/1h/'
#     location2 = loc+'/2h/'
#     location3 = loc+'/3h/'
#     location4 = loc+'/4h/'
#     location5 = loc+'/5h/'
#     location6 = loc+'/6h/'
#     location7 = loc+'/7h/'
#     location8 = loc+'/8h/'
#     location9 = loc+'/9h/'
#     # location10 = loc+'/10h/'
#     # location11 = loc+'/11h/'
#     # location12 = loc+'/12h/'
#
#     found = False
#
#     try:
#         k1 = igraph.read(location1+dis+"_1h.graphml")
#         k2 = igraph.read(location2+dis+"_2h.graphml")
#         k3 = igraph.read(location3+dis+"_3h.graphml")
#         k4 = igraph.read(location4+dis+"_4h.graphml")
#         k5 = igraph.read(location5+dis+"_5h.graphml")
#         k6 = igraph.read(location6+dis+"_6h.graphml")
#         k7 = igraph.read(location7+dis+"_7h.graphml")
#         k8 = igraph.read(location8+dis+"_8h.graphml")
#         k9 = igraph.read(location9+dis+"_9h.graphml")
#         # k10 = igraph.read(location10+dis+"_10h.graphml")
#         # k11 = igraph.read(location11+dis+"_11h.graphml")
#         # k12 = igraph.read(location12+dis+"_12h.graphml")
#
#         found = True
#
#     except:
#         print "Error"
#         found = False
#
#
#     if found:
#         try:
#             print SSS+' : '+dis+' CC -- 1'
#             c1=str(k1.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 2'
#             c2=str(k2.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 3'
#             c3=str(k3.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 4'
#             c4=str(k4.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 5'
#             c5=str(k5.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 6'
#             c6=str(k6.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 7'
#             c7=str(k7.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 8'
#             c8=str(k8.transitivity_undirected())
#             print SSS+' : '+dis+' CC -- 9'
#             c9=str(k9.transitivity_undirected())
#             # print SSS+' : '+dis+' CC -- 10'
#             # c10=str(k10.transitivity_undirected())
#             # print SSS+' : '+dis+' CC -- 11'
#             # c11=str(k11.transitivity_undirected())
#             # print SSS+' : '+dis+' CC -- 12'
#             # c12=str(k12.transitivity_undirected())
#             print SSS+' : '+dis+' clustring done'
#             clustering.write(SSS+'\t'+c1+'\t'+c2+'\t'+c3+'\t'+c4+'\t'+c5+'\t'+c6+'\t'+c7+'\t'+c8+'\t'+c9+'\n')
#             # clustering.write(SSS+'\t'+c1+'\t'+c2+'\t'+c3+'\t'+c4+'\t'+c5+'\t'+c6+'\t'+c7+'\t'+c8+'\t'+c9+'\t'+c10+'\t'+c11+'\t'+c12+'\n')
#             print '----------------------------------------'
#         except:
#             print "Error in CC"
#             clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#             # clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#
#         try:
#             #Path Length
#             print SSS+' : '+dis+' PL -- 1'
#             p1 =str(k1.average_path_length())
#             print SSS+' : '+dis+' PL -- 2'
#             p2 =str(k2.average_path_length())
#             print SSS+' : '+dis+' PL -- 3'
#             p3 =str(k3.average_path_length())
#             print SSS+' : '+dis+' PL -- 4'
#             p4 =str(k4.average_path_length())
#             print SSS+' : '+dis+' PL -- 5'
#             p5 =str(k5.average_path_length())
#             print SSS+' : '+dis+' PL -- 6'
#             p6 =str(k6.average_path_length())
#             print SSS+' : '+dis+' PL -- 7'
#             p7 =str(k7.average_path_length())
#             print SSS+' : '+dis+' PL -- 8'
#             p8 =str(k8.average_path_length())
#             print SSS+' : '+dis+' PL -- 9'
#             p9 =str(k9.average_path_length())
#             # print SSS+' : '+dis+' PL -- 10'
#             # p10 =str(k10.average_path_length())
#             # print SSS+' : '+dis+' PL -- 11'
#             # p11 =str(k11.average_path_length())
#             # print SSS+' : '+dis+' PL -- 12'
#             # p12 =str(k12.average_path_length())
#
#             path_length.write(SSS+'\t'+p1+'\t'+p2+'\t'+p3+'\t'+p4+'\t'+p5+'\t'+p6+'\t'+p7+'\t'+p8+'\t'+p9+'\n')
#             # path_length.write(SSS+'\t'+p1+'\t'+p2+'\t'+p3+'\t'+p4+'\t'+p5+'\t'+p6+'\t'+p7+'\t'+p8+'\t'+p9+'\t'+p10+'\t'+p11+'\t'+p12+'\n')
#             print SSS+' : '+dis+' path done '
#             print '----------------------------------------'
#
#         except:
#             print "Error in Path Length"
#             path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#             # path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#     else:
#         clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#         # # clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#         path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#         # path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
#
#
#
#
#
#
# def do(State):
#     heart = ch (State,"heart")
#     cancer = ch(State,"cancer")
#     clrd = ch (State,"clrd")
#     stroke = ch(State,"stroke")
#     alz = ch (State,"alzheimer")
#     diabetes = ch(State,"diabetes")
#     flupne = ch (State,"flu_or_pneumonia")
#     kidney = ch(State,"kidney")
#     sep = ch (State,"septicemia")
#     liver = ch(State,"liver")
#     hyper = ch (State,"hyper")
#     parkinson = ch(State,"parkinson")
#
#
#     cc.write(State+'\t'+heart[0]+'\t'+heart[1]+'\t'+heart[2]+'\t'+cancer[0]+'\t'+cancer[1]+'\t'+cancer[2]+'\t'+clrd[0]+'\t'+clrd[1]+'\t'+clrd[2]+'\t'+stroke[0]+'\t'+stroke[1]+'\t'+stroke[2]+'\t'+alz[0]+'\t'+alz[1]+'\t'+alz[2]+'\t'+diabetes[0]+'\t'+diabetes[1]+'\t'+diabetes[2]+'\t'+flupne[0]+'\t'+flupne[1]+'\t'+flupne[2]+'\t'+kidney[0]+'\t'+kidney[1]+'\t'+kidney[2]+'\t'+sep[0]+'\t'+sep[1]+'\t'+sep[2]+'\t'+liver[0]+'\t'+liver[1]+'\t'+liver[2]+'\t'+hyper[0]+'\t'+hyper[1]+'\t'+hyper[2]+'\t'+parkinson[0]+'\t'+parkinson[1]+'\t'+parkinson[2]+'\n')
#     de.write(State+'\t'+heart[3]+'\t'+heart[4]+'\t'+heart[5]+'\t'+cancer[3]+'\t'+cancer[4]+'\t'+cancer[5]+'\t'+clrd[3]+'\t'+clrd[4]+'\t'+clrd[5]+'\t'+stroke[3]+'\t'+stroke[4]+'\t'+stroke[5]+'\t'+alz[3]+'\t'+alz[4]+'\t'+alz[5]+'\t'+diabetes[3]+'\t'+diabetes[4]+'\t'+diabetes[5]+'\t'+flupne[3]+'\t'+flupne[4]+'\t'+flupne[5]+'\t'+kidney[3]+'\t'+kidney[4]+'\t'+kidney[5]+'\t'+sep[3]+'\t'+sep[4]+'\t'+sep[5]+'\t'+liver[3]+'\t'+liver[4]+'\t'+liver[5]+'\t'+hyper[3]+'\t'+hyper[4]+'\t'+hyper[5]+'\t'+parkinson[3]+'\t'+parkinson[4]+'\t'+parkinson[5]+'\n')
#     pl.write(State+'\t'+heart[6]+'\t'+heart[7]+'\t'+heart[8]+'\t'+cancer[6]+'\t'+cancer[7]+'\t'+cancer[8]+'\t'+clrd[6]+'\t'+clrd[7]+'\t'+clrd[8]+'\t'+stroke[6]+'\t'+stroke[7]+'\t'+stroke[8]+'\t'+alz[6]+'\t'+alz[7]+'\t'+alz[8]+'\t'+diabetes[6]+'\t'+diabetes[7]+'\t'+diabetes[8]+'\t'+flupne[6]+'\t'+flupne[7]+'\t'+flupne[8]+'\t'+kidney[6]+'\t'+kidney[7]+'\t'+kidney[8]+'\t'+sep[6]+'\t'+sep[7]+'\t'+sep[8]+'\t'+liver[6]+'\t'+liver[7]+'\t'+liver[8]+'\t'+hyper[6]+'\t'+hyper[7]+'\t'+hyper[8]+'\t'+parkinson[6]+'\t'+parkinson[7]+'\t'+parkinson[8]+'\n')
#     dm.write(State+'\t'+heart[9]+'\t'+heart[10]+'\t'+heart[11]+'\t'+cancer[9]+'\t'+cancer[10]+'\t'+cancer[11]+'\t'+clrd[9]+'\t'+clrd[10]+'\t'+clrd[11]+'\t'+stroke[9]+'\t'+stroke[10]+'\t'+stroke[11]+'\t'+alz[9]+'\t'+alz[10]+'\t'+alz[11]+'\t'+diabetes[9]+'\t'+diabetes[10]+'\t'+diabetes[11]+'\t'+flupne[9]+'\t'+flupne[10]+'\t'+flupne[11]+'\t'+kidney[9]+'\t'+kidney[10]+'\t'+kidney[11]+'\t'+sep[9]+'\t'+sep[10]+'\t'+sep[11]+'\t'+liver[9]+'\t'+liver[10]+'\t'+liver[11]+'\t'+hyper[9]+'\t'+hyper[10]+'\t'+hyper[11]+'\t'+parkinson[9]+'\t'+parkinson[10]+'\t'+parkinson[11]+'\n')
#
#
#     # cc.writerow((State,heart[0],heart[1],heart[2],cancer[0],cancer[1],cancer[2],clrd[0],clrd[1],clrd[2],stroke[0],stroke[1],stroke[2],alz[0],alz[1],alz[2],diabetes[0],diabetes[1],diabetes[2],flupne[0],flupne[1],flupne[2],kidney[0],kidney[1],kidney[2],sep[0],sep[1],sep[2],liver[0],liver[1],liver[2],hyper[0],hyper[1],hyper[2],parkinson[0],parkinson[1],parkinson[2]))
#     # de.writerow((State,heart[3],heart[4],heart[5],cancer[3],cancer[4],cancer[5],clrd[3],clrd[4],clrd[5],stroke[3],stroke[4],stroke[5],alz[3],alz[4],alz[5],diabetes[3],diabetes[4],diabetes[5],flupne[3],flupne[4],flupne[5],kidney[3],kidney[4],kidney[5],sep[3],sep[4],sep[5],liver[3],liver[4],liver[5],hyper[3],hyper[4],hyper[5],parkinson[3],parkinson[4],parkinson[5]))
#     # pl.writerow((State,heart[6],heart[7],heart[8],cancer[6],cancer[7],cancer[8],clrd[6],clrd[7],clrd[8],stroke[6],stroke[7],stroke[8],alz[6],alz[7],alz[8],diabetes[6],diabetes[7],diabetes[8],flupne[6],flupne[7],flupne[8],kidney[6],kidney[7],kidney[8],sep[6],sep[7],sep[8],liver[6],liver[7],liver[8],hyper[6],hyper[7],hyper[8],parkinson[6],parkinson[7],parkinson[8]))
#     # dm.writerow((State,heart[9],heart[10],heart[11],cancer[9],cancer[10],cancer[11],clrd[9],clrd[10],clrd[11],stroke[9],stroke[10],stroke[11],alz[9],alz[10],alz[11],diabetes[9],diabetes[10],diabetes[11],flupne[9],flupne[10],flupne[11],kidney[9],kidney[10],kidney[11],sep[9],sep[10],sep[11],liver[9],liver[10],liver[11],hyper[9],hyper[10],hyper[11],parkinson[9],parkinson[10],parkinson[11]))
#
# #
# for i in range (len(STATE)):
#     ch(STATE[i],'heart')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'cancer')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'clrd')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'stroke')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'alzheimer')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'diabetes')
#
# # for i in range (len(STATE)):
# #     ch(STATE[i],'flu_or_pneumonia')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'kidney')
#
# # for i in range (len(STATE)):
# #     ch(STATE[i],'septicemia')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'liver')
#
# # for i in range (len(STATE)):
# #     ch(STATE[i],'hyper')
# #
# # for i in range (len(STATE)):
# #     ch(STATE[i],'parkinson')


__author__ = 'Abduljaleel'
import networkx as nx
from db_sqlite3 import sqlite3
import csv
import igraph
GI = nx.Graph()


def ch(SSS,dis):
    clustering = open('/Users/Abduljaleel/Desktop/project/clustering/'+dis+'_clustering2.txt', 'a')
    path_length = open('/Users/Abduljaleel/Desktop/project/path_length/'+dis+'_path_length2.txt', 'a')

    loc = '/Users/Abduljaleel/Desktop/project/graphs/'+SSS


    # location1 = loc+'/1h/'
    # location2 = loc+'/2h/'
    # location3 = loc+'/3h/'
    # location4 = loc+'/4h/'
    # location5 = loc+'/5h/'
    # location6 = loc+'/6h/'
    # location7 = loc+'/7h/'
    # location8 = loc+'/8h/'
    # location9 = loc+'/9h/'
    location10 = loc+'/10h/'
    location11 = loc+'/11h/'
    location12 = loc+'/12h/'

    found = False

    try:
        # k1 = igraph.read(location1+dis+"_1h.graphml")
        # k2 = igraph.read(location2+dis+"_2h.graphml")
        # k3 = igraph.read(location3+dis+"_3h.graphml")
        # k4 = igraph.read(location4+dis+"_4h.graphml")
        # k5 = igraph.read(location5+dis+"_5h.graphml")
        # k6 = igraph.read(location6+dis+"_6h.graphml")
        # k7 = igraph.read(location7+dis+"_7h.graphml")
        # k8 = igraph.read(location8+dis+"_8h.graphml")
        # k9 = igraph.read(location9+dis+"_9h.graphml")
        k10 = igraph.read(location10+dis+"_10h.graphml")
        k11 = igraph.read(location11+dis+"_11h.graphml")
        k12 = igraph.read(location12+dis+"_12h.graphml")

        found = True

    except:
        print "Error"
        found = False


    if found:
        try:
            # print SSS+' : '+dis+' CC -- 1'
            # c1=str(k1.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 2'
            # c2=str(k2.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 3'
            # c3=str(k3.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 4'
            # c4=str(k4.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 5'
            # c5=str(k5.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 6'
            # c6=str(k6.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 7'
            # c7=str(k7.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 8'
            # c8=str(k8.transitivity_undirected())
            # print SSS+' : '+dis+' CC -- 9'
            # c9=str(k9.transitivity_undirected())
            print SSS+' : '+dis+' CC -- 10'
            c10=str(k10.transitivity_undirected())
            print SSS+' : '+dis+' CC -- 11'
            c11=str(k11.transitivity_undirected())
            print SSS+' : '+dis+' CC -- 12'
            c12=str(k12.transitivity_undirected())
            print SSS+' : '+dis+' clustring done'
            clustering.write(c10+'\t'+c11+'\t'+c12+'\n')
            # clustering.write(SSS+'\t'+c1+'\t'+c2+'\t'+c3+'\t'+c4+'\t'+c5+'\t'+c6+'\t'+c7+'\t'+c8+'\t'+c9+'\t'+c10+'\t'+c11+'\t'+c12+'\n')
            print '----------------------------------------'
        except:
            print "Error in CC"
            clustering.write('-'+'\t'+'-'+'\t'+'-'+'\n')
            # clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
        try:
            #Path Length
            # print SSS+' : '+dis+' PL -- 1'
            # p1 =str(k1.average_path_length())
            # print SSS+' : '+dis+' PL -- 2'
            # p2 =str(k2.average_path_length())
            # print SSS+' : '+dis+' PL -- 3'
            # p3 =str(k3.average_path_length())
            # print SSS+' : '+dis+' PL -- 4'
            # p4 =str(k4.average_path_length())
            # print SSS+' : '+dis+' PL -- 5'
            # p5 =str(k5.average_path_length())
            # print SSS+' : '+dis+' PL -- 6'
            # p6 =str(k6.average_path_length())
            # print SSS+' : '+dis+' PL -- 7'
            # p7 =str(k7.average_path_length())
            # print SSS+' : '+dis+' PL -- 8'
            # p8 =str(k8.average_path_length())
            # print SSS+' : '+dis+' PL -- 9'
            # p9 =str(k9.average_path_length())
            print SSS+' : '+dis+' PL -- 10'
            p10 =str(k10.average_path_length())
            print SSS+' : '+dis+' PL -- 11'
            p11 =str(k11.average_path_length())
            print SSS+' : '+dis+' PL -- 12'
            p12 =str(k12.average_path_length())

            path_length.write(p10+'\t'+p11+'\t'+p12+'\n')
            # path_length.write(SSS+'\t'+p1+'\t'+p2+'\t'+p3+'\t'+p4+'\t'+p5+'\t'+p6+'\t'+p7+'\t'+p8+'\t'+p9+'\t'+p10+'\t'+p11+'\t'+p12+'\n')
            print SSS+' : '+dis+' path done '
            print '----------------------------------------'

        except:
            print "Error in Path Length"
            path_length.write('-'+'\t'+'-'+'\t'+'-'+'\n')
            # path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
    else:
        clustering.write('-'+'\t'+'-'+'\t'+'-'+'\n')
        # clustering.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')
        path_length.write('-'+'\t'+'-'+'\t'+'-'+'\n')
        # path_length.write(SSS+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\n')


states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '

STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

# for i in range (len(STATE)):
#     ch(STATE[i],'heart')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'clrd')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'stroke')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'alzheimer')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'diabetes')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'flu_or_pneumonia')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'kidney')

# for i in range (len(STATE)):
#     ch(STATE[i],'septicemia')

for i in range (len(STATE)):
    ch(STATE[i],'liver')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'hyper')
#
# for i in range (len(STATE)):
#     ch(STATE[i],'parkinson')