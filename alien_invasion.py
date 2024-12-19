import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from utils import hide_mouse_cursor


class AlienInvasion:
    """Основной класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()  # Загружаем настройки игры
        self.clock = pygame.time.Clock()  # Создаем объект для управления FPS
        self.fps = 60  # Устанавливаем FPS

        # Инициализация звуков
        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound('assets/sound/laser.wav')
        self.alien_hit_sound = pygame.mixer.Sound('assets/sound/explosion.wav')
        self.ship_hit_sound = pygame.mixer.Sound('assets/sound/ship_hit.wav')
        self.game_over_sound = pygame.mixer.Sound('assets/sound/game_over.wav')

        # Создаем окно игры
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

        # Инициализируем статистику игры, табло, корабль, пули и пришельцев
        self.stats = GameStats(self)
        self.score_board = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet_of_aliens()  # Создаем флот пришельцев
        self.play_button = Button(self, 'Play')  # Создаем кнопку "Play"

    def run_game(self):
        """Основной цикл игры."""
        while True:
            self.respond_to_events()  # Обрабатываем события

            if self.stats.game_active:  # Если игра активна
                self.ship.update()  # Обновляем позицию корабля
                self.update_bullet_positions()  # Обновляем позиции пуль
                self._update_aliens()  # Обновляем позиции пришельцев

            self._update_screen()  # Обновляем экран
            self.clock.tick(self.fps)  # Устанавливаем FPS

    def respond_to_events(self):
        """Обрабатывает события, такие как нажатия клавиш и кнопок мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если нажата кнопка закрытия окна
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Если клавиша нажата
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Если клавиша отпущена
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
                mouse_pos = pygame.mouse.get_pos()
                self.start_game_if_player_clicks_play(mouse_pos)

    def start_game_if_player_clicks_play(self, mouse_pos):
        """Запускает игру, если игрок нажал на кнопку Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.reset_game_statistics()  # Сбрасываем статистику игры
            self.remove_aliens_and_bullets()  # Удаляем всех пришельцев и пули
            self.create_new_fleet()  # Создаем новый флот
            hide_mouse_cursor()  # Скрываем курсор мыши

    def reset_game_settings(self):
        """Сбрасывает настройки игры."""
        self.settings.initialize_dynamic_settings()
        self.reset_game_statistics()

    def remove_aliens_and_bullets(self):
        """Удаляет всех пришельцев и пули."""
        self.aliens.empty()
        self.bullets.empty()

    def create_new_fleet(self):
        """Создает новый флот пришельцев и центрирует корабль."""
        self.create_fleet_of_aliens()
        self.ship.align_center()

    def reset_game_statistics(self):
        """Сбрасывает статистику игры."""
        self.stats.reset_stats()
        self.stats.game_active = True
        self.score_board.prep_score()
        self.score_board.prep_level()
        self.score_board.prep_ships()

    def check_keydown_events(self, event):
        """Обрабатывает нажатия клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self, event):
        """Обрабатывает отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        """Создает новую пулю и добавляет ее в группу пуль."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_sound.play()  # Воспроизводим звук выстрела

    def update_bullet_positions(self):
        """Обновляет позиции пуль и удаляет старые пули."""
        self.bullets.update()
        self.remove_bullets_that_have_disappeared()
        self.manage_bullet_alien_collision()

    def remove_bullets_that_have_disappeared(self):
        """Удаляет пули, которые вышли за пределы экрана."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def manage_bullet_alien_collision(self):
        """Обрабатывает столкновения пуль с пришельцами."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.score_board.prep_score()
            self.score_board.check_high_score()
            self.alien_hit_sound.play()  # Воспроизводим звук попадания

        if not self.aliens:
            self.increase_level()

    def increase_level(self):
        """Увеличивает уровень игры."""
        self.bullets.empty()
        self.create_fleet_of_aliens()
        self.settings.increase_speed()

        self.stats.level += 1
        self.score_board.prep_level()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Проверяет, достигли ли пришельцы нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.score_board.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self.create_fleet_of_aliens()
            self.ship.align_center()

            self.ship_hit_sound.play()  # Воспроизводим звук столкновения

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def create_fleet_of_aliens(self):
        """Создает флот пришельцев."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.place_alien_in_row(alien_number, row_number)

    def place_alien_in_row(self, alien_number, row_number):
        """Размещает пришельца в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Проверяет, достиг ли флот края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Меняет направление флота и опускает его вниз."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.score_board.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()