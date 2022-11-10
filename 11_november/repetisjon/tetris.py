import pygame
import time
import random
 
pygame.init()

squaresize = 25

WIDTH = squaresize * 16
HEIGHT = squaresize * 20

dis = pygame.display.set_mode((WIDTH, HEIGHT))
 
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", squaresize)


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

S = [[" "," "," "," "],
	[" "," ","X","X"],
	[" ","X","X"," "],
	[" "," "," "," "]]

O = [[" "," "," "," "],
	[" ","X","X"," "],
	[" ","X","X"," "],
	[" "," "," "," "]]

I = [[" "," ","X"," "],
	[" "," ","X"," "],
	[" "," ","X"," "],
	[" "," ","X"," "]]

Z = [[" "," "," "," "],
	[" ","X","X"," "],
	[" "," ","X","X"],
	[" "," "," "," "]]

T = [[" "," "," "," "],
	[" "," ","X"," "],
	[" ","X","X","X"],
	[" "," "," "," "]]

J = [[" "," "," "," "],
	[" "," "," ","X"],
	[" ","X","X","X"],
	[" "," "," "," "]]

L = [[" "," "," "," "],
	[" ","X"," ",""],
	[" ","X","X","X"],
	[" "," "," "," "]]


class Piece:
	def __init__(self,x,y,body):
		self.x = x
		self.y = y
		self.body = body

	def rotate(self):
		rtnMatrix = [[" " for x in range(len(self.body))] for x in range(len(self.body))]

		for x in range(len(self.body)):
			for y in range(len(self.body[x])):
				rtnMatrix[x][y] = self.body[y][-x]

		self.body = rtnMatrix


class Pieces:
	def __init__(self):
		self.restock()

	def dealAPice(self):
		return random.choice(self.hand)

	def restock(self):
		self.hand = [O,L,J,S,Z,T,I]

def printMatrix(a):
	for row in a:
		for sqr in row:
			print(sqr, end= " ")
		print()

def drawScreen(board, tetrino,heldTetrino):
	for i in range(20):
		if not canMove(Piece(tetrino.x, tetrino.y + i, tetrino.body),board):
			shadowPiece = Piece(tetrino.x, tetrino.y + i-1, tetrino.body)
			break

	pygame.draw.rect(dis,black,[0,0,WIDTH,HEIGHT])
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == "X":
				pygame.draw.rect(dis,white,(j*squaresize+1,i*squaresize+1,squaresize-2,squaresize-2))
	try:
		for x in range(len(shadowPiece.body)):
			for y in range(len(shadowPiece.body[x])):
				if shadowPiece.body[x][y] == "X":
					pygame.draw.rect(dis,blue,((x+shadowPiece.x)*squaresize+1,(y+shadowPiece.y)*squaresize+1,squaresize-2,squaresize-2))
					pygame.draw.rect(dis,black,((x+shadowPiece.x)*squaresize+3,(y+shadowPiece.y)*squaresize+3,squaresize-6,squaresize-6))

	except:
		pass

	for x in range(len(tetrino.body)):
		for y in range(len(tetrino.body[x])):
			if tetrino.body[x][y] == "X":
				pygame.draw.rect(dis,red,((x+tetrino.x)*squaresize+1,(y+tetrino.y)*squaresize+1,squaresize-2,squaresize-2))			

	pygame.draw.rect(dis,white,(10*squaresize,0*squaresize,10*squaresize,20*squaresize))

	pygame.draw.rect(dis,black,(11*squaresize,2*squaresize,4*squaresize,4*squaresize))	

	if heldTetrino != None:
		for x in range(len(heldTetrino.body)):
			for y in range(len(heldTetrino.body[x])):
				if heldTetrino.body[x][y] == "X":
					pygame.draw.rect(dis,red,((x + 11)*squaresize+1,(y+2)*squaresize+1,squaresize-2,squaresize-2))	


def nextTetrino(pieces):
	newBody = pieces.dealAPice()
	pieces.hand.pop(pieces.hand.index(newBody))
	if len(pieces.hand) == 0:
		pieces.restock()

	return Piece(3,-2,newBody)

def canMove(tetrino,board):
	takenSqr = []
	for x in range(len(board)):
		for y in range(len(board[x])):
			if board[x][y] == "X":
				takenSqr.append((y,x))
	for x in range(len(tetrino.body)):
		for y in range(len(tetrino.body[x])):
			if tetrino.body[x][y] == "X":
				if (tetrino.x + x, tetrino.y+y) in takenSqr:
					return False
				if tetrino.x + x >= len(board[x]) or tetrino.y+y >= len(board) or tetrino.x + x < 0:
					return False
	return True

def placeTetrino(tetrino,board):
	for x in range(len(tetrino.body)):
		for y in range(len(tetrino.body[x])):
			if tetrino.body[x][y] == "X":
				board[y + tetrino.y][x + tetrino.x] = "X"
	return clearLines(board)

def clearLines(board):
	num = 0
	for x in range(len(board)):
		if not " " in board[x]:
			board.remove(board[x])
			board.insert(0,[" " for x in range(10)])
			num += 1
	return num

board = [[" " for x in range(10)]for x in range(20)]
pieces = Pieces()

def holdTetrino(tetrino, hand):
	prevTetrino = hand
	hand = tetrino
	return prevTetrino

def dropTetrino(tetrino, board):
	for i in range(20):
		if not canMove(Piece(tetrino.x, tetrino.y + i, tetrino.body),board):
			return placeTetrino(Piece(tetrino.x, tetrino.y + i-1, tetrino.body),board)



gameOver = False
tetrino = None
frameCount = 0
heldTetrino = None

level = 1
score = 0
linesCleared = 0


while not gameOver:
	clock.tick(15)
	if tetrino == None:
		tetrino = nextTetrino(pieces)
		if not canMove(tetrino,board):
			gameOver = True

	drawScreen(board,tetrino,heldTetrino)
	pygame.display.update()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_DOWN] and canMove(Piece(tetrino.x, tetrino.y + 1, tetrino.body),board):
		tetrino.y += 1
	elif keys[pygame.K_LEFT] and canMove(Piece(tetrino.x - 1, tetrino.y, tetrino.body),board):
		tetrino.x -= 1
	elif keys[pygame.K_RIGHT] and canMove(Piece(tetrino.x + 1, tetrino.y, tetrino.body),board):
		tetrino.x += 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				roatedTetrino = Piece(tetrino.x, tetrino.y, tetrino.body)
				roatedTetrino.rotate()
				if not canMove(roatedTetrino,board):
					continue
				tetrino.rotate()
				break
			elif event.key == pygame.K_c:
				heldTetrino, tetrino = tetrino, heldTetrino
				heldTetrino.x = 3
				heldTetrino.y = -2
				break
			elif event.key == pygame.K_SPACE:
				linesCleared += dropTetrino(tetrino, board)
				tetrino = None

	if (frameCount) % (30  - level* 2)  == 0 and not tetrino == None:
		if canMove(Piece(tetrino.x, tetrino.y + 1, tetrino.body),board):
			tetrino.y += 1
		else:
			linesCleared += placeTetrino(tetrino,board)
			tetrino = None

	frameCount+=1
	level = linesCleared//10 + 1

pygame.quit()
quit()