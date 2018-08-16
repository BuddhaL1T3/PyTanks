import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (195, 195, 195)
red = (255, 0, 0)
cyan = (0, 255, 255)
green = (0, 155, 0)
magenta = (255, 0, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)

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

def text_to_btn(msg, color, btnX, btnY, btnWidth, btnHeight, size='small'):
  textSurf, textRect = text_objs(msg, color, size)
  textRect.center = btnX + btnWidth/2, btnY + btnHeight/2
  gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg, color, y_displace=0, size='small'):
  textSurf, textRect = text_objs(msg, color, size)
  textRect.center = (display_width/2), (display_height/2) + y_displace
  gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactColor, actColor, inactTXTColor=black, actTXTColor=white):
  cur = pygame.mouse.get_pos()
  if x + width > cur[0] > x and y + height > cur[1] > y:
      pygame.draw.rect(gameDisplay, actColor, (x ,y ,width, height))
      text_to_btn(text, inactTXTColor, x, y, width, height)
  else:
    pygame.draw.rect(gameDisplay, inactColor, (x ,y ,width, height))
    text_to_btn(text, actTXTColor, x, y, width, height)

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
    message_to_screen('BATTLE TANKS', blue, -180, 'large')
    message_to_screen('The objective of the game is to shoot', black, -90, 'small')
    message_to_screen('and destroy the enemy tank before they destroy you', black, -50, 'small')
    message_to_screen('The more enemies you destroy the harder they get.', black, -10, 'small')
    # message_to_screen('But, be careful... If you run into yourself, or the walls, you will die.', black, 50, 'small')
    message_to_screen('During game play, press "Space-bar" to pause.', black, 30, 'small')
    message_to_screen('Press "Space-bar" to continue or "Esc" to quit.', black, 70, 'small')
    # message_to_screen('red.', red, -150, 'small')
    # message_to_screen('cyan.', cyan, -110, 'small')
    # message_to_screen('green.', green, -70, 'small')
    # message_to_screen('magenta.', magenta, -30, 'small')
    # message_to_screen('blue.', blue, 10, 'small')
    # message_to_screen('yellow.', yellow, 50, 'small')


    # cur = pygame.mouse.get_pos()
    # if 150 + 100 > cur[0] > 150 and 500+50 > cur[1] > 500:
    #   pygame.draw.rect(gameDisplay, magenta, (150, 500, 100, 50))
    # else:
    #   pygame.draw.rect(gameDisplay, green, (150, 500, 100, 50))

    # pygame.draw.rect(gameDisplay, green, (350, 500, 100, 50))
    # pygame.draw.rect(gameDisplay, green, (550, 500, 100, 50))

    # text_to_btn('PLAY', black, 150, 500, 100, 50)
    # text_to_btn('CTRLs', black, 350, 500, 100, 50)
    # text_to_btn('QUIT', black, 550, 500, 100, 50)

    button('PLAY', 150, 500, 100, 50, green, magenta)
    button('INFO', 350, 500, 100, 50, blue, yellow)
    button('QUIT', 550, 500, 100, 50, red, cyan)

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