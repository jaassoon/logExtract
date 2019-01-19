#!/usr/bin/python
# -*- coding: utf-8 -*-
#读入log文件，并写到新文件中
from __future__ import print_function
import time
def extract():
  with open('data/gc.log','r') as f:
    with open('data/gc-'+time.strftime('%Y%m%d')+'.log','w') as f1:
      for line in f:
        if line.find('concurrent-sweep-start]')>-1:
          f1.write(line)

#按日统计gc动作执行次数
def daily():
  with open('data/gc-'+time.strftime('%Y%m%d')+'.log','r') as f:
    with open('data/gc-'+time.strftime('%Y%m%d')+'.csv','w') as f1:
      header='server-name,avg,total,'
      hourCntMap={}
      for i in range(0,23):
        header+=str(i)+','
        hourCntMap[i]=0
      header+=str(23)+'\n'
      hourCntMap[23]=0
      f1.write(header)

      total=0
      for line in f:
        firstStr=line.split(':')[0]
        sHour=firstStr[11:]
        if sHour.find('0')==0:
          sHour=sHour[1:]
        hourCntMap[int(sHour)]+=1
        total+=1

      avg=int(round(total/24))
      result='Excel-server#1,'+str(avg)+','+str(total)+','
      for i in range(0,23):
        result+=str(hourCntMap[i])+','
      result+=str(hourCntMap[23])+'\n'
      f1.write(result)

def monthly():
  i=0
if __name__ == "__main__":
  daily()
