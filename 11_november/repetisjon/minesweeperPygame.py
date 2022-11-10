import random
import math
import pygame
import sys
	
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

def createBoard(dim):
	board = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append("")
		board.append(row)
	return board

def printBrett(brett):
	for i in range(len(brett)+1):
		print(i, end = " ")
	print("\n--------------")
	for i, rad in enumerate(brett):
		print(i+1, end = "|")
		for square in rad:
			if square == "":
				print("☐",end = "")
			print(square, end = " ")
		print("\n")

def plantBombs(bombs, board, dim):
	for i in range(len(board)):
		for j in range(len(board)):
			board[i][j] = " "
	bombNr = 0
	while bombNr < bombs:
		col = random.randrange(len(board))
		rad = random.randrange(len(board[0]))
		if board[col][rad] == "X":
			continue
		else:
			board[col][rad] = "X"
			bombNr += 1
	for i, rad in enumerate(board):
		for j, square in enumerate(rad):
			if square == "X":
				continue
			num = 0
			for x in range(3):
				for y in range(3):
					try:
						board[i+x-1][j+y-1]
					except:
						pass
					else:
						if (i+x-1) < 0 or (j+y-1) < 0:
							continue
						else:
							if board[i+x-1][j+y-1] == "X":
								num += 1
			if not num == 0:
				board[i][j] = num

def validInp(inp,dim,brett):
	x = int(inp[0]) - 1
	y = int(inp[1]) - 1
	if not brett[x][y] == "":
		print("invalid input, square is open")
		return False
	return (x, y)

def isOver(x,y,bo,refBo):

	if refBo[x][y] == "X":
		return (False,False)
	for i, rad in enumerate(bo):
		for j, square in enumerate(rad):
			if bo[i][j] == "" and refBo[i][j] != "X":
				return (True,True)
	return (False,True)

def updateBoard(x,y,bo,refBo):
	if bo[x][y] != "" or refBo[x][y] == "X": 
		return None
	if isinstance(refBo[x][y], int):
		bo[x][y] = refBo[x][y]
		return None
	else:
		bo[x][y] = refBo[x][y]
		for k in range(3):
			for l in range(3):
				try:
					bo[x+k-1][y+l-1]
				except:
					pass
				else:
					if (x+k-1) < 0 or (y+l-1) < 0:
						continue
					else:
						updateBoard((x+k-1),(y+l-1),bo,refBo)

def drawBrett(board):
	for c in range(dim):
		for r in range(dim):
			pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE-3,SQUARESIZE-3))
	for c in range(dim):
		for r in range(dim):
			if board[c][r] == " ":
				pygame.draw.rect(screen, BLACK, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE,SQUARESIZE))
			elif isinstance(board[c][r],int):
				pygame.draw.rect(screen, BLACK, (c * SQUARESIZE, r * SQUARESIZE, SQUARESIZE-3,SQUARESIZE-3))
				label = myfont.render(f"{board[c][r]}", 1, YELLOW)
				screen.blit(label, (5 + (c*SQUARESIZE)+(SQUARESIZE/2) - (fontSize/2),r*SQUARESIZE+SQUARESIZE/2 - fontSize/2))
			elif board[c][r] == "X":
				pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE+ SQUARESIZE / 2,)), RADIUS)
			
	pygame.display.update()

dim = 10
bombs = 10

if bombs > dim**2:
	print("cant have more bombs than squares")
	sys.exit()
				
brett = createBoard(dim)
refBrett = createBoard(dim)
plantBombs(bombs, refBrett, dim)

pygame.init()

SQUARESIZE = 50
width = (dim * SQUARESIZE) - 3
height = (dim * SQUARESIZE) - 3
size = (width,height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)

fontSize = 40
myfont = pygame.font.SysFont("monospace", fontSize)

game = True
while game:
	drawBrett(brett)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:	
			posX = event.pos[0]
			posY = event.pos[1]
			col = int(posX//SQUARESIZE)
			rad = int(posY//SQUARESIZE)
		
			x, y = col, rad
			updateBoard(x,y,brett,refBrett)

			game, win = isOver(x,y,brett, refBrett)

	if not game:
		drawBrett(refBrett)
		if win:
			label = myfont.render("You win!", 1, WHITE)
		else:
			label = myfont.render("Game over!", 1, WHITE)
		screen.blit(label, (10,10))
		pygame.display.update()
		pygame.time.wait(3000)
		break