__author__ = 'Abduljaleel'
di = ["","heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]

def dd(SSS,dis,location):

    Degree = open(location+'/degree/'+dis+'.txt', 'r')

    data = []
    for row in Degree:
        if row != '':
            data.append(int(row))

    DD = open(location+'/DegreeDistribution/'+dis+'.txt', 'a')

    for i in range (0,max(data)):
        j = i+1
        count = 0
        for k in range (0,len(data)):
            if data[k] == j:
                count +=1
        DD.write(str(j)+'\t'+str(count)+'\n')


def DD(SSS,dis):
    locc = '/Users/Abduljaleel/Desktop/project/'

    location3 = locc+SSS+'/3h'
    location6 = locc+SSS+'/6h'
    location12 = locc+SSS+'/12h'

    dd(SSS,dis,location3)
    dd(SSS,dis,location6)
    dd(SSS,dis,location12)


SSS = "Colorado"

DD(SSS,di[8])