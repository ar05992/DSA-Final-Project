'''
Character class
'''

import pygame
from time import sleep

class Character:

	def __init__(self, screen, side_length, border_width, valid_points, start_point, end_point, current_position, a_colour, na_colour,\
				keys=None, k_colour=None):

		self.screen = screen # pygame screen
		self.side_length = side_length # length of the grid unit
		self.border_width = border_width # border width of the grid unit
		self.start_point = start_point # starting point of character in maze stored as a tuple
		self.end_point = end_point # end point of character in maze (tuple)
		self.current_position = current_position # current position of character (tuple)
		self.a_colour = a_colour # active colour of the character (tuple of 3 elements) RGB colour
		self.na_colour = na_colour # inactive colour of the character (tuple of 3 elements) RGB colour
		
			
		# draw the initial position of the character
		self.draw_position()

	# draw the character
	def draw_position(self):
		pygame.draw.rect(self.screen, self.a_colour, [self.border_width+(self.side_length+self.border_width)*self.current_position[0],\
			self.border_width+(self.side_length+self.border_width)*self.current_position[1], self.side_length, self.side_length])

	# move the character to next position
	def move_character(self, next_position):
		# create a rectangle for the current position
		current_rect = [self.border_width+(self.side_length+self.border_width)*self.current_position[0],\
						self.border_width+(self.side_length+self.border_width)*self.current_position[1],\
						self.side_length, self.side_length]
		# create a rectangle for the next position
		next_rect = [self.border_width+(self.side_length+self.border_width)*next_position[0],\
					 self.border_width+(self.side_length+self.border_width)*next_position[1],\
					 self.side_length, self.side_length]
		# draw the previous position of the character as an inactive block
		pygame.draw.rect(self.screen, self.na_colour, current_rect)
		# update the screen at the current point
		pygame.display.update(current_rect)
		# draw the next position of the character
		pygame.draw.rect(self.screen, self.a_colour, next_rect)
		# update the screen at the next point
		pygame.display.update(next_rect)
		# update the current position of the character to the next position
		self.current_position = next_position


	# draw the intermediate steps when moving a character
	def move_character_smooth(self, next_position, steps):
		# go right
		if next_position[0] != self.current_position[0]:
			# from i = 1 to steps
			for i in range(1,steps+1):
				# short delay between each intermediate step
				sleep(0.005)
				difference = (next_position[0]-self.current_position[0])*i/steps
				next_pos = (self.current_position[0]+difference, self.current_position[1])
				self.move_character(next_pos)
		else:
			for i in range(1,steps+1):
				sleep(0.005)
				difference = (next_position[1]-self.current_position[1])*i/steps
				next_pos = (self.current_position[0], self.current_position[1]+difference)
				self.move_character(next_pos)

	# return the current position of the character
	def get_current_position(self):
		return self.current_position

	# end goal flag
	def reached_goal(self):
		if self.current_position == self.end_point:
			return True
		else:
			return False

