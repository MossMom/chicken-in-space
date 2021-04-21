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
controller = pygame.joystick.Joystick(0) #grab a controller from the operating system, hold in this variable
controller.init() #sets up controller
key = [False, False, False, False] #python array to hold controller key values (they all start not pressed)
button = [False, False, False] #python array to hold controller button values (they all start not pressed) X A B
movingUp = False
movingLeft = False
movingDown = False
movingRight = False
eat = False
sleep = False
sprinting = False

class pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.circle(screen, (white), (self.x, self.y), 1)

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
            
        if event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN: #check for controller input
            hat = controller.get_hat(0) #the hat is the flat cross-shaped button (as opposed to stick or button)
            button = controller.get_button(0) #the button variable?
            
            #LEFT
            if hat[0] < 0:
                key[0] = True
                movingLeft = True
            else:
                key[0] = False
                movingLeft = False
               
            #UP
            if hat[1] > 0:
                key[2] = True
                movingUp = True
            else:
                key[2] = False
                movingUp = False
            
            #RIGHT
            if hat[0] > 0:
                key[3]= True
                movingRight = True
            else:
                key[3] = False
                movingRight = False
           
            #DOWN
            if hat[1] < 0:
                key[1] = True
                movingDown = True
            else:
                key[1] = False
                movingDown = False
                
            #SPRINT
            if controller.get_button(2) == True: 
                sprinting = True 
            else:
                sprinting = False
            
            #EAT
            if controller.get_button(0) == True: 
                eat = True 
            else:
                eat = False
            
            #SLEEP
            if controller.get_button(1) == True: 
                sleep = True 
            else:
                sleep = False
            
            

    keys = pygame.key.get_pressed()#keyboard
    
    if key[0] or key[1] or key[2] or key[3] or keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s] or eating == True or sleeping == True:
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
    
    if keys[pygame.K_q] or eat == True: #eat
        eating = True
        sleeping = False
        if eating == True:
            animating = True
            if LR == 1:
                extra = width*12
            if LR == 2:
                extra = width*13
                
    if keys[pygame.K_e] or sleep == True: #sleep
        sleeping = True
        eating = False
        if sleeping == True:
            animating = True
            if LR == 1: #check if facing left
                extra = width*6
            if LR == 2: #check if facing left
                extra = width*7
                        
    
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] or sprinting == True: #sprint
        speed = 4
    else:
        speed = 2
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or movingLeft == True: #left
        xV=speed*-1
        extra = width*2
        LR = 1
        eating = False
        sleeping = False
            
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] or movingRight == True: #right
        xV=speed
        extra = width*3
        LR = 2
        eating = False
        sleeping = False
            
    if keys[pygame.K_UP] or keys[pygame.K_w] or movingUp == True: #up
        yV=speed*-1
        extra = width
        eating = False
        sleeping = False
        if LR == 1:
            extra = width*4
        else:
            if LR == 2:
                extra = width*5
            
    if keys[pygame.K_DOWN] or keys[pygame.K_s] or movingDown == True: #down
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
    
    
