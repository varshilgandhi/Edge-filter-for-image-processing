# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:55:59 2021

@author: abc
"""

"""

Edge Filter for image processing

1. Robert
2. Sobel
3. Scharr
4. Prewitt
5. Farid
6. Canny


"""

from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

#read our image
img = cv2.imread("BSE_Image.jpg", 0)

#import different edge filters
from skimage.filters import roberts, sobel, scharr, prewitt, farid

#define all above filters
roberts_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)
farid_img = farid(img)

#show our filtered image
cv2.imshow("Original image", img)
cv2.imshow("Roberts", roberts_img)
cv2.imshow("sobel", sobel_img)
cv2.imshow("scharr", scharr_img)
cv2.imshow("prewitt", prewitt_img)
cv2.imshow("farid", farid_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



####################################################

#Canny Edge filter

from skimage import io, filters, feature
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

#read our image
img = cv2.imread("BSE_Image.jpg", 0)

#define Canny edge filter
canny_edge =cv2.Canny(img,30, 200)

#Show our image
cv2.imshow("Original image", img)
cv2.imshow("Canny", canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


#####################################################

#AutoCanny Edge filter

from skimage import io, filters
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
import numpy as np

#read our image
img = cv2.imread("BSE_Image.jpg", 0)

#define Canny Edge filter
canny_edge = cv2.Canny(img, 30, 200)

#define AutoCanny Edge Filter
sigma = 0.3
median = np.median(img)
lower = int(max(0, (1.0 - sigma) * median))
upper = int(min(255, (1.0 + sigma) * median))
auto_canny = cv2.Canny(img, lower, upper)

#show our image
cv2.imshow("Original image", img)
cv2.imshow("Canny edge filter", canny_edge)
cv2.imshow("AutoCanny edge filter", auto_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()






























