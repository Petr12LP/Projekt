import numpy as np
from numba import jit

@jit(nopython=True)
def mandelbrot(
    xmin: float, xmax: float, ymin: float, ymax: float, 
    width: int, height: int, max_iter: int
) -> np.ndarray:
    """
    Vygeneruje Mandelbrotovu množinu jako 2D pole počtu iterací.

    Args:
        xmin: Minimální reálná hodnota rozsahu.
        xmax: Maximální reálná hodnota rozsahu.
        ymin: Minimální imaginární hodnota rozsahu.
        ymax: Maximální imaginární hodnota rozsahu.
        width: Šířka výsledného obrázku v pixelech.
        height: Výška výsledného obrázku v pixelech.
        max_iter: Maximální počet iterací pro test divergence.

    Returns:
        2D numpy pole (height x width) obsahující počet iterací do divergence.
    """
    image = np.zeros((height, width), dtype=np.int32)
    for i in range(width):
        for j in range(height):
            x = xmin + (xmax - xmin) * i / width
            y = ymin + (ymax - ymin) * j / height
            c = complex(x, y)
            z = 0 + 0j
            count = 0
            while abs(z) <= 2 and count < max_iter:
                z = z*z + c
                count += 1
            image[j, i] = count
    return image

@jit(nopython=True)
def julia(
    xmin: float, xmax: float, ymin: float, ymax: float, 
    width: int, height: int, max_iter: int, c: complex
) -> np.ndarray:
    """
    Vygeneruje Juliovu množinu jako 2D pole počtu iterací.

    Args:
        xmin: Minimální reálná hodnota rozsahu.
        xmax: Maximální reálná hodnota rozsahu.
        ymin: Minimální imaginární hodnota rozsahu.
        ymax: Maximální imaginární hodnota rozsahu.
        width: Šířka výsledného obrázku v pixelech.
        height: Výška výsledného obrázku v pixelech.
        max_iter: Maximální počet iterací pro test divergence.
        c: Komplexní parametr funkce f(z) = z^2 + c.

    Returns:
        2D numpy pole (height x width) obsahující počet iterací do divergence.
    """
    image = np.zeros((height, width), dtype=np.int32)
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
