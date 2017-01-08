# a = [3,4,5,7,8]
# import networkx as nx
# import igraph
# N = nx.Graph()
# gg = igraph.Graph()
#
#
# N.add_edge('1','2',weight= 5)
#
# N.add_edge('1','3',weight= 2)
#
# N.add_edge('1','4',weight= 7)
#
# N.add_edge('4','2',weight= 12)
#
#
# dd= open('/Users/Abduljaleel/Desktop/project/ww.txt','a')
# def degrees(N,dd):
#     a = []
#     for node in N.degree():
#         dd.write(str(nx.degree(N, node))+'\n')
#         a.append(nx.degree(N, node))
#     return a
# # print degrees(N,dd)
#
# added_vertices = set()
# def add_vertex(g, name):
#     if name not in added_vertices:
#         added_vertices.add(name)
#         g.add_vertex(name)
#
#
# for i in range (5):
#     add_vertex(gg,"1")
#     add_vertex(gg,"2")
#     add_vertex(gg,"3")
#
# gg.add_edge('1','2',weight=5)
# gg.add_edge('1','3',weight=3)
# gg.add_edge('1','3',weight=300)
#
# print gg.degree()
# # l = len(gg.degree())
# # for i in range(l):
# #     print gg.vs[i]['name']
# print gg.strength()
# # gg.write_graphml('/Users/Abduljaleel/Desktop/hh.graphml')



from pymongo import *

#connecting to MongoDB
connection = Connection()
db = connection.twit_usa

t_u = db.tu
tw = t_u.find()

print tw.count()

for rows in tw:
    print rows['text']
    print rows['user']['screen_name']
    print rows['created_at']
#     and much more


