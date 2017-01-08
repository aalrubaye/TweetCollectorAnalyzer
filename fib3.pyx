def insert_edge(N,int x,int y):
    cdef int w

    try:
        w = N[x][y]['weight']
        w+=1
    except:
        w=1
    N.add_edge(x,y,weight= w)



def loop(Net1,aa):
    cdef int j,jj,wmax

    for j in range (0,len(aa)):
        for jj in range (j+1,len(aa)):
            insert_edge(Net1,aa[j],aa[jj])