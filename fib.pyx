def loop(int g_id,BigArray_heart,BigArray_cancer,BigArray_clrd,BigArray_stroke,BigArray_alzheimer,BigArray_diabetes,
         BigArray_flupne,BigArray_kidney,BigArray_septicemia,BigArray_liver,BigArray_hyper,BigArray_parkinson):

    cdef int x,y

    weight_heart = []
    weight_cancer = []
    weight_clrd = []
    weight_stroke = []
    weight_alzheimer = []
    weight_diabetes = []
    weight_flupne = []
    weight_kidney = []
    weight_septicemia = []
    weight_liver = []
    weight_hyper = []
    weight_parkinson = []

    from_X_heart = []
    from_X_cancer = []
    from_X_clrd = []
    from_X_stroke = []
    from_X_alzheimer = []
    from_X_diabetes = []
    from_X_flupne = []
    from_X_kidney = []
    from_X_septicemia = []
    from_X_liver = []
    from_X_hyper = []
    from_X_parkinson = []

    to_y_heart = []
    to_y_cancer = []
    to_y_clrd = []
    to_y_stroke = []
    to_y_alzheimer = []
    to_y_diabetes = []
    to_y_flupne = []
    to_y_kidney = []
    to_y_septicemia = []
    to_y_liver = []
    to_y_hyper = []
    to_y_parkinson = []

    maxB_heart = BigArray_heart[0][0]
    maxB_cancer = BigArray_cancer[0][0]
    maxB_clrd = BigArray_clrd[0][0]
    maxB_stroke = BigArray_stroke[0][0]
    maxB_alzheimer = BigArray_alzheimer[0][0]
    maxB_diabetes = BigArray_diabetes[0][0]
    maxB_flupne = BigArray_flupne[0][0]
    maxB_kidney = BigArray_kidney[0][0]
    maxB_septicemia = BigArray_septicemia[0][0]
    maxB_liver = BigArray_liver[0][0]
    maxB_hyper = BigArray_hyper[0][0]
    maxB_parkinson = BigArray_parkinson[0][0]


    for x in range(0, g_id-1):
        for y in range(0, g_id-1):

            if BigArray_heart[x][y] != 0:
                if BigArray_heart[x][y] > maxB_heart:
                    maxB_heart = BigArray_heart[x][y]
                weight_heart.append(BigArray_heart[x][y])
                from_X_heart.append(x)
                to_y_heart.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_cancer[x][y] != 0:
                if BigArray_cancer[x][y] > maxB_cancer:
                    maxB_cancer = BigArray_cancer[x][y]
                weight_cancer.append(BigArray_cancer[x][y])
                from_X_cancer.append(x)
                to_y_cancer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_clrd[x][y] != 0:
                if BigArray_clrd[x][y] > maxB_clrd:
                    maxB_clrd = BigArray_clrd[x][y]
                weight_clrd.append(BigArray_clrd[x][y])
                from_X_clrd.append(x)
                to_y_clrd.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_stroke[x][y] != 0:
                if BigArray_stroke[x][y] > maxB_stroke:
                    maxB_stroke = BigArray_stroke[x][y]
                weight_stroke.append(BigArray_stroke[x][y])
                from_X_stroke.append(x)
                to_y_stroke.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_alzheimer[x][y] != 0:
                if BigArray_alzheimer[x][y] > maxB_alzheimer:
                    maxB_alzheimer = BigArray_alzheimer[x][y]
                weight_alzheimer.append(BigArray_alzheimer[x][y])
                from_X_alzheimer.append(x)
                to_y_alzheimer.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_diabetes[x][y] != 0:
                if BigArray_diabetes[x][y] > maxB_diabetes:
                    maxB_diabetes = BigArray_diabetes[x][y]
                weight_diabetes.append(BigArray_diabetes[x][y])
                from_X_diabetes.append(x)
                to_y_diabetes.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_flupne[x][y] != 0:
                if BigArray_flupne[x][y] > maxB_flupne:
                    maxB_flupne = BigArray_flupne[x][y]
                weight_flupne.append(BigArray_flupne[x][y])
                from_X_flupne.append(x)
                to_y_flupne.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_kidney[x][y] != 0:
                if BigArray_kidney[x][y] > maxB_kidney:
                    maxB_kidney = BigArray_kidney[x][y]
                weight_kidney.append(BigArray_kidney[x][y])
                from_X_kidney.append(x)
                to_y_kidney.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_septicemia[x][y] != 0:
                if BigArray_septicemia[x][y] > maxB_septicemia:
                    maxB_septicemia = BigArray_septicemia[x][y]
                weight_septicemia.append(BigArray_septicemia[x][y])
                from_X_septicemia.append(x)
                to_y_septicemia.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_liver[x][y] != 0:
                if BigArray_liver[x][y] > maxB_liver:
                    maxB_liver = BigArray_liver[x][y]
                weight_liver.append(BigArray_liver[x][y])
                from_X_liver.append(x)
                to_y_liver.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_hyper[x][y] != 0:
                if BigArray_hyper[x][y] > maxB_hyper:
                    maxB_hyper = BigArray_hyper[x][y]
                weight_hyper.append(BigArray_hyper[x][y])
                from_X_hyper.append(x)
                to_y_hyper.append(y)
            print str(x)+'    &    '+str(y)


            if BigArray_parkinson[x][y] != 0:
                if BigArray_parkinson[x][y] > maxB_parkinson:
                    maxB_parkinson = BigArray_parkinson[x][y]
                weight_parkinson.append(BigArray_parkinson[x][y])
                from_X_parkinson.append(x)
                to_y_parkinson.append(y)
            print str(x)+'    &    '+str(y)


    return (weight_heart,weight_cancer,weight_clrd,weight_stroke,weight_alzheimer,weight_diabetes,weight_flupne,weight_kidney,weight_septicemia,weight_liver,weight_hyper,weight_parkinson,
    from_X_heart,from_X_cancer,from_X_clrd,from_X_stroke,from_X_alzheimer,from_X_diabetes,from_X_flupne,from_X_kidney,from_X_septicemia,from_X_liver,from_X_hyper,from_X_parkinson,
    to_y_heart,to_y_cancer,to_y_clrd,to_y_stroke,to_y_alzheimer,to_y_diabetes,to_y_flupne,to_y_kidney,to_y_septicemia,to_y_liver,to_y_hyper,to_y_parkinson,
    maxB_heart,maxB_cancer,maxB_clrd,maxB_stroke,maxB_alzheimer,maxB_diabetes,maxB_flupne,maxB_kidney,maxB_septicemia,maxB_liver,maxB_hyper,maxB_parkinson)