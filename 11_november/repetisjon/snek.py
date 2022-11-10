import pygame
import time
import random
 
pygame.init()

squaresize = 25

WIDTH = squaresize * 15
HEIGHT = squaresize * 10

dis = pygame.display.set_mode((WIDTH, HEIGHT))
 
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", squaresize)


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

class Snake:
    def __init__(self,x,y,speed = 5):
        self.x = x
        self.y = y
        self.speed = speed
        self.dirx = 0
        self.diry = squaresize
        self.body = []
        self.score = 0

    def moveBody(self):
        for i in reversed(range(len(self.body))):
            if i == 0:
                self.body[i]["x"] = self.x
                self.body[i]["y"] = self.y
            else:
                self.body[i]["x"] = self.body[i-1]["x"]
                self.body[i]["y"] = self.body[i-1]["y"]

    def checkcolision(self):
        if self.x < 0 or self.x > WIDTH - squaresize:
            return True
        if self.y < 0 or self.y > HEIGHT - squaresize:
            return True

        for part in self.body:
            if part["x"] == self.x and part["y"]== self.y:
                return True

        return False


class Apple:
    def __init__(self,color = red):
        self.color = color

    def newposition(self, snake):
        busy = [(snake.x//squaresize,snake.y//squaresize)]
        for part in snake.body:
            busy.append((part["x"]//squaresize,part["y"]//squaresize))

        empty = []
        for i in range(WIDTH//squaresize):
            for j in range(HEIGHT//squaresize):
                nope = False
                for x in range(len(busy)):
                    if busy[x][0] == i and busy[x][1] == j:
                        nope = True
                        break
                if not nope:
                    empty.append((i,j))
        new = random.choice(empty)
        self.x = new[0]*squaresize
        self.y = new[1]*squaresize


def drawscreen(snake,apple):
    pygame.draw.rect(dis,black,[0,0,WIDTH,HEIGHT])
    
    score_label = score_font.render(f"Score: {snake.score}", 1, (255,255,255))
    dis.blit(score_label,(10,10))

    pygame.draw.rect(dis,white,[snake.x+1,snake.y+1,squaresize-2,squaresize-2])

    for part in snake.body:
        pygame.draw.rect(dis,white,[part["x"]+1,part["y"]+1,squaresize-2,squaresize-2])

    pygame.draw.circle(dis,apple.color,[apple.x+squaresize//2,apple.y+squaresize//2],(squaresize//3)-1)

"""
def path(snake,apple):
    displacmentX = snake.x - apple.x
    displacmentY = snake.y - apple.y
    print(displacmentX,displacmentY)
    if abs(displacmentX) > abs(displacmentY) or displacmentY == 0:
        if not snake.checkcolision(-(displacmentX/abs(displacmentX))*squaresize,0) and snake.dirx == 0:
            return displacmentX/abs(displacmentX)
    else:
        if not snake.checkcolision(0,-(displacmentY/abs(displacmentY))*squaresize) and snake.diry == 0:
            return 2*displacmentY/abs(displacmentY)
    if snake.checkcolision(snake.dirx*squaresize,snake.diry*squaresize):
        snake.dirx, snake.diry = -snake.diry, -snake.dirx
    return 0
"""

def path(snake,apple):
    board = [[0 for y in range(WIDTH//squaresize)] for x in range(HEIGHT//squaresize)]

    for part in snake.body:
        if part["y"]//squaresize >= len(board[0]) or part["x"]//squaresize >= len(board):
            continue
        board[part["y"]//squaresize][part["x"]//squaresize] = 1

    board[apple.y//squaresize][apple.x//squaresize] = 2

    board[snake.y//squaresize][snake.x//squaresize] = 3


    for row in board:
        for sqr in row:
            print(sqr,end = " ")
        print()
    print("===============")



mySnake = Snake(0,0,5)
newApple = Apple()


newApple.newposition(mySnake)
path(mySnake,newApple)
game_over = False
while not game_over:
    clock.tick(mySnake.speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and mySnake.diry != 0:
                mySnake.dirx = -squaresize
                mySnake.diry = 0
                break
            elif event.key == pygame.K_RIGHT and mySnake.diry != 0:
                mySnake.dirx = squaresize
                mySnake.diry = 0
                break
            elif event.key == pygame.K_UP and mySnake.dirx != 0:
                mySnake.dirx = 0
                mySnake.diry = -squaresize
                break
            elif event.key == pygame.K_DOWN and mySnake.dirx != 0:
                mySnake.dirx = 0
                mySnake.diry = squaresize
                break

    mySnake.moveBody()
    mySnake.x += mySnake.dirx
    mySnake.y += mySnake.diry

    if mySnake.x == newApple.x and mySnake.y == newApple.y:
        if len(mySnake.body) < 1:
            mySnake.body.append({"x":mySnake.x - mySnake.dirx,"y": mySnake.y - mySnake.diry})
        else:
            mySnake.body.append({"x": mySnake.body[-1]["x"]-mySnake.dirx,"y": mySnake.body[-1]["y"]-mySnake.diry})
        newApple.newposition(mySnake)
        mySnake.score += 1
        
        path(mySnake,newApple)



    if mySnake.checkcolision():
        break
    drawscreen(mySnake,newApple)
    pygame.display.update()

pygame.quit()
quit()