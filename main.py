import pygame
import copy

FPS = 50
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 128, 255)
ORANGE = (255, 100, 0)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

WHight = 600
WWidght = WHight + 100


#pygame.mixer.init()
#pygame.mixer.music.load('musicc.mp3')

pygame.init()
screen = pygame.display.set_mode((WWidght, WHight))

font = pygame.font.Font(None, 42)
p1 = font.render("P1", True, BLACK)
p2 = font.render("P2", True, BLACK)


done = False

x = [0,0,0]
y = [0,0,0]
direc = [0,0,0]

x[1] = WHight/2 - 100
y[1] = WHight/2

x[2] = WHight/2 + 100
y[2] = WHight/2

side = 4

n = WHight/side

temp = [True,]*n
CanGo = [0]*n
for i in xrange(n):
    CanGo[i]=copy.deepcopy(temp)

direc[1] = UP
direc[2] = UP

speed = side

Points = [0,0,0]

def NewGame():
    global x
    x = [0,0,0]
    global y 
    y = [0,0,0]
    global direc 
    direc = [0,0,0]
    
    x[1] = WHight/2 - 100
    y[1] = WHight/2
    
    x[2] = WHight/2 + 100
    y[2] = WHight/2
    
    side = 4
    
    n = WHight/side
    global CanGo
    temp = [True,]*n
    CanGo = [0]*n
    for i in xrange(n):
        CanGo[i]=copy.deepcopy(temp)
    
    direc[1] = UP
    direc[2] = UP
    
    speed = side
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, BLACK , pygame.Rect(0, 0, WHight, WHight))
    
    pygame.draw.rect(screen, BLUE, pygame.Rect(x[1], y[1], side, side))
    pygame.draw.rect(screen, ORANGE, pygame.Rect(x[2], y[2], side, side))
    
    screen.blit(p1,
        [WWidght - p1.get_width()+10, 10])

def chgDir(plNum, direct):
    if direct == UP:
        direc[plNum]=UP
    elif direct == DOWN:
        direc[plNum]=DOWN
    elif direct == LEFT:
        direc[plNum]=LEFT
    elif direct == RIGHT:
        direc[plNum]=RIGHT  
        
def go(plNum):
    if direc[plNum] == UP:
        y[plNum]-=speed
    if direc[plNum] == DOWN:
        y[plNum]+=speed
    if direc[plNum] == LEFT:
        x[plNum]-=speed
    if direc[plNum] == RIGHT:
        x[plNum]+=speed      

def setKvadrs():
    CanGo[x[1]/side][y[1]/side] = False
    CanGo[x[2]/side][y[2]/side] = False
    
def gameIsOver():
    return x[1]/side<0 or x[1]/side>=n or   \
        x[2]/side<0 or x[2]/side>=n or      \
        y[1]/side<0 or y[1]/side>=n or      \
        y[2]/side<0 or y[2]/side>=n or      \
        not CanGo[x[1]/side][y[1]/side] or not CanGo[x[2]/side][y[2]/side] 

def whoWin():
    if   x[1]/side<0 or x[1]/side>=n or   \
        y[1]/side<0 or y[1]/side>=n or     \
        not CanGo[x[1]/side][y[1]/side] :
        return 2
    else:
        return 1  
    
speed = side

clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.draw.rect(screen, BLACK , pygame.Rect(0, 0, WHight, WHight))

pygame.draw.rect(screen, BLUE, pygame.Rect(x[1], y[1], side, side))
pygame.draw.rect(screen, ORANGE, pygame.Rect(x[2], y[2], side, side))

#pygame.mixer.music.play(-1)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_SPACE]:
            NewGame()
            gameEnd = False
            while not gameEnd:
                pygame.event.pump()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]: 
                    if direc[1] == LEFT or direc[1] == RIGHT: 
                        direc[1] = UP
                if pressed[pygame.K_DOWN]: 
                    if direc[1] == LEFT or direc[1] == RIGHT: 
                        direc[1] = DOWN
                if pressed[pygame.K_LEFT]:
                    if direc[1] == UP or direc[1] == DOWN: 
                        direc[1] = LEFT            
                if pressed[pygame.K_RIGHT]:
                    if direc[1] == UP or direc[1] == DOWN: 
                        direc[1] = RIGHT 
                
                if pressed[pygame.K_w]: 
                    if direc[2] == LEFT or direc[2] == RIGHT: 
                        direc[2] = UP
                if pressed[pygame.K_s]:
                    if direc[2] == LEFT or direc[2] == RIGHT: 
                        direc[2] = DOWN
                if pressed[pygame.K_a]:
                    if direc[2] == UP or direc[2] == DOWN: 
                        direc[2] = LEFT         
                if pressed[pygame.K_d]:
                    if direc[2] == UP or direc[2] == DOWN: 
                        direc[2] = RIGHT 
                        
                        
                #screen.fill((255, 255, 255))
                
                pygame.draw.rect(screen, BLUE, pygame.Rect(x[1], y[1], side, side))
                pygame.draw.rect(screen, ORANGE, pygame.Rect(x[2], y[2], side, side))
                
                go(1)
                go(2)
                gameEnd = gameIsOver()
                if not gameEnd:
                    setKvadrs()
                
                pygame.display.flip()
                clock.tick(FPS)
            Points[whoWin()]+=1
            print "GameOver!"
        pygame.display.flip()
        clock.tick(FPS)