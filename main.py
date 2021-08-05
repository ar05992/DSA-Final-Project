from graph import Graph
import queue
from character import Character
import time
from collections import deque
import ui_file
import pygame
import random
import os

# function to set the position dof the display window
def SetWindowPosition(x, y):
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# creates a grid of size (asize)*(size)
def CreatingMatrix(area):

	# create a graph for the grid
	matrix = Graph()

	# add the vertices of the grid
	for i in range(area):
		for j in range(area):
			matrix.add_vertex((i,j))

	# return the constructed grid
	return matrix

# creates a maze when a grid and its vertices are passed in
def CreatingMaze(matrix, vertex, finish=None, points=None):
	
	if points is not None:
    		pass
	else:
		points = matrix.get_vertices()
	if finish is not None:
    		pass
	else:
		finish = [vertex]

	# select a random direction
	route = list(int(i) for i in range(4))
	random.shuffle(route)

	# vertices in the direction from current vertex
	right = (vertex[0]+1,vertex[1])
	left = (vertex[0]-1,vertex[1])
	down = (vertex[0],vertex[1]+1)
	up = (vertex[0],vertex[1]-1)

	for direction in route:
		if direction != 0:
    			pass
		else:
			if up in points and up not in finish:
				# add the edges
				matrix.add_edge((up,vertex))
				matrix.add_edge((vertex,up))
				finish.append(up)
				CreatingMaze(matrix, up, finish, points)
		if direction != 1:
    			pass
		else:
			if down in points and down not in finish:
				matrix.add_edge((vertex,down))
				matrix.add_edge((down,vertex))
				finish.append(down)
				CreatingMaze(matrix, down, finish, points)
		if direction != 2:
    			pass
		else:
			if left in points and left not in finish:
				matrix.add_edge((vertex,left))
				matrix.add_edge((left,vertex))
				finish.append(left)
				CreatingMaze(matrix, left, finish, points)
		if direction != 3:
    			pass
		else:
			if right in points and right not in finish:
    			
				matrix.add_edge((vertex,right))
				matrix.add_edge((right,vertex))
				finish.append(right)
				CreatingMaze(matrix, right, finish, points)

	return matrix

# draw maze function
# takes in a (size)x(size) maze and prints a "colour" path
# side_length is the length of the grid unit and border_width is its border thickness
def draw_maze(screen, maze, size, colour, side_length, border_width):
	# for every vertex in the maze:
	for i in range(size):
		for j in range(size):
			# if the vertex is not at the left-most side of the map
			if (i == 0):
    				pass
			else:
				# check if the grid unit to the current unit's left is connected by an edge
				if maze.is_edge(((i,j),(i-1,j))):
					# if connected, draw the grid unit without the left wall
					pygame.draw.rect(screen,colour,[(side_length+border_width)*i, border_width+(side_length+border_width)*j,\
									 side_length+border_width, side_length])
			# if the vertex is not at the right-most side of the map
			if (i == size-1):
    				pass
			else:
				if maze.is_edge(((i,j),(i+1,j))):
					# draw the grid unit without the right wall (extend by border_width)
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 border_width+(side_length+border_width)*j, side_length+border_width, side_length])
			# if the vertex is not at the top-most side of the map
			if (j == 0):
    				pass
			else:
				if maze.is_edge(((i,j),(i,j-1))):
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 (side_length+border_width)*j, side_length, side_length+border_width])
			# if the vertex is not at the bottom-most side of the map
			if (j == size-1):
    				pass
			else:
				if maze.is_edge(((i,j),(i,j+1))):
					pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
									 border_width+(side_length+border_width)*j, side_length, side_length+border_width])

# draw position of grid unit
def draw_position(screen, side_length, border_width, current_point, colour):
	pygame.draw.rect(screen, colour, [border_width+(side_length+border_width)*current_point[0],\
					 border_width+(side_length+border_width)*current_point[1], side_length, side_length])

# takes in a player2 character, maze, vertices, cooldown, and timer
def Player2(player2, maze, vertices, cooldown, timer):
	# get the pressed keys
	keys = pygame.key.get_pressed()
	
	if (pygame.time.get_ticks() - timer < cooldown):
    		pass
	else:
		current_point = player2.get_current_position()
		
		# move character left
		if keys[pygame.K_a]:
			if (current_point[0]-1,current_point[1]) in vertices:
				next_point = (current_point[0]-1, current_point[1])
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		
		# move character down
		if keys[pygame.K_s]:
			if (current_point[0],current_point[1]+1) in vertices:
				next_point = (current_point[0], current_point[1]+1)
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		
		# move character up
		if keys[pygame.K_w]:
			if (current_point[0],current_point[1]-1) in vertices:
				next_point = (current_point[0], current_point[1]-1)
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()
		
		# move character right
		if keys[pygame.K_d]:
			# check if the next point is in the maze
			if (current_point[0]+1, current_point[1]) in vertices:
				next_point = (current_point[0]+1, current_point[1])
				# check if the next point is connected by an edge
				if (maze.is_edge((current_point,next_point))):
					player2.move_character_smooth(next_point,5)
			# restart cooldown timer
			timer = pygame.time.get_ticks()

	return timer

# run the maze game
# takes in a game mode parameter along with grid size and side length for the maze
def runGame(matrix_size, side_length, mode):
	# initialize the game engine
	pygame.init()

	# Defining colours (RGB) ...
	GRAY = (100,100,100)
	GOLD = (249,166,2)
	BLACK = (0,0,0)
	BLUE = (0,0,255)
	GREEN = (0,255,0)
	WHITE = (255,255,255)
	RED = (255,0,0)
	

	# set the grid size and side length of each grid
	# grid_size = 20 # this is the maximum size before reaching recursion limit on maze buidling function
	# side_length = 10

	# initialize the grid for the maze
	matrix = CreatingMatrix(matrix_size)

	# scale the border width with respect to the given side length
	border_width = side_length//5

	
	# create the maze using the grid
	maze = CreatingMaze(matrix, (matrix_size//2,matrix_size//2)) # use the starting vertex to be middle of the map

	# Opening a window ...
	# set the screen size to match the grid
	size = (matrix_size*(side_length+border_width)+border_width,\
			matrix_size*(side_length+border_width)+border_width)
	
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("\"Esc\" to exit")

	# set the continue flag
	CarryOn = True

	# set the clock (how fast the screen updates)
	clock = pygame.time.Clock()

	# have a black background
	screen.fill(BLACK)

	# get all of the vertices in the maze
	vertices = maze.get_vertices()

	# draw the maze
	draw_maze(screen, maze, matrix_size, WHITE, side_length, border_width)

	# initialize starting point of character and potential character 2
	StartCoordinates = (0,0)
	# opposing corner
	start_point2 = (matrix_size-1,matrix_size-1)

	# set end-point for the maze
	end_point = (matrix_size-1,matrix_size-1)
	# initialize opponent's end-point for two player mode
	end_point2 = (0,0)

	# randomize a start and end point
	choice = random.randrange(4)

	if choice == 0:
		StartCoordinates = (matrix_size-1,matrix_size-1)
		start_point2 = (0,0)
		end_point = (0,0)
		end_point2 = (matrix_size-1,matrix_size-1)
	elif choice == 1:
		StarCoordinates = (0,matrix_size-1)
		start_point2 = (matrix_size-1,0)
		end_point = (matrix_size-1,0)
		end_point2 = (0,matrix_size-1)
	elif choice == 2:
		StartCoordinates = (matrix_size-1,0)
		start_point2 = (0,matrix_size-1)
		end_point = (0,matrix_size-1)
		end_point2 = (matrix_size-1,0)

	# initialize winner variable
	winner = 0

	# initialize the character
	player1 = Character(screen, side_length, border_width, vertices,\
						StartCoordinates, end_point, StartCoordinates, GREEN, WHITE)
	
	# if the two player game mode is selected, initialize the other character
	if mode == 1:
		player2 = Character(screen, side_length, border_width, vertices,\
							start_point2, end_point2, start_point2, BLUE, WHITE)
	
	# draw the end-point
	draw_position(screen, side_length, border_width, end_point, RED)
	# if two player mode, draw endpoints
	if mode == 1:
		draw_position(screen, side_length, border_width, end_point, GREEN)
		draw_position(screen, side_length, border_width, end_point2, BLUE)
	

	# update the screen
	pygame.display.flip()

	# set cooldown for key presses
	cooldown = 100

	# initialize the cooldown timer
	start_timer = pygame.time.get_ticks()

	# if the two player mode is selected, initialize the cooldown timer for second player
	if mode == 1:
		start_timer2 = pygame.time.get_ticks()

	# initialize game timer for solo mode
	game_timer = 0
	# if solo mode is selected, start game timer
	if mode == 0:
		game_timer = time.time()

	# main loop
	while CarryOn:
		# action (close screen)
		for event in pygame.event.get():# user did something
			if event.type == pygame.KEYDOWN:
    				#Pressing the Esc Key will quit the game
				if event.key == pygame.K_ESCAPE:
					CarryOn = False
					mode = -1
			elif event.type == pygame.QUIT:
				CarryOn = False
				# mode = -2 means just exit
				mode = -1
			

		# get the pressed keys
		keys = pygame.key.get_pressed()
		
		if (pygame.time.get_ticks() - start_timer < cooldown):
    			pass
		else:
			# get the current point of character
			current_point = player1.get_current_position()
			# move character right
			if keys[pygame.K_RIGHT]:
				# check if the next point is in the maze
				if (current_point[0]+1,current_point[1]) in vertices:
					next_point = (current_point[0]+1,current_point[1])
					# check if the next point is connected by an edge
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character left
			elif keys[pygame.K_LEFT]:
				if (current_point[0]-1,current_point[1]) in vertices:
					next_point = (current_point[0]-1, current_point[1])
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character up
			elif keys[pygame.K_UP]:
				if (current_point[0],current_point[1]-1) in vertices:
					next_point = (current_point[0], current_point[1]-1)
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()
			# move character down
			elif keys[pygame.K_DOWN]:
				if (current_point[0],current_point[1]+1) in vertices:
					next_point = (current_point[0], current_point[1]+1)
					if (maze.is_edge((current_point,next_point))):
						player1.move_character_smooth(next_point,5)
						
				# restart cooldown timer
				start_timer = pygame.time.get_ticks()

		# PLAYER 2 MOVEMENT HERE (if gamemode selected)
		if mode == 1:
			# update the start timer for player 2
			start_timer2 = Player2(player2, maze, vertices, cooldown, start_timer2)

			# redraw the finish points
			draw_position(screen, side_length, border_width, end_point, GREEN)
			draw_position(screen, side_length, border_width, end_point2, BLUE)
			# redraw the characters
			player2.draw_position()
			player1.draw_position()
			# update screen
			pygame.display.update()

		

		# win conditions for the different modes
		if mode == 0:
			if player1.reached_goal():
				CarryOn = False
		elif mode == 1:
			if player1.reached_goal():
				winner = 1
				CarryOn = False
			elif player2.reached_goal():
				winner = 2
				CarryOn = False

		# limit to 60 frames per second (fps)
		clock.tick(60)

	# stop the game engine once exited the game
	pygame.quit()

	# solo mode
	if mode == 0:
		timer = int(time.time() - game_timer)
		return mode, timer
	# other modes
	else:
		return mode, winner

# main function
if __name__ == "__main__":

	# set the window display position
	SetWindowPosition(50,50)

	# initialize states
	states = {0:"Main Menu", 1:"Gameplay"}
	current_state = states[0]

	# initialize variables
	matrix_size = 0
	side_length = 0
	mode = 0

	# flag for main loop
	Run = True

	while Run:
		if current_state == states[0]:
			Run, matrix_size, side_length, mode = ui_file.startScreen()
			current_state = states[1]
		elif current_state == states[1]:
			mode, value = runGame(matrix_size, side_length, mode)
			if mode != -1:
				ui_file.endGame(mode, value)

			current_state = states[0]

	
	quit()