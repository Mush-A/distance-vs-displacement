import pygame 
import pygame.freetype
import sys
import time

# A simple program that demonstrates distance vs displacement (physics).

class Node:
	nodesRef = []

	def __init__(self):	
		self.pos = 0
		self.color = (255, 255, 255)

	def draw(self, display, event):
		check = self.mouse(event)
		if check:
			pos = self.mouse(event)
			self.nodesRef.append(pos)
			for j in range(1):
				display.fill((0,0,0))
				for i in range(len(self.nodesRef)):
					x = self.nodesRef[0 + i]
					pygame.draw.circle(display, self.color, x, 6)

	def mouse(self, event):
		pos = self.pos
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pos = pygame.mouse.get_pos()
				return pos
			else:
				return False
		else:
			return False

class Line:
	def __init__(self):
		self.color = (255, 0, 0)

	def draw(self, display, event):
		if self.mouse(event):
			length = 0
			array = Node.nodesRef
			for i in range(len(array) - 1):
				x = array[0 + i]
				y = array[1 + i]
				pygame.draw.line(display, (255, 0, 0), x, y, 4)
				length = 0
				for j in range(len(array) - 1):
					a = array[0 + j]
					b = array[1 + j]
					length += self.measure(a, b)
			text = pygame.freetype.Font("BLKCHCRY.ttf", 24)
			text.render_to(display, (10, 50), "Distance       : " + str(round(self.pxtocm(length))) + " cm" , (255, 0, 0))
			# print("Total distance:", round(length))
			# print("------------------------------")

	def displacement(self, display, event):
		if self.mouse(event):
			length = 0
			array = Node.nodesRef
			x = array[0]
			y = array[-1]
			pygame.draw.line(display, (0, 255, 0), x, y, 2)
			length = self.measure(x, y)
			text = pygame.freetype.Font("BLKCHCRY.ttf", 24)
			text.render_to(display, (10, 15), "Displacement: " + str(round(self.pxtocm(length))) + " cm" , (0, 255, 0))
			# print("displacement  :", round(length))
			# print("------------------------------")

	def measure(self, x, y):
		dl = ((y[0]-x[0])**2+((y[1]-x[1])**2))**0.5
		return dl

	def mouse(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				return True
			else:
				return False
		else:
			return False

	def pxtocm(self, value):
		cm = (2.54/96)*value
		return cm

def reset(display, event):
	text = pygame.freetype.Font("BLKCHCRY.ttf", 24)
	text.render_to(display, (1100, 15), "Reset", (255, 255, 255))
	if pygame.mouse.get_pos()[0] >= 1050 and pygame.mouse.get_pos()[1] >= 15:
		if pygame.mouse.get_pos()[0] <= 1150 and pygame.mouse.get_pos()[1] <= 40:
			text = pygame.freetype.Font("BLKCHCRY.ttf", 24)
			text.render_to(display, (1100, 15), "Reset", (255, 0, 0))
	if event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 1:
			if pygame.mouse.get_pos()[0] >= 1050 and pygame.mouse.get_pos()[1] >= 15:
				if pygame.mouse.get_pos()[0] <= 1150 and pygame.mouse.get_pos()[1] <= 40:
					del Node.nodesRef[:]
					display.fill((0, 0, 0))

def start(display):
	if len(Node.nodesRef) == 0:
		text = pygame.freetype.Font("BLKCHCRY.ttf", 50)
		text.render_to(display, (450, 350), "Click anywhere!", (255, 255, 255))

def main():
	screenWidth = 1200
	screenHeight = 700
	pygame.init()
	display = pygame.display.set_mode((screenWidth, screenHeight))
	pygame.display.set_caption("Distance Vs Displacement by @MushrafAltaf")
	pygame.display.set_icon(pygame.image.load("icon.png"))
	node = Node()
	line = Line()

	running = True
	while running:	

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			
			node.draw(display, event)
			line.draw(display, event)
			line.displacement(display, event)

			start(display)
			reset(display, event)
			pygame.display.update()
		time.sleep(1/100)

main()
