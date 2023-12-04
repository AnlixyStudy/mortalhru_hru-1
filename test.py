import pygame
import hero
import Draw

pygame.init()

# Определение основных констант
WIDTH, HEIGHT = 1920, 1080
FPS = 60
COOLDOWN_TIME = 1  # Кулдаун в секундах
GRAVITY = 0.75  # Гравитация 

JUMP_HEIGHT = 10  # Высота прыжка
JUMP_SPEED = 1  # Скорость подпрыгивания

RED = (255, 0, 0)
BLUE = (0, 0, 255)
PLATFORM_HEIGHT = 30
PLAYER_HEALTH = 100

# Установка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Mortal Kombat Lite")
clock = pygame.time.Clock()

# Платформа
platform = pygame.Rect(0, HEIGHT - PLATFORM_HEIGHT, WIDTH, PLATFORM_HEIGHT)

# Установка параметров прыжка
is_jumping = [False, False]
is_crouching = [False, False]
jump_count = [JUMP_HEIGHT, JUMP_HEIGHT]

# Характеристики здоровья игроков
health = [PLAYER_HEALTH, PLAYER_HEALTH]

# Cooldown для ударов
cooldowns = [0, 0, 0]

# ИИ для игрока 2 (синий куб)
enemy_cooldown = 0
move_direction = 1  # 1 - вправо, -1 - влево
enemy_speed = 2  # Значение скорости

# # Игровые объекты и переменные для прыжка
player1 = pygame.Rect(50, HEIGHT - 150, 150, 150)
player2 = pygame.Rect(200, HEIGHT - 150, 150, 150)
players = [player1, player2]
is_jumping = [False, False]
jump_count = [JUMP_HEIGHT, JUMP_HEIGHT]
jump_cooldown = [0, 0]
jump_speed = [0, 0]

draw = Draw.draw(player2, JUMP_HEIGHT, JUMP_SPEED, WIDTH, HEIGHT, PLATFORM_HEIGHT)

def draw_players():
    global player2_state
    global player1_image
    global player2_image

    # Handle keyboard events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                draw.player1_state = "jump"
            elif event.key == pygame.K_LCTRL:
                draw.player1_state = "crouch"
            elif event.key == pygame.K_RETURN:
                draw.player1_state = "attack"

    if draw.player1_state == "jump":
        player1_image = draw.player1_images["jump"]

    elif draw.player1_state == "crouch":
        player1_image = draw.player1_images["crouch"]
        
    elif draw.player1_state == "attack":
        player1_image = draw.player1_images["attack"]
        
    else:
        player1_image = draw.player1_images["idle"]
        
    if draw.player2_state == "jump":
        player2_image = draw.player2_images["jump"]
    
        if player2.y > draw.GROUND_LEVEL - JUMP_HEIGHT:
            player2.y -= JUMP_SPEED
        else:
            player2_state = "idle"  

        
        if player2.y >= draw.GROUND_LEVEL:
            player2.y = draw.GROUND_LEVEL
            player2_state = "idle"  

    elif draw.player2_state == "crouch":
        player2_image = draw.player2_images["crouch"]
    
    elif draw.player2_state == "attack":
        player2_image = draw.player2_images["attack"]
        
    else:
        player2_image = draw.player2_images["idle"]

    scaled_player1_image = pygame.transform.scale(player1_image, (player1.width, player1.height))
    screen.blit(scaled_player1_image, player1)

    scaled_player2_image = pygame.transform.scale(player2_image, (player2.width, player2.height))
    screen.blit(scaled_player2_image, player2)

# Основной игровой цикл
running = True
while running:
    # Отслеживание действий пользователя и событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Hero1 = hero.Player1(player1, is_jumping, is_crouching, jump_count, JUMP_HEIGHT, GRAVITY, platform)
    keys = Hero1.keys

    Hero2 = hero.Player2(player1, player2, enemy_speed, is_jumping, cooldowns, keys, health, is_crouching, draw.player1_state, FPS, COOLDOWN_TIME, move_direction)

    # Отрисовка
    screen.blit(draw.background_image, (0, 0))
    draw_players()
    pygame.draw.rect(screen, (0, 0, 0), platform)

    # Отображение здоровья
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player 1 Health: {health[0]}", True, RED) 
    screen.blit(text, (10, 10))
    text = font.render(f"Player 2 Health: {health[1]}", True, BLUE)
    screen.blit(text, (WIDTH - text.get_width() - 10, 10))
   
    pygame.display.flip()

    # Ограничения перемещения игроков в пределах экрана
    for player in players:
        player.x = max(0, min(player.x, WIDTH - player.width))
        player.y = max(HEIGHT - player.height, min(player.y, HEIGHT - player.height))

    # Ограничение для платформы
    if player1.colliderect(platform):
        if is_jumping[0]:
            is_jumping[0] = False
            jump_count[0] = JUMP_HEIGHT
        player1.y = platform.top - player1.height

    if player2.colliderect(platform):
        if is_jumping[1]:
            is_jumping[1] = False
            jump_count[1] = JUMP_HEIGHT
        player2.y = platform.top - player2.height

    if enemy_cooldown > 0:
        enemy_cooldown -= 1

    clock.tick(FPS)

pygame.quit()