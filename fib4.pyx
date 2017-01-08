def add_vertex(g, name,added_vertices):
    if name not in added_vertices:
        added_vertices.add(name)
        g.add_vertex(name)


def loop(N,aa,added_vertices):
    cdef int j,jj

    for j in range (0,len(aa)):
        for jj in range (j+1,len(aa)):
            add_vertex(N,str(aa[j]),added_vertices)
            add_vertex(N,str(aa[jj]),added_vertices)
            N.add_edge(str(aa[j]),str(aa[jj]))