import os
import csv
from skimage import exposure
import numpy as np
from scipy.misc import imread, toimage
Channels = 3
EdgeFind = True
filefolder = "/processed/"
datastarted = False
data = []
files = os.listdir(os.getcwd() + filefolder)
for i in range(len(files)):
	filename = files[i]
	im=imread(os.getcwd() + filefolder + filename)
	im = np.divide(im, 255.0)
	data += [im]
	print str(i*100.0/len(files)) +"% complete"

stackeddata = np.stack(data)

np.save("images-"+str(Channels)+"l3", stackeddata)
