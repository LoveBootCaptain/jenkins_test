#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time

import pygame

pygame.init()

pygame.mouse.set_visible(False)

PATH = sys.path[1] + '/src'

file = __file__

print('file: {}'.format(file))

print(PATH)

FOLDER_PATH = '/FOLDER_1/'

IMAGE_PATH = PATH + FOLDER_PATH + 'jenkins.png'

print(IMAGE_PATH)

image = pygame.image.load(IMAGE_PATH)

font = pygame.font.SysFont('arial', 18)

color = (255, 255, 255)

TFT = pygame.display.set_mode((256, 256))

background = pygame.draw.rect(TFT, RED, )


def draw_to_tft():
    TFT.blit(image, (0, 0))
    TFT.blit(font.render('jenkins', True, color), (200, 240))

    pygame.display.update()

    time.sleep(1)


def quit_all():

    pygame.quit()
    quit()


def loop():

    running = True

    while running:

        draw_to_tft()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

                quit_all()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    running = False

                    quit_all()

                elif event.key == pygame.K_SPACE:

                    print('SPACE')

    quit_all()

if __name__ == '__main__':

    try:

        loop()

    except KeyboardInterrupt:

        quit_all()
