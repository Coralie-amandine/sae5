# -*- coding: utf-8 -*-
import numpy as np
import datetime

fh = open('C:/Users/amand/Music/Mon projet SAE15/TP1 SAE 1.5/PREMIER TRAVAIL/evenementSAE_15.ics','r')
res=fh.read()
 
fh.close()
ress=res.split('\n')
print(ress)
# print(evenementSAE_15)
''