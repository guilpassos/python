import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()
# Iniciando o Pygame
pygame.init()
pygame.mixer.music.load('ex021')
pygame.mixer.music.play()
input()
pygame.event.wait()