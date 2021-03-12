import pygame 
import pygame.freetype
import sys
import time

class Node:
	nodesRef = []

	def __init__(self, color):
		self.color = (255, 255, 255)

	def draw(self, pos, display, thickness):
		pygame.draw.circle(display, self.color, pos, thickness)

	def mouse(self):
		return pygame.mouse.get_pos()

	def click(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				return True
			else:
				return False
		else:
			return False

	def register(self, display, event):
		if self.click(event):
			pos = self.mouse()
			self.nodesRef.append(pos)
			for j in range(1):
				display.fill((0,0,0))
				for i in range(len(self.nodesRef)):
					x = self.nodesRef[0 + i]
					self.draw(x, display, 6)

class Line:

	def __init__(self, color):
		self.color = color

	def draw(self, display, color, x, y, thickness):
		pygame.draw.line(display, color, x, y, thickness)

	def click(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				return True
			else:
				return False
		else:
			return False

	def distance(self, display, event, color):
		if self.click(event):
			length = 0
			array = Node.nodesRef
			for i in range(len(array) - 1):
				x = array[0 + i]
				y = array[1 + i]
				self.draw(display, color, x, y, 4)
				length = 0
				for j in range(len(array) - 1):
					a = array[0 + j]
					b = array[1 + j]
					length += self.measure(a, b)
			print(length)

	def displacement(self, display, event, color):
		if self.click(event):
			length = 0
			array = Node.nodesRef
			x = array[0]
			y = array[-1]
			self.draw(display, color, x, y, 4)
			length = self.measure(x, y)

	def measure(self, x, y):
		dl = ((y[0]-x[0])**2+((y[1]-x[1])**2))**0.5
		return dl

class Text:
	def __init__(self, color, font):
		self.color = color
		self.font = font

	def converter(self, unit):
		pass

	def text(self, size, pos, color, unit):
		text = pygame.freetype.Font(self.pos, size)
		text.render_to(display, pos, value , (0, 255, 0))




def main():
	screenWidth = 1200
	screenHeight = 700
	pygame.init()
	display = pygame.display.set_mode((screenWidth, screenHeight))
	pygame.display.set_caption("Distance Vs Displacement by @MushrafAltaf")
	pygame.display.set_icon(pygame.image.load("icon.png"))
	node = Node((255, 255, 255))
	line = Line((255, 255, 255))

	running = True
	while running:	

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			node.register(display, event)
			line.distance(display, event, (255, 0, 255))
			line.displacement(display, event, (255, 255, 0))
			pygame.display.update()

		time.sleep(1/100)

main()
