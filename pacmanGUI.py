#!/usr/bin/env python3

import pacmanBFS
import escape
import pygame
import train


block_size = 50
time_init = 0
total_games = 10
show_game = 5
bot = True

class Game :
	def __init__(self, filename = 'pacmanMatrix'):
		fp = open(filename,'r')
		data = fp.readlines()
		self.matrix = []
		self.row = len(data)
		self.col = None
		self.score = 0
		self.ghost = ()
		self.ghost_prev = ()
		self.time = time_init
		self.over = False
		self.win = False
		self.pac = ()
		self.pac_prev = ()
		self.fruit = ()
		self.fruitOrg = ()
		self.pacOrg = ()
		self.ghostOrg = ()
		i = 0
		for line in data:
			self.col = len(line) - 1
			self.matrix.append([])
			j = 0
			for j in range(len(line) - 1):
				self.matrix[i].append(' ')
				if line[j] == 'p':
					self.pac = (i,j)
				elif line[j] == 'g':
					self.ghost += ((i,j),)
				elif line[j] == '#':
					self.matrix[i][j] = '#'
				elif line[j] == 'f':
					#self.matrix[i][j] = 'f'
					self.fruit += ((i,j),)
			i += 1
		self.fruitOrg = self.fruit
		self.pacOrg = self.pac
		self.ghostOrg = self.ghost

	def reset(self):
		self.score = 0
		self.ghost = self.ghostOrg
		self.time = time_init
		self.over = False
		self.win = False
		self.pac = self.pacOrg
		self.fruit = self.fruitOrg

	def display(self):
		s = ''
		for i in range(self.row):
			for j in range(self.col):
				s += self.matrix[i][j]
			s += '\n'
		print(s)

	def valid(self, i, j):
		if i >= 0 and i < self.row and j >= 0 and j < self.col:
			if self.matrix[i][j] != '#':
				return True
			return False
		return False

	def eat(self):
		fruit = ()
		ghost = ()
		win = False
		game_over = False
		for i,j in self.fruit:
			if (i,j) == self.pac:
				self.time = 40
			else:
				fruit += ((i,j),)
		self.fruit = fruit

		for i,j in self.ghost:
			if (i,j) == self.pac:
				if self.time == 0:
					win = False
					game_over = True
					ghost += ((i,j),)
			else:
				ghost += ((i,j),)
		self.ghost = ghost

		if len(self.ghost) == 0:
			win = True
			game_over = True
		self.over = game_over
		self.win = win

	def lose(self):
		if self.win == True : 
			print('You Won')
			print('Your time = ', self.score)
		else:
			print('Game Over')

	def action(pressed):
		move = None
		if pressed[pygame.K_UP] and G.valid(G.pac[0] - 1, G.pac[1]): 
			move = 0
		elif pressed[pygame.K_DOWN] and G.valid(G.pac[0] + 1, G.pac[1]): 
			move = 1
		elif pressed[pygame.K_LEFT] and G.valid(G.pac[0], G.pac[1] - 1): 
			move = 2
		elif pressed[pygame.K_RIGHT] and G.valid(G.pac[0], G.pac[1] + 1):
			move = 3
		return move

class window:
	def __init__(self, row, col):
		pygame.init()
		self.background = (33, 33, 33)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((col * block_size, row * block_size))
		pygame.display.set_caption('Pacman')
		self.store = {}

		# Left Pacman
		image = pygame.image.load('Images/pac.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_left1'] = image
		image = pygame.image.load('Images/pac1.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_left2'] = image

		# Right Pacman
		image = pygame.image.load('Images/pac_right.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_right1'] = image
		image = pygame.image.load('Images/pac1_right.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['pac_right2'] = image
		
		# Fruit
		image = pygame.image.load('Images/fruit.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['fruit'] = image

		# Obstacle
		image = pygame.image.load('Images/block.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['block'] = image
		
		# Ghost
		image = pygame.image.load('Images/red_ghost.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['red_ghost'] = image
		image = pygame.image.load('Images/cold_ghost.jpg')
		image = pygame.transform.scale(image, (block_size, block_size))
		self.store['cold_ghost'] = image

		# Game Over
		image = pygame.image.load('Images/game_over.jpg')
		image = pygame.transform.scale(image, (col * block_size, row * block_size // 4))
		self.store['game_over'] = image
		
		# Win
		image = pygame.image.load('Images/win.jpg')
		image = pygame.transform.scale(image, (col * block_size, row * block_size // 2))
		self.store['win'] = image

		# start screen
		image = pygame.image.load('Images/pacman.jpeg')
		image = pygame.transform.scale(image, (col * block_size, row * block_size))
		self.store['start'] = image

		# training
		image = pygame.image.load('Images/karate.png')
		image = pygame.transform.scale(image, (col * block_size, row * block_size))
		self.store['train'] = image




	def display(self, matrix, time, direct, even, pac, ghost, fruit):
		self.screen.fill(self.background)
		row = len(matrix)
		col = len(matrix[0])
		for i in range(row):
			for j in range(col):
				if matrix[i][j] == ' ':
					continue
				if matrix[i][j] == '#':
					self.screen.blit(self.store['block'], (block_size * j, block_size * i))
				#else :
				#	self.screen.blit(self.store['fruit'], (block_size * j, block_size * i))
		

		for i, j in fruit:
			coord = (block_size * j, block_size * i)
			self.screen.blit(self.store['fruit'], coord)
		# Ghost and Pacman
		coord = (block_size * pac[1], block_size * pac[0])
		if direct == 0:
			if even:
				self.screen.blit(self.store['pac_left1'], coord)
			else:
				self.screen.blit(self.store['pac_left2'], coord)
		else:
			if even:
				self.screen.blit(self.store['pac_right1'], coord)
			else:
				self.screen.blit(self.store['pac_right2'], coord)
		for i, j in ghost:
			coord = (block_size * j, block_size * i)
			if time > 8 or time % 2:
				self.screen.blit(self.store['cold_ghost'], coord)
			else:
				self.screen.blit(self.store['red_ghost'], coord)



'''
	move = 0 -> up
	move = 1 -> down
	move = 2 -> left
	move = 3 -> right

'''
def main() :

	G = Game()
	Win = window(G.row, G.col)
	Win.screen.blit(Win.store['train'], (0, 0))
	pygame.display.flip()
	for eps in range(total_games):
		G.reset()
		G.pac_prev = G.pac
		G.ghost_prev = G.ghost
		game = True
		direct = 0
		move = -1
		delay = 2
		over = 0
		df = 5
		dg = 5
		r, c = G.pac
		even = 0
		if eps > total_games - show_game:
			Win.screen.blit(Win.store['start'], (0, 0))
			pygame.display.flip()
			Win.clock.tick(0.5)

		while game:
			#Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game = False
					return
			if bot == False:
				pressed = pygame.key.get_pressed()
				move = G.action(pressed)
			else:
				move = train.Qlearning(G.pac, G.pac_prev, G.ghost_prev, G.ghost, len(G.fruitOrg), G.fruit, over, dg, df, G.time)

			if move == 2:
				direct = 0
			elif move == 3:
				direct = 1

			if move == 0 and G.valid(G.pac[0] - 1, G.pac[1]):
				r = max(r - 1, 1)
			elif move == 1 and G.valid(G.pac[0] + 1,G.pac[1]):
				r = min(r + 1, G.row - 2)
			elif move == 2 and G.valid(G.pac[0], G.pac[1] - 1):
				c = max(c - 1, 1)
			elif move == 3 and G.valid(G.pac[0], G.pac[1] + 1):
				c = min(c + 1,G.col - 2)

			G.matrix[G.pac[0]][G.pac[1]] = ' '
			for i,j in G.ghost:
				G.matrix[i][j] = ' '

			G.pac_prev = G.pac
			G.pac = (r, c)
			G.ghost_prev = G.ghost
			G.eat()
			if G.over == False:
				over = 0
			elif G.win == True:
				over = 1
			else:
				over = -1

			if G.over == True:
				if eps > total_games - show_game:
					Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost, G.fruit)
				break
			
			if delay % 2:
				if G.time:
					G.ghost, dg, df = pacmanBFS.BFS(G.matrix, G.ghost, G.row, G.col, G.pac, G.fruit)
					G.ghost = escape.BFS(G.matrix, G.ghost_prev, G.row, G.col, G.pac)
				else:
					G.ghost, dg, df = pacmanBFS.BFS(G.matrix, G.ghost, G.row, G.col, G.pac, G.fruit)
			
			delay = (delay + 1) % 2
			even = (even + 1) % 2
			Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost, G.fruit)
			G.eat()

			if G.over == False:
				over = 0
			elif G.win == True:
				over = 1
			else:
				over = -1

			if G.over == True:
				if eps > total_games - show_game:
					Win.display(G.matrix, G.time, direct, even, G.pac, G.ghost, G.fruit)
				break
			if len(G.fruit) == 0:
				G.fruit = G.fruitOrg
			G.score += 1
			G.time = max(0, G.time - 1)
			if eps > total_games - show_game:
				Win.clock.tick(4)
				pygame.display.flip()
		move = train.Qlearning(G.pac, G.pac_prev, G.ghost_prev, G.ghost, len(G.fruitOrg), G.fruit, over, dg, df, G.time)

		if eps > total_games - show_game:
			if G.win == False:
				Win.screen.blit(Win.store['game_over'], (0, 2 * block_size))
			else:
				Win.screen.blit(Win.store['win'], (0, 2 * block_size))
			pygame.display.flip()
			Win.clock.tick(1)

	

if __name__ == '__main__':
	#train.E.reinit()
	main()
	train.E.write()
