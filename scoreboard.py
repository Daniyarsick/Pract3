import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Класс для отображения информации о счете."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты для подсчета очков."""
        self.ai_game = ai_game
        self.screen = ai_game.screen  # Экран игры
        self.screen_rect = self.screen.get_rect()  # Прямоугольник экрана
        self.settings = ai_game.settings  # Настройки игры
        self.stats = ai_game.stats  # Статистика игры

        # Настройки шрифта для отображения информации о счете.
        self.text_color = (30, 30, 30)  # Цвет текста
        self.font = pygame.font.SysFont(None, 48)  # Шрифт

        # Подготовка изображений для отображения счета.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Преобразует текущий счет в изображение."""
        rounded_score = round(self.stats.score, -1)  # Округляем счет до десятков
        score_str = "{:,}".format(rounded_score)  # Форматируем счет с разделителем тысяч
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Отображаем счет в правом верхнем углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # Отступ справа
        self.score_rect.top = 20  # Отступ сверху

    def prep_high_score(self):
        """Преобразует рекордный счет в изображение."""
        high_score = round(self.stats.high_score, -1)  # Округляем рекордный счет
        high_score_str = "{:,}".format(high_score)  # Форматируем рекордный счет
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Центрируем рекордный счет в верхней части экрана.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx  # Центрируем по горизонтали
        self.high_score_rect.top = self.score_rect.top  # Располагаем на одной высоте со счетом

    def prep_level(self):
        """Преобразует уровень в изображение."""
        level_str = str(self.stats.level)  # Текущий уровень в виде строки
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Располагаем уровень под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # Выравниваем по правому краю
        self.level_rect.top = self.score_rect.bottom + 10  # Отступ снизу

    def prep_ships(self):
        """Отображает количество оставшихся кораблей."""
        self.ships = Group()  # Группа для отображения кораблей
        for ship_number in range(self.stats.ships_left):  # Для каждого оставшегося корабля
            ship = Ship(self.ai_game)  # Создаем объект корабля
            ship.rect.x = 10 + ship_number * ship.rect.width  # Располагаем корабли в ряд
            ship.rect.y = 10  # Отступ сверху
            self.ships.add(ship)  # Добавляем корабль в группу

    def check_high_score(self):
        """Проверяет, установлен ли новый рекорд."""
        if self.stats.score > self.stats.high_score:  # Если текущий счет больше рекорда
            self.stats.high_score = self.stats.score  # Обновляем рекорд
            self.prep_high_score()  # Подготавливаем изображение для нового рекорда

    def show_score(self):
        """Отображает счет, уровень и оставшиеся корабли на экране."""
        self.screen.blit(self.score_image, self.score_rect)  # Рисуем текущий счет
        self.screen.blit(self.high_score_image, self.high_score_rect)  # Рисуем рекордный счет
        self.screen.blit(self.level_image, self.level_rect)  # Рисуем уровень
        self.ships.draw(self.screen)  # Рисуем оставшиеся корабли