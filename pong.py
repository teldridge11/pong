import pygame
import time
import random

pygame.init()

displayHeight = 600
displayWidth = 800
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
FPS = 30

white = (255,255,255)
black = (0,0,0)

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

lineWidth = 5

ballSize = 10
ballX = int(displayWidth/2)
ballY = int(displayHeight/2)
ballSpeed = 10
changeBallX = -ballSpeed
changeBallY = -ballSpeed

pygame.draw.circle(gameDisplay, white, (ballX,ballY), ballSize)
pygame.draw.line(gameDisplay,white,(int(displayWidth/2),displayHeight),(int(displayWidth/2),0),lineWidth)

currentPlayerScore = 0
currentComputerScore = 0

paddleHeight = 80
paddleSpeed = 15

playerPaddleY = (displayHeight/2)-(paddleHeight/2)
playerPaddleX = 10
changePlayerPaddleY = 0

computerPaddleY = (displayHeight/2)-(paddleHeight/2)
computerPaddleX = 790

def score(playerScore,computerScore):
    playerText = medfont.render(str(playerScore), True, white)
    computerText = medfont.render(str(computerScore), True, white)
    gameDisplay.blit(playerText, [displayWidth/2-50,5])
    gameDisplay.blit(computerText, [displayWidth/2+20,5])

def playerPaddle(playerY):
    pygame.draw.line(gameDisplay,white,(playerPaddleX,playerY),(playerPaddleX,playerY+paddleHeight),lineWidth)

def computerPaddle(computerY):
    pygame.draw.line(gameDisplay,white,(computerPaddleX,computerY),(computerPaddleX,computerY+paddleHeight),lineWidth) 

def ballDraw(ballXPosition,ballYPosition):
    pygame.draw.circle(gameDisplay, white, (ballXPosition,ballYPosition), ballSize)

# Game Loop
while True:
    gameDisplay.fill(black)
    
    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changePlayerPaddleY = -paddleSpeed
            elif event.key == pygame.K_DOWN:
                changePlayerPaddleY = paddleSpeed
        elif event.type == pygame.KEYUP:
            changePlayerPaddleY = 0

    # Player paddle Boundaries 
    if playerPaddleY >= displayHeight-paddleHeight:
        playerPaddleY = displayHeight-paddleHeight
    elif playerPaddleY <= 0:
        playerPaddleY = 0
        
    # Ball Boundaries
    if ballY+ballSize >= displayHeight:
        changeBallY = -ballSpeed
    elif ballY <= 0:
        changeBallY = ballSpeed
        
    # Ball/Paddle Collision Detection
    if ballX == playerPaddleX+ballSize:
        if playerPaddleY+paddleHeight+ballSize >= ballY >= playerPaddleY-ballSize:
            changeBallX = ballSpeed
    elif ballX == computerPaddleX-ballSize:
        if computerPaddleY+paddleHeight+ballSize >= ballY >= computerPaddleY-ballSize:
            changeBallX = -ballSpeed
    elif ballX < playerPaddleX+ballSize:
        currentComputerScore += 1
        ballX = int(displayWidth/2)
        changeBallX = ballSpeed
    elif ballX > computerPaddleX-ballSize:
        currentPlayerScore += 1
        ballX = int(displayWidth/2)
        changeBallX = -ballSpeed
        
    # Make changes to player paddle's Y coordinates
    playerPaddleY += changePlayerPaddleY

    # Computer paddle control
    if changeBallY == ballSpeed:
        computerPaddleY = ballY+random.randrange(0,10)-(paddleHeight/2)+(paddleHeight/1.5)
    elif changeBallY == -ballSpeed:
        computerPaddleY = ballY-random.randrange(0,10)-(paddleHeight/2)-(paddleHeight/1.5)

    # Computer paddle boundaries
    if computerPaddleY >= displayHeight-paddleHeight:
        computerPaddleY = displayHeight-paddleHeight
    elif computerPaddleY <= 0:
        computerPaddleY = 0

    # Make changes to ball coordinates
    ballX += changeBallX
    ballY += changeBallY
    ballDraw(ballX,ballY)

    # Update score
    score(currentPlayerScore,currentComputerScore)

    # Draw paddles
    computerPaddle(computerPaddleY)
    playerPaddle(playerPaddleY)
    
    # Draw midline
    pygame.draw.line(gameDisplay,white,(int(displayWidth/2),displayHeight),(int(displayWidth/2),0),lineWidth)

    pygame.display.update()
    clock.tick(FPS)
