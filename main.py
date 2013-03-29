import pygame
import copy

FPS = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE =  (0, 128, 255)
LBLUE = (0, 255, 255)
ORANGE = (255, 100, 0)
LORANGE = (255, 255, 0)
GRAY = (50,50,50)

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

WHight = 600
WWidght = WHight + 100
side = 4
speed = side
n = WHight/side

Points = [0,0,0]

Player1 = "Player1"
Player2 = "Player2"

class ExitEx:
    pass

pygame.mixer.init()
pygame.mixer.music.load('musicc.mp3')
splash = pygame.image.load('splash.jpg')

pygame.init()
pygame.display.set_caption("The TRON Game!")
screen = pygame.display.set_mode((WWidght, WHight))

WLFont = font = pygame.font.Font(None, 72)
font = pygame.font.Font(None, 36)
InstructFont = pygame.font.Font(None, 20)
PlayerText1 = font.render(Player1, True, BLUE)
PlayerText2 = font.render(Player2, True, ORANGE)
toRend = ["P1 - arrows","P2 - wasd","Press","SPASE","to start","new game.","Who get","10 points","will win!"]
HelpText = [InstructFont.render(x, True, WHITE) for x in toRend]

x = None
y = None
direc = None
CanGo = None

def DrawScore():
    PlayerScore1 = font.render(str(Points[1]), True, LBLUE)
    PlayerScore2 = font.render(str(Points[2]), True, LORANGE)
    pygame.draw.rect(screen, GRAY , pygame.Rect(WWidght-100, 0, 100, WHight))
    screen.blit(PlayerText1,
        [WWidght - 50 - (PlayerText1.get_width()/2), 10])
    screen.blit(PlayerText2,
        [WWidght - 50 - (PlayerText2.get_width()/2), 80])
    screen.blit(PlayerScore1,
        [WWidght - 50 - (PlayerScore1.get_width()/2), 40])
    screen.blit(PlayerScore2,
        [WWidght - 50 - (PlayerScore2.get_width()/2), 110])
    textPosY = 200
    i = 0
    while(i<len(HelpText)):
        screen.blit(HelpText[i],
                    [WWidght - 50 - (HelpText[i].get_width()/2), textPosY])
        i+=1
        textPosY+=30

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
    
    global CanGo
    temp = [True,]*n
    CanGo = [0]*n
    for i in xrange(n):
        CanGo[i]=copy.deepcopy(temp)
    
    direc[1] = UP
    direc[2] = UP
    
    
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK , pygame.Rect(0, 0, WHight, WHight))
    pygame.draw.rect(screen, LBLUE, pygame.Rect(x[1], y[1], side, side))
    pygame.draw.rect(screen, LORANGE, pygame.Rect(x[2], y[2], side, side))
    
    DrawScore()

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

def playerLose(num):
    return x[num]/side<0 or x[num]/side>=n or   \
        y[num]/side<0 or y[num]/side>=n or      \
        not CanGo[x[num]/side][y[num]/side] 
        
def gameIsOver():
    return (x[1]==x[2] and y[1]==y[2]) or playerLose(1) or playerLose(2)

def whoWin():
    if (x[1]==x[2] and y[1]==y[2]) or (playerLose(1) and playerLose(2)):
        return 0
    elif  playerLose(1):
        return 2
    else:
        return 1  
    

clock = pygame.time.Clock()

screen.fill(WHITE)

pygame.mixer.music.play(-1)

done = False
NewGame()

screen.blit(splash, (0, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        try:                
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                pygame.event.pump()
                Points = [0,0,0]
                while(max(Points)<10):
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    done = True
                                    raise ExitEx
                    pygame.event.pump() 
                    NewGame()
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_SPACE]:
                        pygame.event.pump()
                        setKvadrs()
                        gameEnd = False
                        while not gameEnd:    
                            pygame.event.pump()
                            pressed = pygame.key.get_pressed()
                            if pressed[pygame.K_UP]: 
                                if direc[1] == LEFT or direc[1] == RIGHT: 
                                    direc[1] = UP
                            elif pressed[pygame.K_DOWN]: 
                                if direc[1] == LEFT or direc[1] == RIGHT: 
                                    direc[1] = DOWN
                            elif pressed[pygame.K_LEFT]:
                                if direc[1] == UP or direc[1] == DOWN: 
                                    direc[1] = LEFT            
                            elif pressed[pygame.K_RIGHT]:
                                if direc[1] == UP or direc[1] == DOWN: 
                                    direc[1] = RIGHT 
                            
                            if pressed[pygame.K_w]: 
                                if direc[2] == LEFT or direc[2] == RIGHT: 
                                    direc[2] = UP
                            elif pressed[pygame.K_s]:
                                if direc[2] == LEFT or direc[2] == RIGHT: 
                                    direc[2] = DOWN
                            elif pressed[pygame.K_a]:
                                if direc[2] == UP or direc[2] == DOWN: 
                                    direc[2] = LEFT         
                            elif pressed[pygame.K_d]:
                                if direc[2] == UP or direc[2] == DOWN: 
                                    direc[2] = RIGHT 
                                    
                            
                            pygame.draw.rect(screen, BLUE, pygame.Rect(x[1], y[1], side, side))
                            pygame.draw.rect(screen, ORANGE, pygame.Rect(x[2], y[2], side, side))
                            
                            go(1)
                            go(2)
                            pygame.draw.rect(screen, LBLUE, pygame.Rect(x[1], y[1], side, side))
                            pygame.draw.rect(screen, LORANGE, pygame.Rect(x[2], y[2], side, side))
                            gameEnd = gameIsOver()
                            if not gameEnd:
                                setKvadrs()
                            
                            pygame.display.flip()
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                            done = True
                                            raise ExitEx
                            
                        isWin = whoWin()
                        if isWin!=0:
                            Points[isWin]+=1
                        
                        print "GameOver!"
                        DrawScore()
                if Points[1]>=10:
                    WinText = WLFont.render(Player1+" win!", True, RED)
                else:
                    WinText = WLFont.render(Player2+" win!", True, RED)
                screen.blit(WinText,
                        [((WWidght - 100)/2) - (WinText.get_width()/2), (WHight/2) - (WinText.get_height()/2)])    
            pygame.display.flip()
            clock.tick(FPS)
        except ExitEx:
			pass