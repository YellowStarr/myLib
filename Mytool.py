#coding=utf-8
import xlrd
import xlwt
import os
from xlutils.copy import copy

myDict={}
def saveExc(path,title,val):
  row=0
  wb=''
  if(os.path.exists(path)):
    data=xlrd.open_workbook(path)
    ta=data.sheets()[0]
    row=ta.nrows
    wb=xlwt.Workbook()
    wb=copy(data)
    table=wb.get_sheet(0)
  else:
    wb=xlwt.Workbook()
    table=wb.add_sheet(u"data1")
  table.write(row,0,title)
  table.write(row,1,val)
  wb.save(path)
  print "rows:%s "%(row+1)
 

def setDict(key,value):
  if not myDict.has_key(key):
    myDict[key]=value
  else:
    raise ValueError('the key has already in dictinary')
def getDict(key):
  if myDict.has_key(key):
    return myDict[key]

def returnMydic():
  return myDict

def printDict():
  if myDict:
    for k in myDict:
      print "key%s"%k
      print "value is:%s"%myDict[k]

#uname=table.cell(0,0).value
#print rows
#print uname
#uname2='qiuwjcom2'#

#print rows
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error


#table.put_cell(1,0,1,uname2,0)
#print table.cell(1,0)
#print table.cell(1,0).value

'''1、导入模块

      import xlrd

   2、打开Excel文件读取数据

       data = xlrd.open_workbook('excelFile.xls')

   3、使用技巧

        获取一个工作表

 

        table = data.sheets()[0]          #通过索引顺序获取
 
        table = data.sheet_by_index(0) #通过索引顺序获取
 

        table = data.sheet_by_name(u'Sheet1')#通过名称获取
 
        获取整行和整列的值（数组）
 　　
         table.row_values(i)
 
         table.col_values(i)
 
        获取行数和列数
　　
        nrows = table.nrows
 
        ncols = table.ncols
       
        循环行列表数据
        for i in range(nrows ):
      print table.row_values(i)
 
单元格
cell_A1 = table.cell(0,0).value
 
cell_C4 = table.cell(2,3).value
 
使用行列索引
cell_A1 = table.row(0)[0].value
 
cell_A2 = table.col(1)[0].value
 
简单的写入
row = 0
 
col = 0
 
# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
ctype = 1 value = '单元格的值'
 
xf = 0 # 扩展的格式化
 
table.put_cell(row, col, ctype, value, xf)
 
table.cell(0,0)  #单元格的值'
 
table.cell(0,0).value #单元格的值
'''