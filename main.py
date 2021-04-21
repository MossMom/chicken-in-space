import pygame
import random

pygame.init()

screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption('A Chicken Exploring Space')
image = pygame.image.load('chickens.png')
clock = pygame.time.Clock()

#variables
xpos = 400
ypos = 100
xV = 0
yV = 0
ticker = 0
counter = 0
speed = 2
fps = 60
maxframes = 7
black = (0, 0, 0)
white = (255, 255, 255)
scale = 48
height = 48
width = 48
extra = 0
LR = 1 #left = 1 | right = 2
UD = 2 #up = 1 | down = 2
animating = False
eating = False
sleeping = False
angle = 0

class pellet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (white), (self.xpos, self.ypos), 1)

stars = list()
for i in range(50):
    stars.append(pellet(random.randint(1, screenwidth),random.randint(1, screenheight)))

while True: #GAME LOOP
    random.seed()
    clock.tick(fps)
#input/output section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s] or eating == True or sleeping == True:
        animating = True
    else:
        counter = 0
        animating = False
        
    if animating == True: #sets up animation speed n frame switch
        ticker+=1
        if ticker>maxframes*2/(.5*speed):
            ticker=0
            counter+=1
        if counter>maxframes:
            counter=0
    
    if keys[pygame.K_q]: #eat
        eating = True
        sleeping = False
        if eating == True:
            animating = True
            if LR == 1:
                extra = width*12
            if LR == 2:
                extra = width*13
                
    if keys[pygame.K_e]: #sleep
        sleeping = True
        eating = False
        if sleeping == True:
            animating = True
            if LR == 1: #check if facing left
                extra = width*6
            if LR == 2: #check if facing left
                extra = width*7
                        
    
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: #sprint
        speed = 4
    else:
        speed = 2
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: #left
        xV=speed*-1
        extra = width*2
        LR = 1
        eating = False
        sleeping = False
            
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #right
        xV=speed
        extra = width*3
        LR = 2
        eating = False
        sleeping = False
            
    if keys[pygame.K_UP] or keys[pygame.K_w]: #up
        yV=speed*-1
        extra = width
        eating = False
        sleeping = False
        if LR == 1:
            extra = width*4
        else:
            if LR == 2:
                extra = width*5
            
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: #down
        yV=speed
        extra = width
        eating = False
        sleeping = False
        if LR == 1:
            extra = width*0
        else:
            if LR == 2:
                extra = width*1
    
    xpos+=xV #add velocity to speed
    ypos+=yV #add velocity to speed
    
    if ypos>screenheight-height: #these keep you on screen
        ypos=screenheight-height
    if ypos<0:
        ypos=0
    if xpos>screenwidth-width:
        xpos=screenwidth-width
    if xpos<0:
        xpos=0
    
    xV*=0.98 #friction in space for some reason
    yV*=0.98 #friction in space for some reason
    
    
#render section
    screen.fill(black)
    
    for i in range(50):
        stars[i].draw()
    
    screen.blit(image, (xpos,ypos), (extra,0+counter*scale,width,height))
    
    pygame.display.flip() 
    
    
