# /usr/bin/env python
# -*- coding: utf-8 -*-

import os, pygame
from pygame.locals import *
from ubuntutweak.gui.widgets import Switch

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Player(pygame.sprite.Sprite):
  MAX_SPEED = 3
  
  def __init__(self, color, team):
    pygame.sprite.Sprite.__init__(self)
    # Create an image of the block, and fill it withmove_ip a color.
    # This could also be an image loaded from the disk.
    self.image = pygame.Surface([50, 50])
    self.image.fill(color)
    pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)

    # Fetch the rectangle object that has the dimensions of the image
    # Update the position of this object by setting the values of rect.x and rect.y
    self.rect = self.image.get_rect()

    # get area
    screen = pygame.display.get_surface()
    self.area = screen.get_rect()
    
  def move(self, direction):
    x, y = 0, 0
    if direction['x'] == K_LEFT:
      x = -self.MAX_SPEED
    elif direction['x'] == K_RIGHT:
      x = self.MAX_SPEED
    if direction['y'] == K_UP:
      y = -self.MAX_SPEED
    elif direction['y'] == K_DOWN:
      y = self.MAX_SPEED
    self._move(x, y)

  
  def _move(self, x, y):
    """Przesuwa o zadaną liczbę pixeli, nie pozwala wyjść poza boisko
    """
    print self.rect.left, self.area.left
    if self.rect.left + x < self.area.left:
      x = self.area.left - self.rect.left
    elif self.rect.right + x > self.area.right:
      x = self.area.right - self.rect.right
    if self.rect.top + y < self.area.top:
      y = self.area.top - self.rect.top
    elif self.rect.bottom + y > self.area.bottom:
      y = self.area.bottom - self.rect.bottom
    self.rect.move_ip(x, y)


def main():
  pygame.init()
  screen = pygame.display.set_mode((640, 480))
  pygame.display.set_caption('LANBALL')

  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((250, 250, 250))

  # Display The Background
  screen.blit(background, (0, 0))
  pygame.display.flip()

  # Prepare Game Objects
  clock = pygame.time.Clock()
  player = Player((255, 255, 255), 1)
  direction = {'x': 0, 'y': 0}
  allsprites = pygame.sprite.Group(player)
  # Main Loop
  while True:
    clock.tick(60)

    # handle keys
    keystate = pygame.key.get_pressed()
    player.move(direction)
    # Handle Input Events
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return

      if event.type == KEYDOWN:
        if event.key == K_RIGHT or event.key == K_LEFT:
          direction['x'] = event.key
        elif event.key == K_UP or event.key == K_DOWN:
          direction['y'] = event.key
          
      if event.type == KEYUP:
        if event.key == direction['x']:
          direction['x'] = 0
        if event.key == direction['y']:
          direction['y'] = 0

      # elif event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or event.key == K_DOWN):
      #  player.move(event.key)
      # elif event.type == MOUSEBUTTONDOWN:
        # if fist.punch(chimp):
        #   punch_sound.play() #punch
        #   chimp.punched()
        # else:
        #   whiff_sound.play() #miss
      # elif event.type is MOUSEBUTTONUP:
        # fist.unpunch()
    player.move(direction)
    allsprites.update()

  	# Draw Everything
    screen.blit(background, (0, 0))
    allsprites.draw(screen)
    pygame.display.flip()

# Game Over

if __name__ == '__main__': main()
