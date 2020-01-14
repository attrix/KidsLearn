import pygame
white= (255,255,255)
lightgreen = (144,238,144)
black = (0,0,0)
pygame.init()
hmax = 900
player1 = 0
player2 = 1
playerturn = 0
vmax = 900
size = (hmax,vmax)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bat And Ball")
clock = pygame.time.Clock()
rect1 = 100
rect2 = 100
rect3 = 50
rect4 = 50
clock.tick(30)
running = True
pygame.draw.line(screen, white,[300,30], [300,600],2)
pygame.draw.line(screen,white,[500,30],[500,600],2)
pygame.draw.line(screen,white,[100,200],[700,200],2)
pygame.draw.line(screen,white,[100,400],[700,400],2)
pygame.draw.rect(screen,lightgreen,[rect1,rect2,rect3,rect4])
pygame.display.flip()
while running:
    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pygame.draw.rect(screen,black,[rect1,rect2,rect3,rect4])   
                pygame.display.flip()         
                pygame.draw.rect(screen,lightgreen,[rect1,(rect2+200),rect3,rect4])
                pygame.display.flip()
                rect2 = rect2 +200
            if event.key == pygame.K_UP:
                pygame.draw.rect(screen,black,[rect1,rect2,rect3,rect4])      
                pygame.display.flip()      
                pygame.draw.rect(screen,lightgreen,[rect1,(rect2-200),rect3,rect4])
                pygame.display.flip()
                rect2 = rect2 -200
            if event.key == pygame.K_RIGHT:
                pygame.draw.rect(screen,black,[rect1,rect2,rect3,rect4])      
                pygame.display.flip()      
                pygame.draw.rect(screen,lightgreen,[(rect1+250),rect2,rect3,rect4])
                pygame.display.flip()
                rect1 = rect1+250
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(screen,black,[rect1,rect2,rect3,rect4])      
                pygame.display.flip()      
                pygame.draw.rect(screen,lightgreen,[(rect1 - 250),rect2,rect3,rect4])
                pygame.display.flip()
                rect1 = rect1 - 250       
            if event.key == pygame.K_SPACE: 
                if (rect1 <210 and rect2 < 150):
                    if playerturn == player1:                   
                        pygame.draw.circle(screen,white,(rect1,rect2),50)

                    if playerturn == player2:
                        pygame.draw.rect(screen,white,(rect1,rect2,90,90))
    pygame.display.flip()
    
