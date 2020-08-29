#!/bin/python3
import math
import pygame
import random
#Inititalize the pygame..
pygame.init()


#Create a screen
screen = pygame.display.set_mode((800,600))
running = True

#Adding a title and a logo for the game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

#Adding a background
background = pygame.image.load("background.jpg")

#Adding a player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerXChange = 0

#Adding an enemy

enemyImg = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
noOfEnemies = 6

for i in range(noOfEnemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(60,100))
    enemyXChange.append(3)
    enemyYChange.append(40)



#Adding Bullet Fire
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#Score Value
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
scoreX = 10
scoreY = 10

#GameOver value
over_font = pygame.font.Font("freesansbold.ttf",70)

#Functions
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True,(100,100,200))
    screen.blit(score,(x,y))


def player(x,y):
    screen.blit(playerImg,(x, y))


def enemy(x,y,i):
    screen.blit(enemyImg[i],(x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def game_over():
    over_text = over_font.render("GAME OVER", True,(255,255,200))
    screen.blit(over_text,(200,250))
#GameLoop
while running:
    screen.fill((100,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXChange += 5
                #print("Right Key is pressed")
            if event.key == pygame.K_LEFT:
                playerXChange -= 5
                #print("Left Key is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    #print("Space Key was pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                #print("Key Released")
                playerXChange = 0
    
    playerX += playerXChange

    if playerX <= 0:
        playerX = 0
        
    elif playerX >= 736:
        playerX = 736
        
   

    # Enemy Movement
    for i in range(noOfEnemies):

        #Game Over
        if enemyY[i] > 430:
            for j in range(noOfEnemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 3
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -3
            enemyY[i] += enemyYChange[i]
        
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            score_value +=1
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(60,100)
        enemy(enemyX[i],enemyY[i],i)


    #Bullet Movement 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    if collision:
        score_value +=1
        bulletY = 480
        bullet_state = "ready"
        enemyX[i] = random.randint(0,735)
        enemyY[i] = random.randint(60,100)


    player(playerX, playerY)
    show_score(scoreX,scoreY)
 
    pygame.display.update()
