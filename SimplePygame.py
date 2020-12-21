import pygame
import math
import random
pygame.init()
clock = pygame.time.Clock()
fps = 5
screen = pygame.display.set_mode([300,300])
running = True

def showMessage(text, size, color,pos):
    font = pygame.font.Font(None, size)
    surface = font.render(text,True,color)
    screen.blit(surface,pos)

def drawCircle(size,color,pos):
    pygame.draw.circle(screen,color,pos,size)

screen.fill((255,255,255))
x=150
y=150


obstacle_x=150
obstacle_y=50

status = 0
while running:
    if status == 0:
        screen.fill((255, 255, 255))
        obstacle_x = random.randint(0,300)
        obstacle_y = random.randint(0,300)
        obstacle = drawCircle(20,(255,0,0),[obstacle_x,obstacle_y])

    #showMessage("circle",50,(255,0,0),(10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 10
                if event.key == pygame.K_RIGHT:
                    x += 10
                if event.key == pygame.K_UP:
                    y -= 10
                if event.key == pygame.K_DOWN:
                    y += 10
        circle = drawCircle(20,(0,0,0),(x,y))

        if math.fabs(x - obstacle_x) < 40 and math.fabs(y -  obstacle_y) < 40:
            print("Game Over")
            status = 1
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,255))
        showMessage("Game Over", 50, (255, 0, 0), (60, 10))

    #circle = drawCircle(x,(0,0,0),(150,150))
     # x = x+1
    #if x > 150:
     #   x = 0

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()