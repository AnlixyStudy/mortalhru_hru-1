import pygame

# Управление игроками
class Player1:
    def __init__(self, player1, is_jumping, is_crouching, jump_count, JUMP_HEIGHT, GRAVITY, platform):
        self.keys = pygame.key.get_pressed()

        # Управление игроком 1
        if self.keys[pygame.K_ESCAPE]:
            import menu_test
        if self.keys[pygame.K_a]:
            player1.x -= 3
            player1_state = "idle"
        if self.keys[pygame.K_d]:
            player1.x += 3
            player1_state = "idle"
        if self.keys[pygame.K_s] and not is_jumping[0]:
            is_crouching[0]  = True
            player1_state = "crouch"
        # В обработчике событий/управления персонажем
        if self.keys[pygame.K_w] and not is_jumping[0]:
            is_jumping[0] = True
            jump_count[0] = JUMP_HEIGHT
            player1_state = 'jump'  # Устанавливаем начальную высоту прыжка

        if is_jumping[0]:
            if jump_count[0] >= -JUMP_HEIGHT:
                # Обновляем координаты по вертикали в зависимости от высоты прыжка
                player1.y -= (jump_count[0] ** 2) * 0.5 * GRAVITY
                jump_count[0] -= 1  # Уменьшаем высоту прыжка
            else:
                is_jumping[0] = False  # Завершаем прыжок

        # Обработка столкновений с платформой и другими объектами
        if player1.colliderect(platform):
            if is_jumping[0]:
                is_jumping[0] = False  # Останавливаем прыжок
                jump_count[0] = JUMP_HEIGHT  # Сбрасываем высоту прыжка
            player1.y = platform.top - player1.height  # Выравниваем персонажа с платформой

        if is_crouching[0]:
        # Устанавливаем новые параметры для персонажа в состоянии приседания
            player1.height = 50  # Примерно половина высоты персонажа
            # Изменяем его координаты, чтобы он оставался на платформе
            if player1.colliderect(platform):
                player1.y = platform.top - player1.height

        # Проверяем, если кнопка S больше не нажата
        if not self.keys[pygame.K_s]:
            # Сбрасываем состояние приседания
            is_crouching[0] = False
            # Возвращаем исходную высоту персонажу
            player1.height = 150
            # Также нужно обновить его координаты, чтобы он оставался на платформе, если он на ней стоит
            if player1.colliderect(platform):
                player1.y = platform.top - player1.height

class Player2:
    def __init__(self, player1, player2, enemy_speed, is_jumping, cooldowns, keys, health, is_crouching, player1_state, FPS, COOLDOWN_TIME, move_direction):
        # ИИ для игрока 2
        # Проверяем позицию красного квадрата относительно синего и изменяем направление движения
        if player1.x > player2.x:
            move_direction = 0.8
        elif player1.x < player2.x:
            move_direction = -0.8

        # Автоматическое движение синего квадрата с учётом скорости
        player2.x += enemy_speed * move_direction 

        # Добавляем приседание для синего квадрата при приближении красного
        if player1.colliderect(player2) and not is_jumping[1]:
            player2.y += 5  # Это значение можно изменить для корректного отображения

        # Обработка атак с учетом Cooldown'а
        if cooldowns[1] > 0:
            cooldowns[1] -= 1
        
        if keys[pygame.K_SPACE] and player1.colliderect(player2) and cooldowns[1] == 0:
            if is_jumping[0]:
                health[1] -= 20 
            
            elif is_crouching[0]:
                health[1] -= 15
                player1_state = "crouch_attack"

            else:
                health[1] -= 10
                player1_state = "attack"
                
            cooldowns[1] = FPS * COOLDOWN_TIME  # Установка Cooldown'а


        if health[1] <= 0:
            import menu_test