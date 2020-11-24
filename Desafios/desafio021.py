# Este programa abre e reproduz um arquivo de audio mp3
import pygame
pygame.init()
pygame.mixer.music.load('Kalimba.mp3')
pygame.mixer.music.play()
pygame.event.wait()
