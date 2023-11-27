import pygame
import sys
import os

pygame.init()

screen_width = 1920
screen_height = 1080

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Интерактивное меню")

background_image = pygame.image.load(os.path.join('images/backgroundmenu.png'))
background_image = pygame.transform.scale(background_image, (screen_width*1.5, screen_height*1.5))

font = pygame.font.Font(None, 72)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect

new_game_button = pygame.Rect(700, 400, 500, 100)
load_game_button = pygame.Rect(700, 550, 500, 100)
exit_button = pygame.Rect(700, 700, 500, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if new_game_button.collidepoint(mouse_pos):
                print("Нажата кнопка 'Новая игра'")

            elif setting_rect.collidepoint(mouse_pos):
                print('setting menu')
               
            elif load_game_button.collidepoint(mouse_pos):
                print("Нажата кнопка 'Загрузить игру'")
                
            elif exit_button.collidepoint(mouse_pos):
                print("Нажата кнопка 'Выход'")
                pygame.quit()
                sys.exit()

    screen.blit(background_image, (0, 0))
    
    title_rect = draw_text("Игровое меню", font, white, screen, 700, 200)
    new_game_rect = draw_text("Новая игра", font, white, screen, 700, 400)
    setting_rect = draw_text("Настройки", font, white, screen, 700, 400)
    load_game_rect = draw_text("Загрузить игру", font, white, screen, 700, 550)
    exit_rect = draw_text("Выход", font, white, screen, 700, 700)
    
    pygame.display.flip()