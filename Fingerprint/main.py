'''
Main programan to test some tools for the fptool library
'''

import fptools
import cv2


image_path = './DB/101_1.tif'

imgC = cv2.imread(image_path)
img = cv2.cvtColor(imgC,cv2.COLOR_BGR2GRAY)
D,Mag = fptools.anguloCalc(img)
imgOrietada = fptools.OrietationFigure(imgC,D)


cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.imshow('Original',imgC)
cv2.waitKey(0)
cv2.destroyAllWindows()