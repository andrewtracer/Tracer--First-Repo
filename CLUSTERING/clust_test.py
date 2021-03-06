import numpy as N
import pylab
import os
import re
from readicp import datareader

basePath = './FILES/Mar27_2011/'
fileCheck1 = re.compile('.bt9')
fileCheck2 = re.compile('mesh')
reader = datareader()

file_data = dict() #filename : [vect(Qx), vect(Qy), vect(Qz), vect(H)]

for root, dirs, files in os.walk('./FILES/Mar27_2011/'):
	for fname in files:
		if fileCheck1.search(fname) and fileCheck2.search(fname):
			filename = basePath + fname
			data = reader.readbuffer(filename)
			file_data[fname] = [data.data['Qx'],data.data['Qy'], data.data['Qz'], data.data['E']]
#for i in file_data:
#	if sum(file_data[i][3]) > 0.0:
#		print sum(file_data[i][3])
print len(file_data)
			
