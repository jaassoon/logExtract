#!/usr/bin/python
# -*- coding: utf-8 -*-
#读入log文件，并写到新文件中
from __future__ import print_function
def extract():
  print('OK')
  with open('data/gc.log','r') as f:
    array=[]
    with open('data/newgc.log','w') as f1:
      for line in f:
        if line.find('concurrent-sweep-start]')>-1:
          array.append(line)
          f1.write(line)

def daily():
  i=0

def monthly():
  i=0