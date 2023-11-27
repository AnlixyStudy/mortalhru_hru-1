import pygame

pygame.init()

# Определение основных констант
WIDTH, HEIGHT = 800, 600
FPS = 60
COOLDOWN_TIME = 1  # Кулдаун в секундах
GRAVITY = 0.75  # Гравитация 

JUMP_HEIGHT = 10  # Высота прыжка
JUMP_COOLDOWN = 50  # Кулдаун для прыжков в кадрах
JUMP_SPEED = 1  # Скорость подпрыгивания

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PLATFORM_HEIGHT = 30
PLAYER_HEALTH = 100

# Установка окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mortal Kombat Lite")
clock = pygame.time.Clock()

# Загрузка изображений персонажей
player1_images = {
    "idle": pygame.image.load("images/hero3.png"),
    "attack": pygame.image.load("images/hero3.png"),
    "jump": pygame.image.load("images/hero3.png"),
    "crouch": pygame.image.load("images/hero3.png"),
}

player2_images = {
    "idle": pygame.image.load("images/hero2.png"),
    "attack": pygame.image.load("images/hero2.png"),
    "jump": pygame.image.load("images/hero2.png"),
    "crouch": pygame.image.load("images/hero2.png"),
}
background_image = pygame.image.load("images/mario-background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


GROUND_LEVEL = HEIGHT - PLATFORM_HEIGHT - player2_images["idle"].get_height() 
def draw_players():
    global player1_state
    global player2_state

    # Handle keyboard events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1_state = "jump"
            elif event.key == pygame.K_LCTRL:
                player1_state = "crouch"
            elif event.key == pygame.K_RETURN:
                player1_state = "attack"


    if player1_state == "jump":
        player1_image = player1_images["jump"]

    elif player1_state == "crouch":
        player1_image = player1_images["crouch"]
        
    elif player1_state == "attack":
        player1_image = player1_images["attack"]
        
    else:
        player1_image = player1_images["idle"]
        

    if player2_state == "jump":
        player2_image = player2_images["jump"]
       
        if player2.y > GROUND_LEVEL - JUMP_HEIGHT:
            player2.y -= JUMP_SPEED
        else:
            player2_state = "idle"  

        
        if player2.y >= GROUND_LEVEL:
            player2.y = GROUND_LEVEL
            player2_state = "idle"  

    elif player2_state == "crouch":
        player2_image = player2_images["crouch"]
       
    elif player2_state == "attack":
        player2_image = player2_images["attack"]
        
    else:
        player2_image = player2_images["idle"]
       


    scaled_player1_image = pygame.transform.scale(player1_image, (player1.width, player1.height))
    screen.blit(scaled_player1_image, player1)

    scaled_player2_image = pygame.transform.scale(player2_image, (player2.width, player2.height))
    screen.blit(scaled_player2_image, player2)


# Платформа
platform = pygame.Rect(0, HEIGHT - PLATFORM_HEIGHT, WIDTH, PLATFORM_HEIGHT)

# Установка параметров прыжка
is_jumping = [False, False]
jump_count = [JUMP_HEIGHT, JUMP_HEIGHT]

# Характеристики здоровья игроков
health = [PLAYER_HEALTH, PLAYER_HEALTH]

# Cooldown для ударов
cooldowns = [0, 0]

# ИИ для игрока 2 (синий куб)
enemy_cooldown = 0
move_direction = 1  # 1 - вправо, -1 - влево
enemy_speed = 2  # Значение скорости

player1_state = "idle"  # начальное состояние
player2_state = "idle"  # начальное состояние

# # Игровые объекты и переменные для прыжка
player1 = pygame.Rect(50, HEIGHT - 100, 50, 50)
player2 = pygame.Rect(200, HEIGHT - 100, 50, 50)
players = [player1, player2]
is_jumping = [False, False]
jump_count = [JUMP_HEIGHT, JUMP_HEIGHT]
jump_cooldown = [0, 0]
jump_speed = [0, 0]

# Основной игровой цикл
running = True
while running:
    # Отслеживание действий пользователя и событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроками
    keys = pygame.key.get_pressed()

    # Управление игроком 1
    if keys[pygame.K_a]:
        player1.x -= 3
        player1_state = "idle"
    if keys[pygame.K_d]:
        player1.x += 3
        player1_state = "idle"
    if keys[pygame.K_s] and not is_jumping[0]:
        player1.y += 5 
        player1_state = "crouch"
    if keys[pygame.K_w] and not is_jumping[0] and jump_cooldown[0] == 0:
        is_jumping[0] = True
        jump_speed[0] = JUMP_SPEED
        jump_cooldown[0] = JUMP_COOLDOWN
        player1_state = "jump"

    if is_jumping[0]:
        if jump_count[0] >= -JUMP_HEIGHT:
           player1.y -= (jump_count[0] ** 2) * 0.5 * GRAVITY
           jump_count[0] -= 1
        else:
            is_jumping[0] = False
            jump_count[0] = JUMP_HEIGHT

    for i in range(2):
        if is_jumping[i]:
             if jump_speed[i] >= -JUMP_SPEED:
                 players[i].y -= jump_speed[i]
                 jump_speed[i] -= 1
        else:
               is_jumping[i] = False
               jump_speed[i] = 0  # Сброс скорости

        if players[i].colliderect(platform):
            jump_cooldown[i] = JUMP_COOLDOWN  # Установка кулдауна



    # ИИ для игрока 2
    # Проверяем позицию красного квадрата относительно синего и изменяем направление движения
    if player1.x > player2.x:
        move_direction = 1
    elif player1.x < player2.x:
        move_direction = -1

    # Автоматическое движение синего квадрата с учётом скорости
    player2.x += enemy_speed * move_direction

    # # Добавляем прыжок для синего квадрата при приближении красного
    if player1.colliderect(player2) and not is_jumping[1]:
        is_jumping[1] = True
        jump_count[1] = JUMP_HEIGHT
        player2_state = "jump"

    if is_jumping[1]:
        if jump_count[1] >= -JUMP_HEIGHT:
             player2.y -= (jump_count[1] ** 2) * 0.5 * GRAVITY
             jump_count[1] -= 1
        else:
             is_jumping[1] = False
             jump_count[1] = JUMP_HEIGHT

    # Добавляем приседание для синего квадрата при приближении красного
    if player1.colliderect(player2) and not is_jumping[1]:
        player2.y += 5  # Это значение можно изменить для корректного отображения

    # Обработка атак с учетом Cooldown'а
    if cooldowns[0] > 0:
        cooldowns[0] -= 1
    if keys[pygame.K_SPACE] and player1.colliderect(player2) and cooldowns[1] == 0:  # Удар в присяги
        health[1] -= 10
        player1_state = "attack"
        cooldowns[1] = FPS * COOLDOWN_TIME  # Установка Cooldown'а
    if is_jumping[0] and player1.colliderect(player2) and cooldowns[2] == 0:  # Удар в прыжке
        health[1] -= 20
        cooldowns[2] = FPS * COOLDOWN_TIME  # Установка Cooldown'а

    # Отрисовка
    screen.blit(background_image, (0, 0))
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

