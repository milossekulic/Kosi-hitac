import numpy as np
from Vector2D import *

class AffineTransform:


    def __init__(self, drawingSurface, xMin, xMax, yMin, yMax):
        sx = drawingSurface.get_width() / (xMax - xMin)
        sy = -1.0 * drawingSurface.get_height() / (yMax - yMin)
        tx = -1.0 * sx * xMin
        ty = -1.0 * sy * yMax

        m = np.array([[sx, 0, tx],
                      [0, sy, ty],
                      [0, 0, 1]])

        self.__drawingSurface = drawingSurface
        self.__translateAndScaleMatrix = m

    def transformCoord(self, pt: Vector2D):
        ptT = [pt.X, pt.Y, 1]

        # ptT = rotationMatrix.dot(ptT)

        ptT = self.__translateAndScaleMatrix.dot(ptT)

        return Vector2D(ptT[0], ptT[1])