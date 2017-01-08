

__author__ = 'Abduljaleel'
import networkx as nx
import igraph
GI = nx.Graph()


def ch(SSS,dis):

    # loc = '/Users/Abduljaleel/Desktop/project/graphs/'+SSS
    #
    # location1 = loc+'/1h/'
    # location2 = loc+'/2h/'

    found = False

    try:
        # k1 = igraph.read(location1+dis+"_1h.graphml")
        # k2 = igraph.read(location2+dis+"_2h.graphml")

        f1 = igraph.read("/Users/Abduljaleel/Desktop/01.graphml")
        f2 = igraph.read("/Users/Abduljaleel/Desktop/02.graphml")
        f3 = igraph.read("/Users/Abduljaleel/Desktop/03.graphml")
        f4 = igraph.read("/Users/Abduljaleel/Desktop/04.graphml")
        f5 = igraph.read("/Users/Abduljaleel/Desktop/05.graphml")
        f5 = igraph.read("/Users/Abduljaleel/Desktop/06.graphml")


        found = True

    except:
        print "Error"
        found = False


    if found:
        try:
            #Path Length
            print SSS+' : '+dis+' PL -- 1'
            p1 =str(f1.average_path_length())
            print p1
            print '------------------------'
            print SSS+' : '+dis+' PL -- 2'
            p2 =str(f2.average_path_length())
            print p2
            print '------------------------'
            print SSS+' : '+dis+' PL -- 2'
            p3 =str(f3.average_path_length())
            print p3
            print '------------------------'
            print SSS+' : '+dis+' PL -- 2'
            p4 =str(f4.average_path_length())
            print p4
            print '------------------------'
            print SSS+' : '+dis+' PL -- 2'
            p5 =str(f5.average_path_length())
            print p5


        except:
            print "Error in Path Length"



states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '


ch('Vermont','heart')
