import numpy as np
from numba import jit

@jit(nopython=True)
def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    image = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            x = xmin + (xmax - xmin) * i / width
            y = ymin + (ymax - ymin) * j / height
            c = complex(x, y)
            z = 0
            count = 0
            while abs(z) <= 2 and count < max_iter:
                z = z*z + c
                count += 1
            image[j, i] = count
    return image

@jit(nopython=True)
def julia(xmin, xmax, ymin, ymax, width, height, max_iter, c):
    image = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            x = xmin + (xmax - xmin) * i / width
            y = ymin + (ymax - ymin) * j / height
            z = complex(x, y)
            count = 0
            while abs(z) <= 2 and count < max_iter:
                z = z*z + c
                count += 1
            image[j, i] = count
    return image
