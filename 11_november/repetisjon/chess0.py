import pygame
import time

pygame.init()

colors = ["W","B"]

squaresize = 50

BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)

width = squaresize * 8
height = squaresize * 8

dis = pygame.display.set_mode((width,height))

fontSize = 20
myfont = pygame.font.SysFont("monospace", fontSize)
endFont = pygame.font.SysFont("monospace", 60)

class Piece:
	def __init__(self,color):
		self.color = color
		self.moved = False

	def is_open(self,bo,x,y):
		if not x in range(8) or not y in range(8):
			return False

		if bo[x][y] == " ":
			return True
		else:
			return False

	def is_takable(self,bo,x,y):
		if not x in range(8) or not y in range(8):
			return False

		if bo[x][y].color != self.color:
			return True
		else:
			return False

class King(Piece):
	def __repr__ (self):
		return "K" + self.color

	def moves(self, bo, x, y):
		available_moves = []
		for i in range(3):
			for j in range(3):
				if Piece.is_open(self,bo,x+i-1,y+j-1):
					available_moves.append((x+i-1,y+j-1))
				elif x+i-1 in range(8) and y+j-1 in range(8) and Piece.is_takable(self,bo,x+i-1,y+j-1):
					available_moves.append((x+i-1,y+j-1))

		if not self.moved:
			if isinstance(board[x][0], Rock) and not board[x][0].moved and board[x][1] == board[x][2] == board[x][3] == " ":
				available_moves.append((x,2))
			if isinstance(board[x][7], Rock) and not board[x][7].moved and board[x][5] == board[x][6] == " ":
				available_moves.append((x,6))

		return available_moves

class Queen(Piece):
	def __repr__ (self):
		return "Q" + self.color
	
	def moves(self, bo, x, y):
		available_moves = []
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y+i):
				available_moves.append((x+i,y+i))
			else:
				if x+i in range(8) and y+i in range(8) and Piece.is_takable(self,bo,x+i,y+i):
					available_moves.append((x+i,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y-i):
				available_moves.append((x-i,y-i))
			else:
				if x-i in range(8) and y-i in range(8) and Piece.is_takable(self,bo,x-i,y-i):
					available_moves.append((x-i,y-i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y+i):
				available_moves.append((x-i,y+i))
			else:
				if y+i in range(8) and x-i in range(8) and Piece.is_takable(self,bo,x-i,y+i):
					available_moves.append((x-i,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y-i):
				available_moves.append((x+i,y-i))
			else:
				if y-i in range(8) and x+i in range(8) and Piece.is_takable(self,bo,x+i,y-i):
					available_moves.append((x+i,y-i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y):
				available_moves.append((x+i,y))
			else:
				if x+i in range(8) and Piece.is_takable(self,bo,x+i,y):
					available_moves.append((x+i,y))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y):
				available_moves.append((x-i,y))
			else:
				if x-i in range(8) and Piece.is_takable(self,bo,x-i,y):
					available_moves.append((x-i,y))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x,y+i):
				available_moves.append((x,y+i))
			else:
				if y+i in range(8) and Piece.is_takable(self,bo,x,y+i):
					available_moves.append((x,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x,y-i):
				available_moves.append((x,y-i))
			else:
				if y-i in range(8) and Piece.is_takable(self,bo,x,y-i):
					available_moves.append((x,y-i))
				break

		return available_moves

class Pawn(Piece):
	def __init__(self,color):
		self.color = color
		self.moved = False
		self.enpassant= False

	def __repr__ (self):
		return "P" + self.color

	def moves(self, bo,x,y):
		available_moves = []
		direction = (lambda: 1 if self.color == "B" else -1)()
		for i in range(1,3):
			if Piece.is_open(self,bo, x+(direction*i), y):
				available_moves.append((x+(direction*i), y))								
			else:
				break
			if self.moved:
				break

		if y != len(bo)-1:
			if isinstance(bo[x+direction][y+1], Piece) and bo[x+direction][y+1].color != self.color :
				available_moves.append((x+direction,y+1))

			if isinstance(bo[x][y+1], Pawn) and bo[x][y+1].enpassant:
				available_moves.append((x,y+1))

		if y != 0:
			if isinstance(bo[x+direction][y-1], Piece) and bo[x+direction][y-1].color != self.color :
				available_moves.append((x+direction,y-1))

			if isinstance(bo[x][y-1], Pawn) and bo[x][y-1].enpassant:
				available_moves.append((x,y+1))


		return available_moves

class Rock(Piece):
	def __repr__ (self):		
		return "R" + self.color

	def moves(self, bo, x, y):
		available_moves = []
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y):
				available_moves.append((x+i,y))
			else:
				if x+i in range(8) and Piece.is_takable(self,bo,x+i,y):
					available_moves.append((x+i,y))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y):
				available_moves.append((x-i,y))
			else:
				if x-i in range(8) and Piece.is_takable(self,bo,x-i,y):
					available_moves.append((x-i,y))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x,y+i):
				available_moves.append((x,y+i))
			else:
				if y+i in range(8) and Piece.is_takable(self,bo,x,y+i):
					available_moves.append((x,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x,y-i):
				available_moves.append((x,y-i))
			else:
				if y-i in range(8) and Piece.is_takable(self,bo,x,y-i):
					available_moves.append((x,y-i))
				break
		
		return available_moves

class Bishop(Piece):
	def __repr__ (self):
		return "B" + self.color

	def moves(self, bo, x, y):
		available_moves = []
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y+i):
				available_moves.append((x+i,y+i))
			else:
				if x+i in range(8) and y+i in range(8) and Piece.is_takable(self,bo,x+i,y+i):
					available_moves.append((x+i,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y-i):
				available_moves.append((x-i,y-i))
			else:
				if x-i in range(8) and y-i in range(8) and Piece.is_takable(self,bo,x-i,y-i):
					available_moves.append((x-i,y-i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x-i,y+i):
				available_moves.append((x-i,y+i))
			else:
				if y+i in range(8) and x-i in range(8) and Piece.is_takable(self,bo,x-i,y+i):
					available_moves.append((x-i,y+i))
				break
		for i in range(1,8):
			if Piece.is_open(self,bo,x+i,y-i):
				available_moves.append((x+i,y-i))
			else:
				if y-i in range(8) and x+i in range(8) and Piece.is_takable(self,bo,x+i,y-i):
					available_moves.append((x+i,y-i))
				break
		return available_moves

class Horse(Piece):
	def __repr__ (self):
		return "H" + self.color

	def moves(self, bo, x, y):
		available_moves = []
		for i in [1,-1]:
			for j in [2,-2]:
				if Piece.is_open(self, bo,x+i,y+j) or Piece.is_takable(self,bo,x+i,y+j):
					available_moves.append((x+i,y+j))
		for i in [2,-2]:
			for j in [1,-1]:
				if Piece.is_open(self, bo,x+i,y+j) or Piece.is_takable(self,bo,x+i,y+j):
					available_moves.append((x+i,y+j))

		return available_moves
	
def createBoard():
	specialB = [[Rock("B"),Horse("B"),Bishop("B"),Queen("B"),King("B"),Bishop("B"),Horse("B"),Rock("B")]]
	bonderadB = [[Pawn("B") for x in range(8)]]
	deadzone = [[" " for y in range(8)] for x in range(4)]
	bonderadW = [[Pawn("W") for x in range(8)]]
	specialW = [[Rock("W"),Horse("W"),Bishop("W"),Queen("W"),King("W"),Bishop("W"),Horse("W"),Rock("W")]]
	
	return specialB + bonderadB + deadzone + bonderadW + specialW

board = createBoard()

def possible_moves(bo,color):
	squares = []
	for i in range(len(bo)):
		for j in range(len(bo[i])):
			squares += pick_pice(bo,color, i, j)
	return squares

def find_king(bo,color):
	for x in range(len(bo)):
		for y in range(len(bo[x])):
			if isinstance(bo[x][y],King) and bo[x][y].color == color:
				return (x,y)
	return (0,0)

def attacked_squares(bo,color):
	squares = []
	for i in range(len(bo)):
		for j in range(len(bo[i])):
			if isinstance(bo[i][j], Pawn):
				moves = pick_pice(bo,color, i, j)
				for square in moves:
					if square[1] != j:
						squares.append(square)
			else:
				squares += pick_pice(bo,color, i, j)
	return squares

def in_check(bo,turn):
	kingX, kingY = find_king(bo, colors[(turn)%2])
	
	for sqr in attacked_squares(bo,colors[(turn+1)%2]):
		if kingX == sqr[0] and kingY == sqr[1]:
			return True
	return False

def pick_pice(bo, color,x,y):
	if not isinstance(bo[x][y],Piece) or bo[x][y].color != color:
		return []
	return  bo[x][y].moves(bo,x,y)

def pick_move(bo,x,y,x1,y1,sqrs):
	if not (x,y) in sqrs:
		return False

	bo[x][y] = bo[x1][y1]
	bo[x1][y1] = " "

	if isinstance(bo[x][y], King) and not bo[x][y].moved:
		if y == 6 and x == x1:
			bo[x1][5] = Rock(bo[x][y].color)
			bo[x1][7] = " "
		if y == 2 and x == x1:
			bo[x1][3] = Rock(bo[x][y].color)
			bo[x1][0] = " "

	if isinstance(bo[x][y],Pawn):
		if x == 0 or x == 7:
			bo[x][y] = Queen(bo[x][y].color)
	return True

def draw_board(bo,sqs, check,selected):
	square = lambda z: WHITE if z % 2 == 0 else BLACK
	picecolor = lambda z: WHITE if z == "W" else BLACK
	for i in range(len(bo)):
		for j in range(len(bo[i])):
			pygame.draw.rect(dis, square(i+j), (j * squaresize, i * squaresize, squaresize,squaresize))
	for x,y in sqs:
		pygame.draw.rect(dis, YELLOW, (y * squaresize, x * squaresize, squaresize,squaresize))

	if check[0]:
		kingX, kingY = find_king(bo,"W")
		pygame.draw.rect(dis, RED, (kingY * squaresize, kingX * squaresize, squaresize,squaresize))
	if check[1]:
		kingX, kingY = find_king(bo,"B")
		pygame.draw.rect(dis, RED, (kingY * squaresize, kingX * squaresize, squaresize,squaresize))
	if selected:
		pygame.draw.rect(dis,GREEN,(y1*squaresize,x1*squaresize,squaresize,squaresize))
	for i in range(len(bo)):
		for j in range(len(bo[i])):
			if bo[i][j] != " ":
				label = myfont.render(f"{board[i][j]}", 1, BLUE)
				dis.blit(label, (5 + (j*squaresize)+(squaresize//2) - (fontSize//2),i*squaresize+(squaresize//2) - (fontSize//2)))

def createcopy(bo):
	return [[y for y in x] for x in bo]

def self_checking_move(bo,x,y,squares,turn):
	returnsqrs = []
	for sqr in squares:
		test_bo = createcopy(bo)
		pick_move(test_bo,sqr[0],sqr[1],x,y,squares)
		if not in_check(test_bo,turn):
			returnsqrs.append(sqr)
	return returnsqrs

def checkmate(bo,turn):
	for x in range(len(bo)):
		for y in range(len(bo[x])):
			tst_squares = pick_pice(bo,colors[turn % 2],x,y)
			squares = self_checking_move(bo,x,y,tst_squares,turn)
			if len(squares) > 0:
				return False
	return True

turn = 0
clock = pygame.time.Clock()

piceselected = False
squares = []

unpassant = None

check = [False,False]

game = True
while game:
	clock.tick(60)
	draw_board(board,squares, check,piceselected)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONDOWN:

			if isinstance(unpassant, tuple) and unpassant[2] < turn:
				board[unpassant[0]][unpassant[1]].enpassant = False
				unpassant = None

			posX = event.pos[1]
			posY = event.pos[0]
			x = int(posX//squaresize)
			y = int(posY//squaresize)

			if piceselected:
				picked = pick_move(board, x,y,x1,y1,squares)
				if picked:
					if isinstance(board[x][y],Pawn) and not board[x][y].moved:
						board[x][y].enpassant = True
						unpassant = (x,y,turn)

					board[x][y].moved = True
					
					squares = []
					piceselected = False
					check[(turn)%2] = in_check(board,turn)
					check[(turn+1)%2] = in_check(board,turn+1)
					if check[(turn+1)%2] and checkmate(board,turn+1):
						game = False
						draw_board(board,squares,check)
						label = endFont.render(f"{colors[(turn)%2]} win!", 10, RED)
						dis.blit(label, (squaresize*8 // 2 - label.get_rect().width // 2,squaresize*8 // 2 - label.get_rect().height//2))
						pygame.display.update()
						pygame.time.wait(3000)
					turn += 1

			squares = pick_pice(board, colors[turn % 2],x,y)
			if board[x][y] == " " or board[x][y].color == colors[(turn+1) % 2]:
				piceselected = False

			else:
				piceselected = True
				squares = self_checking_move(board,x,y,squares,turn)
				x1,y1 = x,y
			
	pygame.display.update()
pygame.quit()
quit()