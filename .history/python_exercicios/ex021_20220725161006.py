import pygame
pygame.init()
pygame.mixer.music.load()
#na linha acima selecionar e adicionar arquivo mp3 para executar programa
pygame.mixer.music.play()
pygame.event.wait()