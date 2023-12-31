import pygame.font


class Scoreboard:
    """Класс для отображения информации о счете/рекордах"""

    def __init__(self, ai_settings, screen, stats):
        """Инициализизация атрибутов оценки"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Настройка шрифта
        self.text_color = (255, 204, 0)
        self.font = pygame.font.Font('assets\PsychicForce2012Monospaced.otf', 48)

        # Подготовка оценок
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Визуализация счета"""
        score_str = "Счет: "+str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Отображение счета в правом верхнем углу
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Вывод рекорда игрока"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Рекорд: "+"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # Ставит рекорд в центре вверху
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Превращает уровень в изображение"""
        self.level_image = self.font.render("Уровень: "+str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        # Отображение уровня под текущим счетом в правом вверхнем углу
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
