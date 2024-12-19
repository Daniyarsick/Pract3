import pygame.font


class Button:
    """Класс для создания кнопки в игре."""

    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen  # Экран игры
        self.screen_rect = self.screen.get_rect()  # Прямоугольник экрана

        # Устанавливаем размеры и свойства кнопки.
        self.width, self.height = 200, 50  # Ширина и высота кнопки
        self.button_color = (0, 255, 0)  # Цвет кнопки (зеленый)
        self.text_color = (255, 255, 255)  # Цвет текста (белый)
        self.font = pygame.font.SysFont(None, 48)  # Шрифт текста

        # Создаем объект прямоугольника кнопки и центрируем его.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение на кнопке нужно подготовить только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в изображение и центрирует текст на кнопке."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отрисовывает пустую кнопку, а затем текст на ней."""
        self.screen.fill(self.button_color, self.rect)  # Заполняем цветом прямоугольник кнопки
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Рисуем текст на кнопке