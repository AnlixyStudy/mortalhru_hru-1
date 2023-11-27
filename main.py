import pygame
import time
import os
from hero import Hero
from boss import Boss

w = 1920
h = 1080
background_image = pygame.image.load(os.path.join('images/backgroundmenu.png'))
background_image = pygame.transform.scale(background_image, (w*1.5, h*1.5))

hero_name = input("Выберите героя (hero1, hero2, hero3): ")

if hero_name == '1':
    hero_image = pygame.image.load("images/hero1.png")
elif hero_name == '2':
    hero_image = pygame.image.load("images/hero2.png")
elif hero_name == '3':
    hero_image = pygame.image.load("images/hero3.png")

hero_image = pygame.transform.scale(hero_image, (w // 2.5, h // 1.5))

def start_game():
    pygame.init()
    screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
    pygame.display.set_caption("Моя игра")

    hero = Hero(hero_image, screen)  
    hero.rect.bottom = screen.get_rect().bottom
    hero.rect.left = screen.get_rect().left
    boss = Boss(screen, w, h)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        hero.moving_hero(screen)
        boss.moving_boss(screen)
        screen.blit(background_image, (0, 0))
        hero.output_hero()
        boss.output_boss()

        pygame.display.flip()

time.sleep(1)
start_game()