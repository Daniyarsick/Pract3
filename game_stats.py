class GameStats:
    """Класс для отслеживания статистики игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings  # Настройки игры
        self.reset_stats()  # Сбрасываем статистику

        # Игра начинается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться.
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, которая может изменяться во время игры."""
        self.ships_left = self.settings.ship_limit  # Количество оставшихся кораблей
        self.score = 0  # Текущий счет
        self.level = 1  # Текущий уровень