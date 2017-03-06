import cv2
from skimage.data import astronaut
from skimage.transform import resize
import time

import numpy as np


"""
skimage 0.0112407207489   
cv2     0.00245337486267  
factor  4.587
"""

img = astronaut()

times = []
for i in range(20):
    start = time.time()
    out = resize(img, (256, 256))
    times.append(time.time() - start)
print np.mean(times)

times = []
for i in range(20):
    start = time.time()
    out = cv2.resize(out, (256, 256))
    times.append(time.time() - start)
print np.mean(times)
