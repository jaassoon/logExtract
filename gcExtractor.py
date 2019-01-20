#!/usr/bin/python
# -*- coding: utf-8 -*-
#读入log文件，并写到新文件中
from __future__ import print_function
import time,calendar,datetime,os
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

#按月统计gc动作执行次数
def monthly():
  today=str(datetime.date.today()).split('-')
  curYear=int(today[0])
  curMonth=int(today[1])
  logDates=[]
  dateCntMap={}
  total=0
  days=calendar.monthrange(curYear,curMonth)[1]
  header='server-name,avg,total,'
  for i in range(1,days):
    header+=str(i)+','
    dateCntMap[i]=0
    logDates.append(datetime.date(curYear,curMonth,i).strftime('%Y%m%d'))
  header+=str(days)+'\n'
  dateCntMap[days]=0
  logDates.append(datetime.date(curYear,curMonth,days).strftime('%Y%m%d'))

  for i in range(1,days):
    logName='data/gc'+logDates[i-1]+'.log'
    if not os.path.exists(logName):
      continue
    count=-1
    for count,line in enumerate(open(logName,'r')):
      pass
    count+=1
    dateCntMap[i]=count
    total+=count

  avg=int(round(total/days))
  result='Excel-server#1,'+str(avg)+','+str(total)+','
  for i in range(1,days):
    result+=str(dateCntMap[i])+','
  result+=str(dateCntMap[days])+'\n'

  with open('data/gc-monthly-'+time.strftime('%Y%m%d')+'.csv','w') as f1:
    f1.write(header)
    f1.write(result)

if __name__ == "__main__":
  monthly()
