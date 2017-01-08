__author__ = 'Abduljaleel'
import xlrd

# num_rows = worksheet.nrows - 1
# num_cells = worksheet.ncols - 1
# curr_row = -1
# while curr_row < num_rows:
#   curr_row += 1
#   row = worksheet.row(curr_row)
#   print 'Row:', curr_row
#   curr_cell = -1
#   while curr_cell < num_cells:
#     curr_cell += 1
#     # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
#     # cell_type = worksheet.cell_type(curr_row, curr_cell)
#     cell_value = worksheet.cell_value(curr_row, curr_cell)
#     print cell_value

loc1 = '/Users/Abduljaleel/Desktop/project/for R/'

cc = open(loc1+'yes.txt','a')
# pl = open(loc1+'pl.txt','a')

def do(dis,i,count):
    cc = open(loc1+'yes.txt','a')
    Time=str(i)+'h'
    workbook = xlrd.open_workbook('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/'+Time+'.xlsx')
    worksheet = workbook.sheet_by_name(Time+'.csv')


    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1

    curr_cell = 0
    while curr_cell < num_cells:
        curr_cell += 1
        # print 'col:', curr_cell
        curr_row = 0
        while curr_row < num_rows:
            curr_row += 1
            cell_value = worksheet.cell_value(curr_row, curr_cell)

            if str(cell_value) == 'yes':

                count += 1
                aaa = []
                for i in range (0,11):
                    aaa.append(str(worksheet.cell_value(curr_row, i)))

                cc.write(str(aaa[0])+'\t'+str(aaa[1])+'\t'+str(aaa[2])+'\t'+str(aaa[3])+'\t'+
                         str(aaa[4])+'\t'+str(aaa[5])+'\t'+str(aaa[6])+'\t'+str(aaa[7])+'\t'+
                         str(aaa[8])+'\t'+str(aaa[9])+'\t'+str(aaa[10])+'\n')

            else:
                count += 1
                aaa = []
                for i in range (0,11):
                    aaa.append(str(worksheet.cell_value(curr_row, i)))

                cc.write(str(aaa[0])+'\t'+str(aaa[1])+'\t'+str(aaa[2])+'\t'+str(aaa[3])+'\t'+
                         str(aaa[4])+'\t'+str(aaa[5])+'\t'+str(aaa[6])+'\t'+str(aaa[7])+'\t'+
                         str(aaa[8])+'\t'+str(aaa[9])+'\t'+str(aaa[10])+'\n')

    return count
            # if str(cell_value) != '-' and str(cell_value) != 'nan':
            #     if str(curr_cell)=='1':
            #         cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hour'+'\n')
            #     else:
            #         if len(str(curr_cell)) == 1:
            #             cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hours'+'\n')
            #         else:
            #             cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+str(curr_cell)+'-hours'+'\n')
            #     print cell_value


cc = 0
for i in range (0,12):
    cc = do('heart',i+1,cc)

for i in range (0,12):
    cc = do('cancer',i+1,cc)

for i in range (0,12):
    cc = do('clrd',i+1,cc)

for i in range (0,12):
    cc = do('stroke',i+1,cc)

for i in range (0,12):
    cc = do('alzheimer',i+1,cc)

for i in range (0,12):
    cc = do('diabetes',i+1,cc)

for i in range (0,12):
    cc = do('flu_or_pneumonia',i+1,cc)

for i in range (0,12):
    cc = do('kidney',i+1,cc)

for i in range (0,12):
    cc = do('septicemia',i+1,cc)

for i in range (0,12):
    cc = do('liver',i+1,cc)

for i in range (0,12):
    cc = do('hyper',i+1,cc)

for i in range (0,12):
    cc = do('parkinson',i+1,cc)

print cc