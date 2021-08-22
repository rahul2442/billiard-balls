import pygame
import random 
import math

pygame.init()

width=600
height=600
bg_color=(0,0,0)

display=pygame.display.set_mode((width,height))

class Ball:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.size=50
		self.color=(0,0,255)
		self.speed=0.01
		self.angle=0

	def display(self):
		pygame.draw.circle(display,self.color,(int(self.x),int(self.y)),self.size)

	def move(self):
		self.x+=math.sin(self.angle)*self.speed
		self.y+=math.cos(self.angle)*self.speed

	def bounce(self):
		if self.x>=width-self.size:
			self.x=width-self.size
			self.angle=-self.angle

		elif self.x<self.size:
			self.x=self.size
			self.angle=-self.angle

		if self.y>=height-self.size:
			self.y=height-self.size
			self.angle=math.pi-self.angle
		elif self.y<=self.size:
			self.y=self.size
			self.angle=math.pi-self.angle

def collision(curr,nxt):
	dx=curr.x-nxt.x
	dy=curr.y-nxt.y
	distance=math.hypot(dx,dy)
	if distance<=curr.size+nxt.size:
		tangent_angle=math.atan2(dy,dx)
		curr.angle=math.pi-(tangent_angle+curr.angle)
		nxt.angle=math.pi-(tangent_angle+nxt.angle)

		(curr.speed,nxt.speed)=(nxt.speed,curr.speed)

		angle=math.pi*0.5 + tangent_angle

		curr.x+=math.sin(angle)
		curr.y-=math.cos(angle)
		nxt.x-=math.sin(angle)
		nxt.y+=math.cos(angle)

code_hub_=pygame.image.load('icon.png')
my_particles=[]
no_of_particles=7

for i in range(no_of_particles):
	x=random.randint(50,550)
	y=random.randint(50,550)
	particle=Ball(x,y)
	particle.size=random.randint(10,40)
	particle.speed=random.random()
	particle.angle=random.uniform(0,math.pi)
	my_particles.append(particle)




run=True


while loop:
	display.fill(bg_color)
	display.blit(code_hub_,(520,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

	for i,ball in enumerate(my_particles):
		ball.bounce()
		ball.move()
		for x in my_particles[i+1:]:
			collision(ball,x)
		ball.display()


	pygame.display.update()
