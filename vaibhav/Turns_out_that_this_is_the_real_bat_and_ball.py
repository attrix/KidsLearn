import pygame
import math

pi = 3.141592653

def drawcircle(radius, x,y,color):

    angle = 0
    radians = angle
    sface = pygame.display.get_surface()
    while ((angle <=30 and angle >=60) ):
        o = round(radius*(math.sin(radians)))
        a = round(radius*(math.cos(radians)))
        j = radius-a
        sface.set_at(((x+radius)-j,y-o),color)
        angle = angle + 2
        radians = ((2*pi)/360)*angle
        angle = 45


    pygame.display.flip()


if __name__ == "__main__":
    white= (255,255,255)
    black = (0,0,0)
    pygame.init()
    hmax = 500
    vmax = 500
    size = (hmax,vmax)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bat And Ball")
    clock = pygame.time.Clock()
    clock.tick(60)
    pi = 3.141592653
    x = 100
    y = 200
    direction = 4
    running = True
    ballangle = 60
    batx = 20
    baty = vmax - 20
    batsize = 30
    endx = batx + batsize
    endy = vmax - 20
    batstep = 10
    radius = 10
    pygame.draw.line(screen,white,[batx,baty],[endx,endy],1)

    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pygame.draw.line(screen,black,[batx,baty],[endx,endy])
                pygame.display.flip()
                batx = batx+batsize
                endx = endx+batsize
                if (endx >= hmax):
                    batx = hmax - batsize
                    endx = hmax
                pygame.draw.line(screen,white,[batx,baty],[endx,endy])
                pygame.display.flip()
                
            if event.key == pygame.K_LEFT:
                pygame.draw.line(screen,black,[batx,baty],[endx,endy])
                pygame.display.flip()
                batx = batx-batsize
                endx = endx-batsize
                if (endx <= 0):
                    batx = 0
                    endx = batsize
                pygame.draw.line(screen,white,[batx,baty],[endx,endy])
                pygame.display.flip()

    
        #drawcircle(10,x,y,white)
        pygame.draw.circle(screen, white, [x,y],radius,1)
        pygame.display.flip()
        pygame.time.wait(50)
        #drawcircle(10,x,y,(0,0,0))
        pygame.draw.circle(screen, black, [x,y],radius,1)
        pygame.display.flip()
        ballradians = ballangle *((2*pi)/360)
        xchange = radius
        ychange = round(math.tan(ballradians) * xchange)
        if direction == 1:
            x += xchange
            y -= ychange
        elif direction == 2:
            x -= xchange
            y -= ychange
        elif direction == 3:
            x -= xchange
            y += ychange
        elif direction == 4:
            x += xchange
            y += ychange

        if y <= 0 or y >= vmax:
            ballangle += 3
            if direction == 4:
                direction = 1
            elif direction == 3:
                direction = 2
            elif direction == 1:
                direction = 4
            elif direction == 2:
                direction = 3


        if x <= 0 or x >= hmax :
            ballangle -= 3
            if direction == 4:
                direction = 3
            elif direction == 3:
                direction = 4
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1

        if x >= batx and x <= endx and ((y + radius) >= baty):
            if direction == 4:
                direction = 1
            elif direction == 3:
                direction = 2
            y = baty -radius 
            pygame.draw.line(screen,white,[batx,baty],[endx,endy])
            pygame.display.flip()