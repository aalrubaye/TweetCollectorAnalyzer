__author__ = 'Abduljaleel'

import powerlaw
import plfit
import matplotlib.pyplot as plt
from collections import Counter
from pylab import *
import csv



# limit = 17
type = 'alpha'

loc = '/Users/Abduljaleel/Desktop/project/Statistics/'
loc3 = '/Users/Abduljaleel/Desktop/project/Statistics/3h/'+type+'/'
loc6 = '/Users/Abduljaleel/Desktop/project/Statistics/6h/'+type+'/'
loc12 = '/Users/Abduljaleel/Desktop/project/Statistics/12h/'+type+'/'

dis = ["heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]

alpha = open(loc+'tweet.txt', 'r')

lines = []
for row in alpha:
    lines.append(row)


dis = ['Heart','Malignant','CLRD','Stroke','Alzheimer','Diabetes','Flu-Pneumonia','Kidney','Septicemia','Liver','Hypertension','Parkinson']
z = 0
j=0
while (j<36):
    d = lines[j].split('\t')
    data=[]
    for i in range (0, len(d)):
        if ('-' not in str(d[i])):
            if ('nan' not in str(d[i])):
                if ('\r' not in str(d[i])):
                    if ('\n' not in str(d[i])):
                        data.append(float(str(d[i])))
                    else:
                        t = str(d[i])
                        data.append(float(t[0:4]))
                else:
                    t = str(d[i])
                    data.append(float(t[1:5]))

    print data
    file = open(loc+'de.txt', 'a')

    for k in range (0,len(data)):
        # if data[k] < limit:
        file.write('3'+'\t'+dis[z]+'\t'+str(data[k])+'\n')

    d = lines[j+1].split('\t')
    data=[]
    for i in range (0, len(d)):
        if ('-' not in str(d[i])):
            if ('nan' not in str(d[i])):
                if ('\r' not in str(d[i])):
                    if ('\n' not in str(d[i])):
                        data.append(float(str(d[i])))
                    else:
                        t = str(d[i])
                        data.append(float(t[0:4]))
                else:
                    t = str(d[i])
                    data.append(float(t[1:5]))

    print data
    file = open(loc+'de.txt', 'a')

    for k in range (0,len(data)):
        # if data[k] < limit:
        file.write('6'+'\t'+dis[z]+'\t'+str(data[k])+'\n')



    d = lines[j+2].split('\t')
    data=[]
    for i in range (0, len(d)):
        if ('-' not in str(d[i])):
            if ('nan' not in str(d[i])):
                if ('\r' not in str(d[i])):
                    if ('\n' not in str(d[i])):
                        data.append(float(str(d[i])))
                    else:
                        t = str(d[i])
                        data.append(float(t[0:4]))
                else:
                    t = str(d[i])
                    data.append(float(t[1:5]))

    print data
    file = open(loc+'de.txt', 'a')

    for k in range (0,len(data)):
        # if data[k] < limit:
        file.write('12'+'\t'+dis[z]+'\t'+str(data[k])+'\n')

    z+=1
    j+=3
















# limit = 15
# type = 'alpha'
#
# loc = '/Users/Abduljaleel/Desktop/project/Statistics/'
# loc3 = '/Users/Abduljaleel/Desktop/project/Statistics/3h/'+type+'/'
# loc6 = '/Users/Abduljaleel/Desktop/project/Statistics/6h/'+type+'/'
# loc12 = '/Users/Abduljaleel/Desktop/project/Statistics/12h/'+type+'/'
#
# dis = ["heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]
#
# alpha = open(loc+'alpha.txt', 'r')
#
# lines = []
# for row in alpha:
#     lines.append(row)
#
# # with open(loc+'alpha.txt') as f:
# #     lines = f.readlines()
#
# def do(j,ll):
#     dis = ['heart','cancer','clrd','stroke','alz','diabetes','flupne','kidney','septicemia','liver','hyper','parkinson']
#     z = 0
#     while (j<36):
#         d = lines[j].split('\t')
#         data=[]
#         for i in range (0, len(d)):
#             if ('nan' not in str(d[i])):
#                 if ('\r' not in str(d[i])):
#                     if ('\n' not in str(d[i])):
#                         data.append(float(str(d[i])))
#                     else:
#                         t = str(d[i])
#                         data.append(float(t[0:4]))
#                 else:
#                     t = str(d[i])
#                     data.append(float(t[1:5]))
#
#         print data
#         file = open(ll+dis[z]+'.txt', 'w')
#         z+=1
#
#         for k in range (0,len(data)):
#             if data[k] < limit:
#                 file.write(str(data[k])+'\n')
#
#         j+=3
#
#
# do(0,loc3)
# do(1,loc6)
# do(2,loc12)