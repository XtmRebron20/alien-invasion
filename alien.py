import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,screen,ai_settings):
		super().__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		
		#获取png图片并矩形化
		self.alien = pygame.image.load(r'alien_invasion\images\alien.png')
		self.rect = self.alien.get_rect()
		
		self.alien_x = float(self.rect.x)
		self.alien_y = float(self.rect.y)
	
	def blit(self):
		#绘制外星人
		self.screen.blit(self.alien,self.rect)
	
	def check_alien_position(self):
		#如果已经到达屏幕右侧，改变标志为-1
		if self.rect.right >= self.screen_rect.right:
			self.ai_settings.alien_x_moving_flage = -1
			return True
		#如果已经到达屏幕左侧，改变标志为1
		elif self.rect.left <= self.screen_rect.left:
			self.ai_settings.alien_x_moving_flage = 1
			return True 
		
	def update(self):
		#外星人左右移动
		self.alien_x += (self.ai_settings.alien_x_speed*
						self.ai_settings.alien_x_moving_flage)
		self.rect.x = self.alien_x
			
