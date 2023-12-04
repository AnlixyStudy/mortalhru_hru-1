import pygame
    
class draw:
    def __init__(self, player2, JUMP_HEIGHT, JUMP_SPEED, WIDTH, HEIGHT, PLATFORM_HEIGHT):
        # Загрузка изображений персонажей
        self.player1_images = {
            "idle": pygame.image.load("images/hero3pixel.png"),
            "attack": pygame.image.load("images/hero3pixel.png"),
            "jump": pygame.image.load("images/hero3pixel.png"),
            "crouch": pygame.image.load("images/hero3pixel.png"),
        }

        self.player2_images = {
            "idle": pygame.image.load("images/hero2pixel.png"),
            "attack": pygame.image.load("images/hero2pixel.png"),
            "jump": pygame.image.load("images/hero2pixel.png"),
            "crouch": pygame.image.load("images/hero2pixel.png"),
        }

        self.GROUND_LEVEL = HEIGHT - PLATFORM_HEIGHT - self.player2_images["idle"].get_height() 

        self.player1_state = "idle"  # начальное состояние
        self.player2_state = "idle"  # начальное состояние

        self.background_image = pygame.image.load("images/mario-background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
