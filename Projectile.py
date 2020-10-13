import sys
import time
import math

import pygame
from ColorConstants import *
from AffineTransform import *
from Ball import *
from Vector2D import *

pygame.init()

screenWidth = 720
screenHeight = 420
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Projectile')
pygame.mouse.set_visible(1)

bkColor = (255, 253, 232)

clock = pygame.time.Clock()

frameRate = 60

transform = AffineTransform(screen, -20, screenWidth - 20, -20, screenHeight - 20)

ballRadius = 15
velocityMagnitude = 80  # 80 pixels/s
acc = Vector2D(0, -10)  # 10 pixels/s^2

v1 = Vector2D(velocityMagnitude * math.cos(60 * math.pi / 180), velocityMagnitude * math.sin(60 * math.pi / 180))
coord1 = Vector2D(ballRadius, ballRadius)
b1 = Ball(ballRadius, ColorGreen, coord1, v1, acc, transform)

v2 = Vector2D(velocityMagnitude * math.cos(80 * math.pi / 180), velocityMagnitude * math.sin(60 * math.pi / 180))
coord2 = Vector2D(ballRadius, ballRadius)
b2 = Ball(ballRadius, ColorBlue, coord2, v2, acc, transform)

v3 = Vector2D(velocityMagnitude * math.cos(70 * math.pi / 180), velocityMagnitude * math.sin(60 * math.pi / 180))
coord3 = Vector2D(ballRadius, ballRadius)
b3 = Ball(ballRadius, ColorRed, coord3, v3, acc, transform)

while True:
    clock.tick(frameRate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bkColor)

    # draw horizontal X-axis line
    startPt = transform.transformCoord(Vector2D(0, 0))
    endPt = transform.transformCoord(Vector2D(screenWidth - 50, 0))
    pygame.draw.line(screen, ColorSkyBlue, [startPt.X, startPt.Y], [endPt.X, endPt.Y], 3)

    # draw the launch pad
    startPt = transform.transformCoord(Vector2D(0, ballRadius))
    pygame.draw.rect(screen, ColorSkyBlue, [startPt.X, startPt.Y, ballRadius, ballRadius], 0)

    currentTime = time.time()
    for ball in [b1, b2, b3]:
        if ball.CurrentCoordinate.Y - ballRadius >= 0:
            ball.update(currentTime)

        ball.draw(screen)

    pygame.display.flip()


