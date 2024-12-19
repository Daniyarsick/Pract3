class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Настройки экрана
        self.screen_width = 1200  # Ширина экрана
        self.screen_height = 800  # Высота экрана
        self.bg_color = (230, 230, 230)  # Цвет фона экрана

        # Настройки корабля
        self.ship_limit = 3  # Количество жизней корабля

        # Настройки пуль
        self.bullet_width = 3  # Ширина пули
        self.bullet_height = 15  # Высота пули
        self.bullet_color = (60, 60, 60)  # Цвет пули
        self.bullets_allowed = 3  # Максимальное количество пуль на экране

        # Настройки пришельцев
        self.fleet_drop_speed = 10  # Скорость опускания флота пришельцев

        # Настройки ускорения игры
        self.speedup_scale = 1.1  # Множитель ускорения игры
        self.score_scale = 1.5  # Множитель увеличения очков за пришельцев

        # Инициализация динамических настроек
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, которые меняются в процессе игры."""
        self.ship_speed = 1.5  # Скорость корабля
        self.bullet_speed = 3.0  # Скорость пуль
        self.alien_speed = 1.0  # Скорость пришельцев

        # Направление флота: 1 означает движение вправо, -1 — влево
        self.fleet_direction = 1

        # Настройки очков
        self.alien_points = 50  # Очки за уничтожение одного пришельца

    def increase_speed(self):
        """Увеличивает скорость игры и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale  # Увеличиваем скорость корабля
        self.bullet_speed *= self.speedup_scale  # Увеличиваем скорость пуль
        self.alien_speed *= self.speedup_scale  # Увеличиваем скорость пришельцев

        # Увеличиваем количество очков за уничтожение пришельца
        self.alien_points = int(self.alien_points * self.score_scale)
