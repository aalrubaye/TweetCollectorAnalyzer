def loop(int g_id,BigArray_heart):

    cdef int x,y

    weight_heart = []
    from_X_heart = []
    to_y_heart = []
    maxB_heart = BigArray_heart[0][0]
    t=0
    for x in range(0, g_id-1):
        for y in range(0, g_id-1):

            if BigArray_heart[x][y] != 0:

                if BigArray_heart[x][y] > maxB_heart:
                    maxB_heart = BigArray_heart[x][y]
                weight_heart.append(BigArray_heart[x][y])
                from_X_heart.append(x)
                to_y_heart.append(y)
            print str(x)+'    &    '+str(y)



    return (weight_heart,from_X_heart,to_y_heart,maxB_heart)