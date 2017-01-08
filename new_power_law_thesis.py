import powerlaw as pl
import matplotlib.pyplot as plt
import csv

states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '

STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()

def ch(dis,i):

    Time = str(i)+'h'

    comparison = csv.writer(open('/Users/Abduljaleel/Desktop/project/power_law2/'+dis+'/'+Time+'.csv', 'wb'))
    comparison.writerow(('','Network','alpha','exp-R','exp-p','log-R','log-p','trunc-R','trunc-p','Behaviour','social'))

    for n in range (len(STATE)):
        found = True
        try:
            Degree = open('/Users/Abduljaleel/Desktop/project/degrees/'+STATE[n]+'/'+Time+'/weighted_degree/'+dis+'_wd.txt', 'r')
        except:
            print 'No file was found'
            found = False

        if (found):
            data = []
            for row in Degree:
                if row != '':
                    data.append(int(row))

            # fit = pl.Fit(data,discrete=True)
            fit = pl.Fit(data,discrete=True,sigma_threshold=0.1)
            # fit = pl.Fit(data,discrete=True,xmin=(1,150))

            alpha = fit.power_law.alpha

            try:
                exp = fit.distribution_compare('power_law','exponential',normalized_ratio=True)
                log = fit.distribution_compare('power_law','lognormal',normalized_ratio=True)
                tru = fit.distribution_compare('power_law','truncated_power_law',normalized_ratio=True)
                re = round(float(exp[1]), 4)
                rl = round(float(log[1]), 4)
                rt = round(float(tru[1]), 4)
                be1 = 0; be2=0; be3=0

                if (exp[0] > 0):
                    if (re < 0.05):
                        be1 +=1
                else:
                    if (re < 0.05):
                        be1 -=1

                if (log[0] > 0):
                    if (rl < 0.05):
                        be2 +=1
                else:
                    if (rl < 0.05):
                        be2 -=1
                if (tru[0] > 0):
                    if (rt < 0.05):
                        be3 +=1
                else:
                    if (rt < 0.05):
                        be3 -=1
                beh=''
                bb=be1+be2+be3
                if bb == 0:
                    beh='None'
                elif bb >0:
                    beh = 'power_law'
                else:
                    beh = ''
                    if be1 <0:
                        beh += ' exp'
                    if be2 <0:
                        beh+=' log'
                    if be3 <0:
                        beh += ' trun'

                social = 'no'
                if beh == 'power_law':
                    if alpha>1.90 and alpha<3.1:
                        social = 'yes'
                comparison.writerow((STATE[n],dis+'-'+Time,alpha,exp[0],re,log[0],rl,tru[0],rt,beh,social))
            except:
                comparison.writerow((STATE[n],dis+'-'+Time,'-','-','-','-','-','-','-','-','-'))

        else:
            comparison.writerow((STATE[n],dis+'-'+Time,'-','-','-','-','-','-','-','-','-'))


# for i in range (1,2):
#     ch('liver',i+1)

# for i in range (0,12):
#     ch('heart',i+1)
#
# for i in range (0,12):
#     ch('cancer',i+1)
#
# for i in range (0,12):
#     ch('clrd',i+1)
#
# for i in range (0,12):
#     ch('stroke',i+1)
#
# for i in range (0,12):
#     ch('alzheimer',i+1)
#
# for i in range (0,12):
#     ch('diabetes',i+1)
#
# for i in range (0,12):
#     ch('flu_or_pneumonia',i+1)
#
# for i in range (0,12):
#     ch('kidney',i+1)
#
# for i in range (0,12):
#     ch('septicemia',i+1)
#
# for i in range (0,12):
#     ch('hyper',i+1)
#
# for i in range (0,12):
#     ch('parkinson',i+1)


