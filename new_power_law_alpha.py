import powerlaw as pl
import matplotlib.pyplot as plt


def ch(SSS,dis):

    i=1
    put = open('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/alpha_'+dis+'.txt', 'a')
    # put2 = open('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/exp_01_R_'+dis+'.txt', 'a')
    # put3 = open('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/exp_02_p_'+dis+'.txt', 'a')
    # put4 = open('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/log_01_R_'+dis+'.txt', 'a')
    # put5 = open('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/log_02_p_'+dis+'.txt', 'a')

    arr = []
    # exp_r = []
    # exp_p = []
    # log_r = []
    # log_p = []

    try:
        while i<13:
            Time = str(i)+'h'
            found = True
            try:
                Degree = open('/Users/Abduljaleel/Desktop/project/degrees/'+SSS+'/'+Time+'/weighted_degree/'+dis+'_wd.txt', 'r')
                # Degree = open('/Users/Abduljaleel/Desktop/project/degrees/'+SSS+'/'+Time+'/degree/'+dis+'_degree.txt', 'r')
            except:
                print 'No file was found'
                found = False

            if (found):
                data = []
                for row in Degree:
                    if row != '':
                        data.append(int(row))

                # fit = pl.Fit(data,discrete=True,xmin=(1,10))
                fit = pl.Fit(data,discrete=True,sigma_threshold=0.1)
                # fit = pl.Fit(data,discrete=True)

                alpha = fit.power_law.alpha
                arr.append(alpha)

                # exp = fit.distribution_compare('power_law','exponential',normalized_ratio=True)
                # log = fit.distribution_compare('power_law','lognormal',normalized_ratio=True)

                # exp_r.append(str(exp[0]))
                # ee = round(float(exp[1]), 2)
                # exp_p.append(str(ee))
                # log_r.append(str(log[0]))
                # ee = round(float(log[1]), 2)
                # log_p.append(str(ee))

            else:
                arr.append('-')
                # exp_r.append('-')
                # exp_p.append('-')
                # log_r.append('-')
                # log_p.append('-')

            i+=1

    except:
        print 'ERROR'

    print '-------------------------------------'
    print SSS,'-',dis,'-----> finished'
    print '-------------------------------------'

    put.write(SSS+'\t'+str(arr[0])+'\t'+str(arr[1])+'\t'+str(arr[2])+'\t'+str(arr[3])+'\t'+str(arr[4])+'\t'
    +str(arr[5])+'\t'+str(arr[6])+'\t'+str(arr[7])+'\t'+str(arr[8])+'\t'+str(arr[9])+'\t'+str(arr[10])+'\t'
    +str(arr[11])+'\n')

    # put2.write(SSS+'\t'+str(exp_r[0])+'\t'+str(exp_r[1])+'\t'+str(exp_r[2])+'\t'+str(exp_r[3])+'\t'+str(exp_r[4])+'\t'
    # +str(exp_r[5])+'\t'+str(exp_r[6])+'\t'+str(exp_r[7])+'\t'+str(exp_r[8])+'\t'+str(exp_r[9])+'\t'+str(exp_r[10])+'\t'
    # +str(exp_r[11])+'\n')
    #
    # put3.write(SSS+'\t'+str(exp_p[0])+'\t'+str(exp_p[1])+'\t'+str(exp_p[2])+'\t'+str(exp_p[3])+'\t'+str(exp_p[4])+'\t'
    # +str(exp_p[5])+'\t'+str(exp_p[6])+'\t'+str(exp_p[7])+'\t'+str(exp_p[8])+'\t'+str(exp_p[9])+'\t'+str(exp_p[10])+'\t'
    # +str(exp_p[11])+'\n')
    #
    # put4.write(SSS+'\t'+str(log_r[0])+'\t'+str(log_r[1])+'\t'+str(log_r[2])+'\t'+str(log_r[3])+'\t'+str(log_r[4])+'\t'
    # +str(log_r[5])+'\t'+str(log_r[6])+'\t'+str(log_r[7])+'\t'+str(log_r[8])+'\t'+str(log_r[9])+'\t'+str(log_r[10])+'\t'
    # +str(log_r[11])+'\n')
    #
    # put5.write(SSS+'\t'+str(log_p[0])+'\t'+str(log_p[1])+'\t'+str(log_p[2])+'\t'+str(log_p[3])+'\t'+str(log_p[4])+'\t'
    # +str(log_p[5])+'\t'+str(log_p[6])+'\t'+str(log_p[7])+'\t'+str(log_p[8])+'\t'+str(log_p[9])+'\t'+str(log_p[10])+'\t'
    # +str(log_p[11])+'\n')



states = ' Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, ' \
         ' Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, ' \
         ' Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, ' \
         ' penna, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, ' \
         ' Wisconsin, Wyoming, District of Columbia '

STATE = states.split(',')
for i in range (0,len(STATE)):
    STATE[i] = STATE[i].strip()


# for i in range (len(STATE)):
#     ch(STATE[i],'heart')

for i in range (len(STATE)):
    ch(STATE[i],'cancer')

for i in range (len(STATE)):
    ch(STATE[i],'clrd')

for i in range (len(STATE)):
    ch(STATE[i],'stroke')

for i in range (len(STATE)):
    ch(STATE[i],'alzheimer')

for i in range (len(STATE)):
    ch(STATE[i],'diabetes')

for i in range (len(STATE)):
    ch(STATE[i],'flu_or_pneumonia')

for i in range (len(STATE)):
    ch(STATE[i],'kidney')

for i in range (len(STATE)):
    ch(STATE[i],'septicemia')

for i in range (len(STATE)):
    ch(STATE[i],'liver')

for i in range (len(STATE)):
    ch(STATE[i],'hyper')

for i in range (len(STATE)):
    ch(STATE[i],'parkinson')




