import numpy as N
import pylab
import os
from readicp4 import datareader

myfile = "./FILES/Mar27_2011/meshs006.bt9"
reader = datareader()
print 'READING DATA'
data = reader.readbuffer(myfile)
