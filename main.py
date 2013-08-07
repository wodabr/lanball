#/usr/bin/env python

import os, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Player(pygame.sprite.Sprite):
    def __init__(self, color, team):
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
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
        if self.rect.left < self.area.left:
            self.rect.move_ip(1, direction[1])
        elif self.rect.right > self.area.right:
            self.rect.move_ip(-1, direction[1])
        elif self.rect.top < self.area.top:
            self.rect.move_ip(direction[0], -1)
        elif self.rect.bottom > self.area.bottom:
            self.rect.move_ip(direction[0], -1)
        else:
            self.rect.move_ip(direction[0], direction[1])
    #def update(self):
        #pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('LANBALL')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    #Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Prepare Game Objects
    clock = pygame.time.Clock()
    player = Player((255,255,255), 1)
    direction = (0, 0)
    x, y = 0, 0
    allsprites = pygame.sprite.Group(player)
    #Main Loop
    while True:
        clock.tick(60)

        #handle keys
        keystate = pygame.key.get_pressed()
        player.move(keystate)
        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    #direction = (3, 0)
                    #if x != 3:
                    x += 10
                elif event.key == K_LEFT:
                    #direction = (-3, 0)
                    if x != 3:
                        x -= 3
                elif event.key == K_UP:
                    #direction = (0, -3)
                    if y != 3:
                        y -= 3
                elif event.key == K_DOWN:
                    #direction = (0, 3)
                    if y != 3:
                        y += 3
                else:
                    print "Unrecognized key"

            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    x = 0
                elif event.key == K_UP or event.key == K_DOWN:
                    y = 0

            #elif event.type == KEYDOWN and (event.key == K_RIGHT or event.key == K_LEFT or event.key == K_UP or event.key == K_DOWN):
            #    player.move(event.key)
            # elif event.type == MOUSEBUTTONDOWN:
                # if fist.punch(chimp):
                #     punch_sound.play() #punch
                #     chimp.punched()
                # else:
                #     whiff_sound.play() #miss
            # elif event.type is MOUSEBUTTONUP:
                # fist.unpunch()

        player.move((x, y))
        allsprites.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

#Game Over

if __name__ == '__main__': main()