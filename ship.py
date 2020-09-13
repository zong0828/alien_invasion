# -*- coding: UTF-8 -*-

import pygame

class Ship:
    """ Aclass to manage the ship """
    # ai_game 為 AlienInvasion 的 instance
    def __init__(self, ai_game):
        """ init the ship, and set its starting position. """
        # 取得遊戲視窗大小
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        # 取得圖型大小
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        # 指定飛船位置到遊戲螢幕的正中下方
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at its current location """
        # 該 blitme 會根據 self.rect 的位置, 建立飛船到遊戲螢幕上
        self.screen.blit(self.image, self.rect)
