import pygame
pygame.init()
pygame.mixer.music.load('021')
#na linha acima selecionar e adicionar arquivo mp3 para executar programa
pygame.mixer.music.play()
pygame.event.wait()