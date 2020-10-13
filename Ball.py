import pygame
import pygame.gfxdraw
import time
from Vector2D import *  # import all from our simple vector2d module
from AffineTransform import *

class Ball:
    def __init__(self, radius, color,
                 coordinate: Vector2D,
                 initialVelocity: Vector2D,
                 acceleration: Vector2D,
                 transform: AffineTransform):
        self.__radius = radius
        self.__color = color
        self.__currentCoordinate = coordinate
        self.__currentVelocity = initialVelocity
        self.__acceleration = acceleration
        self.__simTime = time.time()
        self.__trajectory = []
        self.__transform = transform

    @property
    def CurrentCoordinate(self):
        return self.__currentCoordinate

    def update(self, simTime):
        deltaT = simTime - self.__simTime  # elapsed time since last update

        xCoord = self.__currentCoordinate.X + \
                 self.__currentVelocity.X * deltaT + 0.5 * self.__acceleration.X * deltaT ** 2
        yCoord = self.__currentCoordinate.Y + \
                 self.__currentVelocity.Y * deltaT + 0.5 * self.__acceleration.Y * deltaT ** 2
        self.__currentCoordinate.update(xCoord, yCoord)

        screenCoord = self.__transform.transformCoord(self.__currentCoordinate)
        self.__trajectory.append((int(screenCoord.X), int(screenCoord.Y)))

        vx = self.__currentVelocity.X + self.__acceleration.X * deltaT
        vy = self.__currentVelocity.Y + self.__acceleration.Y * deltaT
        self.__currentVelocity.update(vx, vy)

        self.__simTime = simTime

    def __str__(self):
        return f'Current Coordinate:{self.__currentCoordinate} Current Velocity:{self.__currentVelocity}'

    def draw(self, drawingSurface):
        """
        draw the ball at drawingSurface
        """
        if len(self.__trajectory) > 1:
            pygame.draw.aalines(drawingSurface, self.__color, False, self.__trajectory)

        # center = [int(self.__currentCoordinate.X), int(self.__currentCoordinate.Y)]
        # pygame.draw.circle(drawingSurface, self.__color, center, self.__radius, 0)

        # anti-aliasing version
        screenCoord = self.__transform.transformCoord(self.__currentCoordinate)
        pygame.gfxdraw.aacircle(drawingSurface, int(screenCoord.X), int(screenCoord.Y),
                                self.__radius, self.__color)
        pygame.gfxdraw.filled_circle(drawingSurface, int(screenCoord.X), int(screenCoord.Y),
                                     self.__radius, self.__color)
