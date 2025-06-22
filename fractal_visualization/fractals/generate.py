import numpy as np
from numba import jit

@jit(nopython=True, parallel=True)
def mandelbrot(xmin: float, xmax: float, ymin: float, ymax: float,
               width: int, height: int, max_iter: int) -> np.ndarray:
    """
    Generuje Mandelbrotovu množinu.

    Returns:
        2D numpy array s počtem iterací do divergence.
    """
    image = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            x = xmin + (xmax - xmin) * i / width
            y = ymin + (ymax - ymin) * j / height
            c = complex(x, y)
            z = 0.0 + 0.0j
            count = 0
            while abs(z) <= 2 and count < max_iter:
                z = z*z + c
                count += 1
            image[j, i] = count
    return image

@jit(nopython=True, parallel=True)
def julia(xmin: float, xmax: float, ymin: float, ymax: float,
          width: int, height: int, max_iter: int, c: complex) -> np.ndarray:
    """
    Generuje Juliovu množinu pro daný komplexní parametr c.

    Returns:
        2D numpy array s počtem iterací do divergence.
    """
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
