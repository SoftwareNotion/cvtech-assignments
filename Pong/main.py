# Imports
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init() 

# Generate Window
bgColor = (0, 0, 0)
screen = pygame.display.set_mode((800, 800))
screen.fill(bgColor)
clock = pygame.time.Clock()
FPS = 30

# Set Window Icon & Name
programIcon = pygame.image.load('connor.jpg')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Pong Project')

# --Objects--
# Paddles
class Paddle1:
    def __init__(self):
        self.pos = [0, 0]
        self.shape = [50, 100]
        self.paddle = pygame.Rect(self.pos[0], self.pos[1], self.shape[0], self.shape[1])
        self.status = "normal"
        self.color = 0, 100, 255
        self.speed = 15

    def draw(self):
        pygame.draw.rect(screen, self.color, self.paddle)

    def movement(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[K_w]:
            self.pos[1] += self.speed
            # self.paddle.y += self.speed
        elif keyPressed[K_s]:
            self.pos[1] -= self.speed
            # self.paddle.y -= self.speed
        else:
            pass
        self.paddle.y = self.pos[1]


# --Update Dispaly--
leftPaddle = Paddle1()
running = True
while running:
    leftPaddle.draw()
    leftPaddle.movement()

    print(leftPaddle.pos[1])

    for event in pygame.event.get():        
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()
    clock.tick(FPS)