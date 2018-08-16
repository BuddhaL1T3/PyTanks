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
tankGreen = (80, 112, 85)

clock = pygame.time.Clock()

display_width = 800
display_height = 600


tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5

FPS = 20

smFont = pygame.font.SysFont('comicsansms', 25)
medFont = pygame.font.SysFont('comicsansms', 50)
lgFont = pygame.font.SysFont('comicsansms', 80)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('BATTLE TANKS')

# icon = pygame.image.load('appleicon.png')
# pygame.display.set_icon(icon)
# snakeHead = pygame.image.load('snakehead.png')
# apple = pygame.image.load('apple.png')

def score(score):
  text = smFont.render('Score: '+str(score), True, black)
  gameDisplay.blit(text, [0, 0])

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

def tank(x, y, pos=0):
  x = int(x)
  y = int(y)

  possTurrets = [
    (x-27, y-2),
    (x-26, y-5),
    (x-25, y-8),
    (x-23, y-12),
    (x-20, y-14),
    (x-18, y-15),
    (x-15, y-17),
    (x-13, y-19),
    (x-11, y-21)
  ]


  pygame.draw.circle(gameDisplay, tankGreen, (x, y), int(tankHeight/2))
  pygame.draw.rect(gameDisplay, tankGreen, (x-tankHeight, y, tankWidth, tankHeight))
  pygame.draw.line(gameDisplay, tankGreen, (x, y), possTurrets[pos], turretWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x-15, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x-10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x-5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x+5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x+10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, tankGreen, (x+15, y+22), wheelWidth)


  # startX = 20
  # for x in range(8):
  #   pygame.draw.circle(gameDisplay, tankGreen, (x-startX, y+20), wheelWidth)
  #   startX -= 5

def gameInfo():
  info = True
  while info:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    gameDisplay.fill(gray)
    # message_to_screen('BATTLE TANKS', blue, -180, 'large')
    message_to_screen('Objective', blue, -250, 'medium')
    message_to_screen('The objective of the game is to shoot', black, -190, 'small')
    message_to_screen('and destroy the enemy tank before they destroy you.', black, -150, 'small')
    message_to_screen('The more enemies you destroy the harder they get.', black, -110, 'small')

    message_to_screen('Controls', blue, -60, 'medium')
    message_to_screen('FIRE: SPACE-BAR', black, 0, 'small')
    message_to_screen('Move Turret: UP and DOWN arrows', black, 40, 'small')
    message_to_screen('Move Tank: LEFT and RIGHT arrows', black, 80, 'small')
    message_to_screen('Pause: P', black, 120, 'small')


    button('PLAY', 150, 500, 100, 50, green, magenta, action='play')
    button('BACK', 350, 500, 100, 50, blue, yellow, action='back')
    button('QUIT', 550, 500, 100, 50, red, cyan, action='quit')

    pygame.display.update()
    clock.tick(15)



def button(text, x, y, width, height, inactColor, actColor, inactTXTColor=black, actTXTColor=white, action=None):
  cur = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if x + width > cur[0] > x and y + height > cur[1] > y:
      pygame.draw.rect(gameDisplay, actColor, (x ,y ,width, height))
      text_to_btn(text, inactTXTColor, x, y, width, height)
      if click[0] == 1 and action != None:
        if action == 'quit':
          pygame.quit()
          quit()
        if action =='info':
          gameInfo()
        if action == 'play':
          gameLoop()
        if action == 'back':
          game_intro()

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

def barrier():
  randX = (display_width/2) + random.randint(display_width*-0.2, display_width*0.2)
  randY = random.randrange(display_height*0.1, display_height*0.6)

  pygame.draw.rect(gameDisplay, black, [randX, display_height-randY, 50, randY])

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
    # message_to_screen('The objective of the game is to shoot', black, -90, 'small')
    # message_to_screen('and destroy the enemy tank before they destroy you', black, -50, 'small')
    # message_to_screen('The more enemies you destroy the harder they get.', black, -10, 'small')
    # message_to_screen('But, be careful... If you run into yourself, or the walls, you will die.', black, 50, 'small')
    
    # message_to_screen('Press "Space-bar" to continue or "Esc" to quit.', black, 70, 'small')

    button('PLAY', 150, 300, 100, 50, green, magenta, action='play')
    button('INFO', 350, 300, 100, 50, blue, yellow, action='info')
    button('QUIT', 550, 300, 100, 50, red, cyan, action='quit')

    pygame.display.update()
    clock.tick(15)

def gameLoop():
  
  gameExit = False
  gameOver = False

  mainTankX = display_width * 0.9
  mainTankY = display_height * 0.9
  tankMove = 0
  currTurPos = 0
  changeTurPos = 0

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
          tankMove = -5
        elif event.key == pygame.K_RIGHT:
          tankMove = 5
        elif event.key == pygame.K_UP:
          changeTurPos = 1
        elif event.key == pygame.K_DOWN:
          changeTurPos = -1
        elif event.key == pygame.K_SPACE:
          pause()
        elif event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          tankMove = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          changeTurPos = 0
 
    
    gameDisplay.fill(gray)
    mainTankX += tankMove
    currTurPos += changeTurPos
    if currTurPos > 8:
      currTurPos = 8
    elif currTurPos < 0:
      currTurPos = 0
    tank(mainTankX, mainTankY, currTurPos)
    barrier()

    pygame.display.update()
  
    clock.tick(FPS)
  
  pygame.quit()
  quit()
game_intro()
gameLoop()