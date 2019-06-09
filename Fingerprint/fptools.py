# FingerPrint Tools

import cv2
import numpy as np


def averageOrientation(orientations, weights=None, deviation=False):
    """
    Calculate the average orientation in an orientation field.
    """

    orientations = np.asarray(orientations).flatten()
    o = orientations[0]

    aligned = np.where(np.absolute(orientations - o) > np.pi * 0.5,
            np.where(orientations > o, orientations - np.pi, orientations + np.pi),
            orientations)
    if deviation:
        return np.average(aligned, weights=weights) % np.pi, np.std(aligned)
    else:
        return np.average(aligned, weights=weights) % np.pi

    
def anguloCalc(image, w=16, interpolate=True):
    w = 10
    if (image.ndim > 2):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    height, width = image.shape
    

    sobelKernelX = np.array([[-1,  0,  1],[-2,  0,  2],[-1,  0,  1]])
    sobelKernelY = np.array([[-1, -2, -1],[ 0,  0,  0],[ 1,  2,  1]])

    # Compute the gradients G_x and G_y at each pixel
    G_x = cv2.filter2D(image,cv2.CV_64F, sobelKernelX)
    G_y = cv2.filter2D(image,cv2.CV_64F,sobelKernelY)

    # Estimate the local orientation of each block
    yblocks, xblocks = height // w, width // w
    O = np.empty((yblocks, xblocks))
    Mag = np.empty((yblocks, xblocks))
    for j in range(yblocks):
        for i in range(xblocks):
            V_y, V_x = 0, 0
            for v in range(w):
                for u in range(w):
                    Gxx = G_x[j*w+v, i*w+u] ** 2
                    Gyy = G_y[j*w+v, i*w+u] ** 2
                    V_x += 2 * G_x[j*w+v, i*w+u] * G_y[j*w+v, i*w+u]
                    V_y += Gxx - Gyy

            O[j, i] = np.arctan2(V_x, V_y) * 0.5
            Mag[j, i] = np.sqrt(Gxx + Gyy)/(w*w) 

    # Rotate the orientations so that they point along the ridges, and wrap
    # them into only half of the circle (all should be less than 180 degrees).
    O = (O + np.pi * 0.5) % np.pi


    # Smooth the orientation field
    orientations = np.full(image.shape, -1.0)
    O_p = np.empty(O.shape)
    O = np.pad(O, 2, mode="edge")
    for y in range(yblocks):
        for x in range(xblocks):
            surrounding = O[y:y+5, x:x+5]
            orientation, deviation = averageOrientation(surrounding, deviation=True)
            if deviation > 0.5:
                orientation = O[y+2, x+2]
            O_p[y, x] = orientation
    O = O_p

    return O,Mag

def OrietationFigure(img,D,Mag = -1):
    n_row,n_col,_ = img.shape
    jan_tam = 10
    if (Mag.ndim == 2):
        Mag = 10*np.ones([int(n_row/jan_tam),int(n_col/jan_tam)])
    for c in range(int(n_col/jan_tam)):
        for r in range(int(n_row/jan_tam)):
            r0 = int(r*jan_tam + jan_tam/2)
            c0 = int(c*jan_tam + jan_tam/2)
            r1 = r0 + int(Mag[r,c]*np.sin(D[r,c]))
            c1 = c0 + int(Mag[r,c]*np.cos(D[r,c]))
            cv2.line(img, (c0,r0),(c1 ,r1),(255,0,0),1) 
    return img





