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

cc = open(loc1+'alpha7-12.txt','a')
# pl = open(loc1+'pl.txt','a')

def do(num,dis):
    workbook = xlrd.open_workbook('/Users/Abduljaleel/Desktop/project/power_law/'+dis+'/alpha.xlsx')
    worksheet = workbook.sheet_by_name('Sheet1')

    # workbook2 = xlrd.open_workbook('/Users/Abduljaleel/Desktop/project/path_length/'+dis+'.xlsx')
    # worksheet2 = workbook2.sheet_by_name('Sheet1')

    num_rows = worksheet.nrows - 1
    num_cells = worksheet.ncols - 1

    curr_cell = 0
    while curr_cell < num_cells:
        curr_cell += 1
        print 'col:', curr_cell
        curr_row = 0
        while curr_row < num_rows:
            curr_row += 1
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            if str(cell_value) != '-' and str(cell_value) != 'nan' and cell_value < 5.0:
                if str(curr_cell)=='1':
                    cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hour'+'\n')
                else:
                    if len(str(curr_cell)) == 1:
                        cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hours'+'\n')
                    else:
                        cc.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+str(curr_cell)+'-hours'+'\n')
                print cell_value


    # num_rows = worksheet2.nrows - 1
    # num_cells = worksheet2.ncols - 1
    #
    # curr_cell = 0
    # while curr_cell < num_cells:
    #     curr_cell += 1
    #     print 'col:', curr_cell
    #     curr_row = 0
    #     while curr_row < num_rows:
    #         curr_row += 1
    #         cell_value = worksheet2.cell_value(curr_row, curr_cell)
    #         if str(cell_value) != '-' and str(cell_value) != 'nan':
    #             if str(curr_cell)=='1':
    #                 pl.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hour'+'\n')
    #             else:
    #                 if len(str(curr_cell)) == 1:
    #                     pl.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+'0'+str(curr_cell)+'-hours'+'\n')
    #                 else:
    #                     pl.write(str(cell_value)+'\t'+num+'-'+dis+'\t'+str(curr_cell)+'-hours'+'\n')
    #             print cell_value



# do('01','Heart')
# do('02','Cancer')
# do('03','Clrd')
# do('04','Stroke')
# do('05','Alzheimer')
# do('06','Diabetes')
do('07','flu_or_pneumonia')
do('08','Kidney')
do('09','Septicemia')
do('10','Liver')
do('11','hyper')
do('12','Parkinson')