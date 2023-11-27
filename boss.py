import pygame

class Boss():
    def __init__(self, screen, w , h):
        self.image = pygame.transform.scale(pygame.image.load("images/boss.png"), (w // 2.5, h // 1.5))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.right = self.screen_rect.right  # Изменили строку
        self.move_right = False
        self.move_left = False

    def output_boss(self):
        self.screen.blit(self.image, self.rect)

    def moving_boss(self, screen):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 4
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 4
    
    def create_boss_again(self):
        self.center = self.screen_rect.centerx