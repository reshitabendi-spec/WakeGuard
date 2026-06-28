import pygame
import time

pygame.init()
pygame.mixer.init()

print("Loading sound...")

pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.play()

print("Playing sound...")

time.sleep(5)