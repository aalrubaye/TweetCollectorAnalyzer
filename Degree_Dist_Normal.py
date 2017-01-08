__author__ = 'Abduljaleel'

location = '/Users/Abduljaleel/Desktop/'
Degree = open(location+'weights.txt', 'r')

data = []
for row in Degree:
    if row != '':
        data.append(int(row))

DD = open(location+'DD.txt', 'a')

for i in range (0,max(data)):
    j = i+1
    count = 0
    for k in range (0,len(data)):
        if data[k] == j:
            count +=1
    DD.write(str(j)+'\t'+str(count)+'\n')
print 'Done'