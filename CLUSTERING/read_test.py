import numpy as N
import pylab
import os
from readicp import datareader

myfile = "./FILES/Mar27_2011/meshs006.bt9"
reader = datareader()
data = reader.readbuffer(myfile)

## data.data has keys E, min, Qx, Qy, Qz

print data.data['Qx']

#
#for root, dirs, files in os.walk('./FILES/Mar27_2011/'):
#	for fname in files:
#		print fname
