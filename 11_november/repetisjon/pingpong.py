import pygame
import time

pygame.init()

HEIGHT = 600
WIDTH = 700
dis=pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
 
pygame.display.set_caption("pong")


white = (255,255,255)
black = (0,0,0)

game_over=False

player1 = 0
player2 = 0

ballx = 350
bally = 100
balldirx = -2
balldiry = -1

def paint():
    pygame.draw.rect(dis,black,[0,0,WIDTH,HEIGHT])
    pygame.draw.rect(dis,white,[20,player1,10,200])
    pygame.draw.rect(dis,white,[WIDTH - 20,player2,10,200])
    pygame.draw.circle(dis,white,[ballx,bally],10)

def hit(balldirx,balldiry):
    balldirx = -balldirx
    balldiry = -balldiry
    return (balldirx,balldiry)

clock = pygame.time.Clock()

while not game_over:
    clock.tick(FPS)
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1 != 0:
        player1 -= 10
    if keys[pygame.K_s] and player1 != WIDTH-300:
        player1 += 10
    if keys[pygame.K_UP] and player2 != 0: 
        player2 -= 10
    if keys[pygame.K_DOWN] and player2 != WIDTH-300:
        player2 += 10

    if bally == 0 or bally == HEIGHT:
        balldiry = -balldiry
    
    if pygame.Rect(20,player1,10,200).colliderect(pygame.Rect(ballx,bally,15,15)):
        balldirx,balldiry = hit(balldirx,balldiry)

    if pygame.Rect(WIDTH - 20,player2,10,200).colliderect(pygame.Rect(ballx,bally,15,15)):
       balldirx,balldiry = hit(balldirx,balldiry)


    ballx += balldirx
    bally += balldiry

    paint()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

pygame.quit()
quit()

