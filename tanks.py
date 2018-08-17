import pygame
import time
import random

pygame.init()

# fireSound = pygame.mixer.Sound('fire.wav')
# boomSound = pygame.mixer.Sound('boom.wav')

# pygame.mixer.music.load('song.wav')
# pygame.mixer.music.play(-1)

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

groundHeight = display_height - display_height * 0.9 - tankHeight - wheelWidth

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
  pygame.draw.circle(gameDisplay, black, (x-15, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x-10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x-5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+15, y+22), wheelWidth)

  return possTurrets[pos]

def enemyTank(x, y, pos=0):
  x = int(x)
  y = int(y)

  possTurrets = [
    (x+27, y-2),
    (x+26, y-5),
    (x+25, y-8),
    (x+23, y-12),
    (x+20, y-14),
    (x+18, y-15),
    (x+15, y-17),
    (x+13, y-19),
    (x+11, y-21)
  ]

  pygame.draw.circle(gameDisplay, tankGreen, (x, y), int(tankHeight/2))
  pygame.draw.rect(gameDisplay, tankGreen, (x-tankHeight, y, tankWidth, tankHeight))
  pygame.draw.line(gameDisplay, tankGreen, (x, y), possTurrets[pos], turretWidth)
  pygame.draw.circle(gameDisplay, black, (x-15, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x-10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x-5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+5, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+10, y+22), wheelWidth)
  pygame.draw.circle(gameDisplay, black, (x+15, y+22), wheelWidth)

  return possTurrets[pos]

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

def barrier(randBarX, randBarY, barWidth):
  pygame.draw.rect(gameDisplay, black, [randBarX, display_height-randBarY, barWidth, randBarY])

def boom(x, y, size = 50):
  # pygame.mixer.Sound.play(boomSound)
  boom = True
  while boom:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    startPoint = x,y
    colors = [red, blue, green, yellow]
    mag = 1

    while mag < size:
      boomBitX = x + random.randrange(-1*mag,mag)
      boomBitY = y + random.randrange(-1*mag,mag)

      pygame.draw.circle(gameDisplay, colors[random.randrange(0,4)], (boomBitX,boomBitY), random.randrange(1,5))
      mag += 1
      pygame.display.update()
      clock.tick(100)

    boom = False

def fireShell(gunXY, turPos, power, randBarX, randBarY, barWidth, enemyTankX, enemyTankY):
  # pygame.mixer.Sound.play(fireSound)
  damage = 0
  fire = True
  startingShell = list(gunXY)

  while fire:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
    startingShell[0] -= (12-turPos)*2
    yDirection = ((((startingShell[0]-gunXY[0])*0.015/(power/50))**2) - (turPos + turPos/(12-turPos)))
    startingShell[1] += int(yDirection)

    if startingShell[1] > display_height-groundHeight:
      hitX = int(startingShell[0] * (display_height-groundHeight)/startingShell[1])
      hitY = int(display_height-groundHeight)
      if enemyTankX + 10 > hitX > enemyTankX - 10:
        damage = 25
      elif enemyTankX + 15 > hitX > enemyTankX - 15:
        damage = 18
      elif enemyTankX + 25 > hitX > enemyTankX - 25:
        damage = 10
      elif enemyTankX + 35 > hitX > enemyTankX - 35:
        damage = 5
      boom(hitX, hitY)
      fire = False

    checkX1=startingShell[0] <= randBarX + barWidth
    checkX2=startingShell[0] >= randBarX
    checkY1=startingShell[1] <= display_height
    checkY2=startingShell[1] >= display_height- randBarY 

    if checkX1 and checkX2 and checkY1 and checkY2:
      hitX = int(startingShell[0])
      hitY = int(startingShell[1])
      boom(hitX, hitY)
      fire = False

    pygame.display.update()
    clock.tick(60)
  return damage

def enemyFireShell(gunXY, turPos, power, randBarX, randBarY, barWidth, mainTankX, mainTankY):
  damage = 0
  curPower = 1
  powerFound = False

  while not powerFound:
    curPower += 1
    if curPower>100:
      powerFound=True
    fire = True
    startingShell = list(gunXY)

    while fire:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

      startingShell[0] += (12-turPos)*2
      yDirection = ((((startingShell[0]-gunXY[0])*0.015/(curPower/50))**2) - (turPos + turPos/(12-turPos)))
      startingShell[1] += int(yDirection)

      if startingShell[1] > display_height-groundHeight:
        hitX = int(startingShell[0] * (display_height-groundHeight)/startingShell[1])
        hitY = int(display_height-groundHeight)
        if mainTankX + 15 > hitX > mainTankX - 15:
          powerFound=True
        fire = False

      checkX1=startingShell[0] <= randBarX + barWidth
      checkX2=startingShell[0] >= randBarX
      checkY1=startingShell[1] <= display_height
      checkY2=startingShell[1] >= display_height- randBarY 

      if checkX1 and checkX2 and checkY1 and checkY2:
        hitX = int(startingShell[0])
        hitY = int(startingShell[1])
        fire = False


  fire = True
  startingShell = list(gunXY)

  while fire:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)
    startingShell[0] += (12-turPos)*2
    gunPower = random.randrange(int(curPower*0.9), int(curPower*1.1))
    yDirection = ((((startingShell[0]-gunXY[0])*0.015/(gunPower/50))**2) - (turPos + turPos/(12-turPos)))
    startingShell[1] += int(yDirection)

    if startingShell[1] > display_height-groundHeight:
      hitX = int(startingShell[0] * (display_height-groundHeight)/startingShell[1])
      hitY = int(display_height-groundHeight)
      if mainTankX + 10 > hitX > mainTankX - 10:
        damage = 25
      elif mainTankX + 15 > hitX > mainTankX - 15:
        damage = 18
      elif mainTankX + 25 > hitX > mainTankX - 25:
        damage = 10
      elif mainTankX + 35 > hitX > mainTankX - 35:
        damage = 5
      boom(hitX, hitY)
      fire = False

    checkX1=startingShell[0] <= randBarX + barWidth
    checkX2=startingShell[0] >= randBarX
    checkY1=startingShell[1] <= display_height
    checkY2=startingShell[1] >= display_height- randBarY 

    if checkX1 and checkX2 and checkY1 and checkY2:
      hitX = int(startingShell[0])
      hitY = int(startingShell[1])
      boom(hitX, hitY)
      fire = False

    pygame.display.update()
    clock.tick(60)
  return damage

def shotPower(level):
  text = smFont.render('Power: '+str(level)+ '%', True, black)
  gameDisplay.blit(text, [display_width/2,0])

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
    button('PLAY', 150, 400, 100, 50, green, magenta, action='play')
    button('INFO', 350, 400, 100, 50, blue, yellow, action='info')
    button('QUIT', 550, 400, 100, 50, red, cyan, action='quit')

    pygame.display.update()
    clock.tick(15)

def healthBar(playerHealth, enemyHealth):
  if playerHealth > 66:
    playerHealthColor = green
  elif playerHealth > 33:
    playerHealthColor = yellow
  else:
    playerHealthColor = red

  if enemyHealth > 66:
    enemyHealthColor = green
  elif enemyHealth > 33:
    enemyHealthColor = yellow
  else:
    enemyHealthColor = red
  
  pygame.draw.rect(gameDisplay, playerHealthColor, (680, 25, playerHealth, 25))
  pygame.draw.rect(gameDisplay, enemyHealthColor, (20, 25, enemyHealth, 25))

def game_over():
  game_over = True
  while game_over:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False

    gameDisplay.fill(gray)
    message_to_screen('GAME OVER', red, -180, 'large')
    message_to_screen('You Died', red, -90, 'medium')
    message_to_screen('Try Again', black, -30, 'small')

    button('AGAIN', 150, 400, 100, 50, green, magenta, action='play')
    button('INFO', 350, 400, 100, 50, blue, yellow, action='info')
    button('QUIT', 550, 400, 100, 50, red, cyan, action='quit')

    pygame.display.update()
    clock.tick(15)

def win():
  win = True
  while win:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False

    gameDisplay.fill(gray)
    message_to_screen('YOU WIN', green, -180, 'large')
    message_to_screen('Good Job', black, -90, 'small')
    message_to_screen('Play Again', black, -30, 'small')

    button('AGAIN', 150, 400, 100, 50, green, magenta, action='play')
    button('INFO', 350, 400, 100, 50, blue, yellow, action='info')
    button('QUIT', 550, 400, 100, 50, red, cyan, action='quit')

    pygame.display.update()
    clock.tick(15)

def gameLoop():
  
  gameExit = False
  gameOver = False

  playerHealth = 100
  enemyHealth = 100

  barWidth = 50

  mainTankX = display_width * 0.9
  mainTankY = display_height * 0.9
  tankMove = 0
  turPos = 0
  changeTurPos = 0

  enemyTankX = display_width * 0.1
  enemyTankY = display_height * 0.9

  power = 50
  powerChange = 0

  randBarX = (display_width/2) + random.randint(display_width*-0.2, display_width*0.2 - barWidth)
  randBarY = random.randrange(display_height*0.1, display_height*0.6)

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
          damage = fireShell(gun, turPos, power, randBarX, randBarY, barWidth, enemyTankX, enemyTankY)
          enemyHealth -= damage

          enemyMoves = ['fwd','rev']
          moveIndex = random.randrange(0,2)
          distance = random.randrange(0,10)

          for x in range(random.randrange(0,10)):
            if display_width*0.3 > enemyTankX > display_width*0.03:
              if enemyMoves[moveIndex] == 'fwd':
                enemyTankX += distance
              elif enemyMoves[moveIndex] == 'rev':
                enemyTankX -= distance
              gameDisplay.fill(gray)
              healthBar(playerHealth, enemyHealth)
              gun = tank(mainTankX, mainTankY, turPos)
              enemyGun = enemyTank(enemyTankX,enemyTankY, 8)
              power += powerChange
              shotPower(power)
              barrier(randBarX, randBarY, barWidth )
              gameDisplay.fill(green, rect=[0, display_height-groundHeight, display_width, groundHeight])
              pygame.display.update()
              clock.tick(FPS)

          damage = enemyFireShell(enemyGun, 8, 50, randBarX, randBarY, barWidth, mainTankX, mainTankX)
          playerHealth -= damage
          
        elif event.key == pygame.K_a: #change to mouse wheel down
          powerChange = -1
        elif event.key == pygame.K_d: #change to mouse wheel up
          powerChange = 1
        elif event.key == pygame.K_p:
          pause()
        elif event.key == pygame.K_ESCAPE:
          gameExit = True
          gameOver = False
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          tankMove = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          changeTurPos = 0
        if event.key == pygame.K_a or event.key == pygame.K_d: #change to mouse wheel down and change to mouse wheel up
          powerChange = 0
        
    mainTankX += tankMove
    turPos += changeTurPos
    if turPos > 8:
      turPos = 8
    elif turPos < 0:
      turPos = 0

    if mainTankX-tankWidth/2 < randBarX+barWidth:
      mainTankX +=5

    if mainTankX-tankWidth/2 > display_width-tankWidth:
      mainTankX -= 5

    gameDisplay.fill(gray)
    healthBar(playerHealth, enemyHealth)
    gun = tank(mainTankX, mainTankY, turPos)
    enemyGun = enemyTank(enemyTankX,enemyTankY, 8)
    power += powerChange
    shotPower(power)
    barrier(randBarX, randBarY, barWidth )
    gameDisplay.fill(green, rect=[0, display_height-groundHeight, display_width, groundHeight])
    pygame.display.update()
    if playerHealth < 1:
      game_over()
    elif enemyHealth < 1:
      win()
    clock.tick(FPS)
  
  pygame.quit()
  quit()
game_intro()
gameLoop()