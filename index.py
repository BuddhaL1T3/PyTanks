import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 155)
gray = (195, 195, 195)

clock = pygame.time.Clock()

display_width = 800
display_height = 600

FPS = 20

smFont = pygame.font.SysFont('comicsansms', 25)
medFont = pygame.font.SysFont('comicsansms', 50)
lgFont = pygame.font.SysFont('comicsansms', 80)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('IDK YET :)')

# icon = pygame.image.load('appleicon.png')
# pygame.display.set_icon(icon)
# snakeHead = pygame.image.load('snakehead.png')
# apple = pygame.image.load('apple.png')

def score(score):
  text = smFont.render('Score: '+str(score), True, black)
  gameDisplay.blit(text, [0, 0])

def randAppleGen():
  randAppleX = round(random.randrange(0, display_width - block_size)/10.0)*10.0
  randAppleY = round(random.randrange(0, display_height - block_size)/10.0)*10.0

  return randAppleX,randAppleY

def text_objs(text, color, size):
  if size == 'small':
    textSurface = smFont.render(text, True, color)
  elif size == 'medium':
    textSurface = medFont.render(text, True, color)
  elif size == 'large':
    textSurface = lgFont.render(text, True, color)

  return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size='small'):
  textSurf, textRect = text_objs(msg, color, size)
  textRect.center = (display_width/2), (display_height/2) + y_displace
  gameDisplay.blit(textSurf, textRect)

def pause():
  paused = True
  message_to_screen('Paused', black, -100, 'large')
  message_to_screen('Press "Space-bar" to continue or "Esc" to quit.', black, 25, 'small')
  
  pygame.display.update()
  while paused:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          paused = False
        elif event.key == pygame.K_ESCAPE:
          pygame.quit()
          quit()

def game_intro():
  intro = True
  while intro:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          intro = False
        elif event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False

    gameDisplay.fill(gray)
    message_to_screen('Welcome to BLANK', green, -150, 'large')
    message_to_screen('The objective of the game is to shoot and destroy the enemy tank before they destroy you', black, -30, 'small')
    message_to_screen('The more enemies you destroy the harder they get\.', black, 10, 'small')
    message_to_screen('But, be careful... If you run into yourself, or the walls, you will die.', black, 50, 'small')
    message_to_screen('During game play, press "Space-bar" to pause.', black, 90, 'small')
    message_to_screen('Press "Space-bar" to continue or "Esc" to quit.', black, 180, 'small')

    pygame.display.update()
    clock.tick(5)

game_intro()

def gameLoop():
  
  gameExit = False
  gameOver = False

  while not gameExit:

    while gameOver:
      gameDisplay.fill(gray)
      message_to_screen('Game over!', red, -50, 'large')
      message_to_screen('Press "Space-bar" to continue or "Esc" to quit.', black, 50, 'small')
      score(snakeLength - 1)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          gameOver = False
          gameExit = True
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            gameExit = True
            gameOver = False
          if event.key == pygame.K_SPACE:
            gameLoop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          pass
        elif event.key == pygame.K_RIGHT:
          pass
        elif event.key == pygame.K_UP:
          pass
        elif event.key == pygame.K_DOWN:
          pass
        elif event.key == pygame.K_SPACE:
          pause()
        elif event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False
 
    
    gameDisplay.fill(gray)
    pygame.display.update()
  
    clock.tick(FPS)
  
  pygame.quit()
  quit()

gameLoop()