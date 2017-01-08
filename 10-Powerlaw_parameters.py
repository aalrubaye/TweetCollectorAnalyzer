__author__ = 'Abduljaleel'

import powerlaw as pl
import plfit
import matplotlib.pyplot as plt
from collections import Counter
from pylab import *
import csv

states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts'

# states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
#          ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
#          ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
#          ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
#          ' Wisconsin, Wyoming, District of Columbia '

STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

loc = '/Users/Abduljaleel/Desktop/project/'


def alpha(SSS,dis):
    location1 = loc+SSS+'/1h'
    location2 = loc+SSS+'/2h'
    location3 = loc+SSS+'/3h'
    location4 = loc+SSS+'/4h'
    location5 = loc+SSS+'/5h'
    location6 = loc+SSS+'/6h'

    file = '/weighted_degree/'
    ext = '_wd.txt'

    try:
        Degree = open(location1+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = 1)
        one = str(fit.power_law.alpha)

    except:
        print "Error"
        one = '-'

    try:
        Degree = open(location2+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = 1)
        two = str(fit.power_law.alpha)

    except:
        print "Error"
        two = '-'

    try:
        Degree = open(location3+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = discrete=True)
        three = str(fit.power_law.alpha)

    except:
        print "Error"
        three = '-'


    try:
        Degree = open(location4+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = 1)
        four = str(fit.power_law.alpha)

    except:
        print "Error"
        four = '-'

    try:
        Degree = open(location5+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = 1)
        five = str(fit.power_law.alpha)

    except:
        print "Error"
        five = '-'

    try:
        Degree = open(location6+file+dis+ext, 'r')
        data = []
        for row in Degree:
            if row != '':
                data.append(int(row))
        fit = powerlaw.Fit(data)
        # fit = powerlaw.Fit(data, xmin = 1)
        six = str(fit.power_law.alpha)


    except:
        print "Error"
        six = '-'

    return (one,two,three,four,five,six)
    # R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
    # print R,p
#
#
# dis = ["heart","cancer","clrd","stroke","alzheimer","diabetes","flu_or_pneumonia","kidney","septicemia","liver","hyper","parkinson"]
#
# ff = csv.writer(open(loc+'alpha.csv', "wb"))
#
#
# for i in range (0,len(STATE)):
#     State = STATE[i]
#     rr=[]
#     rr.append(State)
#     for i in range(0,len(dis)):
#         a = alpha(State,dis[i])
#         for j in range (0,6):
#            rr.append(a[j])
#
#     ff.writerow(rr)
#
# #
#
#

SSS='Arizona'
dis = 'diabetes'
Time = '3h'
try:
    # Degree = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/'+timewindow+'/degree/'+dis+'_degree.txt', 'r')
    Degree = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/'+Time+'/weighted_degree/'+dis+'_wd.txt', 'r')
    # Degree = open('/Users/Abduljaleel/Desktop/ww3.txt', 'wr')
    print Degree

    data = []
    for row in Degree:
        if row != '':
            data.append(int(row))
    print data
    fit = pl.Fit(data,discrete=True,xmin=(1,10))
    fit.plot_pdf(marker='.',linestyle='none',color='red')
    fit.power_law.plot_pdf(label=r'$\alpha = %.2f\pm%.3f$'%(fit.power_law.alpha,2*fit.power_law.sigma),color='k',lw=1.5)
    plt.legend(loc='best')

except:
    print 'ERROR'


















#
#     xm = fit.power_law.xmin
#     print xm
#
#     fit = powerlaw.Fit(data, xmin = xm)
#     three = str(fit.power_law.alpha)
#     print three
# except:
#     print "Error"
#     three = '-'



# Degree = open('/Users/Abduljaleel/Desktop/project/tt.txt', 'r')
# data = []
# for row in Degree:
#     if row != '':
#         data.append(int(row))
# fit = powerlaw.Fit(data)
# print fit.power_law.xmin
# fit = powerlaw.Fit(data, xmin = 1)
# three = str(fit.power_law.alpha)
# print three
timewindow = '3h'
