import powerlaw as pl
import matplotlib.pyplot as plt

# SSS='Colorado'
dis = 'heart'
i=0
aa = ['heart','diabetes','alzheimer','liver','parkinson','septicemia']
try:
    while i<6:
        # Time = str(i)+'h'
        Degree = open('/Users/Abduljaleel/Desktop/project/test/'+aa[i]+'.txt', 'r')
        # Degree = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/'+Time+'/weighted_degree/'+dis+'_wd.txt', 'r')
        # Degree = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/wCDD_1_'+dis+'.txt', 'r')
        # Degree = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/'+Time+'/degree/'+dis+'_degree.txt', 'r')
        # print Degree

        data = []

        for row in Degree:
            if row != '':
                data.append(int(row))
        # print data
        plt.subplot(3,2,i)
        plt.title(aa[i])
        plt.xlabel('weighted degree(wk)')
        plt.ylabel('P(wk)')
        # fit = pl.Fit(data,discrete=True,xmin=(1,10))
        fit = pl.Fit(data,discrete=True)
        # print fit.power_law.xmin
        # fit = pl.Fit(data,discrete=True,sigma_threshold=0.001)
        alpha = fit.power_law.alpha
        sigma = fit.power_law.sigma
        fit.plot_pdf(marker='o',linestyle='none',color='blue',lw=2, markersize=10)
        # fit.power_law.plot_pdf(label=r'$\alpha = %.2f\pm%.3f$'%(alpha,2*sigma),color='r',lw=1.0, linestyle='--')
        fit.power_law.plot_pdf(label=r'$\alpha = %.2f$'%(alpha),color='r',lw=2.2, linestyle='--')
        fit.exponential.plot_pdf(label=r'$exponential$',color='k',lw=2.2, linestyle='--')
        fit.lognormal.plot_pdf(label=r'$log normal$',color='g',lw=2.2,linestyle='--')
        fit.truncated_power_law.plot_pdf(label=r'$truncated-power-law$',color='gold',lw=2.2,linestyle='--')
        # fit.exponential.plot_pdf(label=r'$\alpha = %.2f\pm%.3f$'%(fit.power_law.alpha,2*fit.power_law.sigma),color='k',lw=1.0)
        # fit.lognormal.plot_pdf(label=r'$\alpha = %.2f\pm%.3f$'%(fit.power_law.alpha,2*fit.power_law.sigma),color='g',lw=1.0)

        # exp = fit.distribution_compare('power_law','exponential',normalized_ratio=True)
        # log = fit.distribution_compare('power_law','lognormal',normalized_ratio=True)
        # compare = open('/Users/Abduljaleel/Desktop/project/'+SSS+'/heart_comparison.txt', 'a')
        # compare.write(SSS+'\t'+Time+'\t'+str(alpha)+'\t'+str(exp[0])+'\t'+str(exp[1])+'\t'+str(log[0])+'\t'+str(log[1])+'\n')

        plt.legend(loc='best')

        i+=1
    plt.show()

except:
    print 'ERROR'

