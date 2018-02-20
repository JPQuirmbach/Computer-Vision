import numpy
import scipy
from scipy import ndimage

im = scipy.misc.imread('img/Ferrari.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 1)  # horizontal derivative
dy = ndimage.sobel(im, 0)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('img/sobel.jpg', mag)
scipy.misc.imsave('img/sobelx.jpg', dx)
scipy.misc.imsave('img/sobely.jpg', dy)