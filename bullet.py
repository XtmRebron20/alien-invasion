import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	#管理子弹的类
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load(r'alien_invasion\images\bullet.png')
		self.rect = self.image.get_rect()
			
		#设置子弹的初始位置
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
			
		#获取子弹的速度
		self.speed = ai_settings.bullet_speed
		
		#将子弹的y坐标存为浮点数
		self.centery = float(self.rect.centery)
		
		#子弹开火标志
		self.bullet_fire_flage = False
			
	def blitem(self):
		#绘制子弹
		#if new_ship.fire_flage = True
		self.screen.blit(self.image,self.rect)
		
	def bullet_moving(self):
		#更新子弹的位置
		'''if self.bullet_fire_flage:'''
		self.centery -= self.speed
		self.rect.centery = self.centery
