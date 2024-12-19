import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем."""

    def __init__(self, game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = game.screen  # Экран игры
        self.settings = game.settings  # Настройки игры
        self.screen_rect = game.screen.get_rect()  # Прямоугольник экрана

        # Загружаем изображение корабля и получаем его прямоугольник.
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Устанавливаем корабль в нижней центральной части экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохраняем десятичное значение для горизонтальной позиции корабля.
        self.x = float(self.rect.x)

        # Флаги движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля на основе флагов движения."""
        # Обновляем значение x корабля, а не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновляем объект rect на основе значения self.x.
        self.rect.x = self.x

    def draw(self):
        """Отрисовывает корабль на экране."""
        self.screen.blit(self.image, self.rect)

    def align_center(self):
        """Центрирует корабль на экране."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
