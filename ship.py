import pygame
class Ship():
	def __init__(self,screen,ai_settings):
		#初始化飞船并设置其初始位置
		#获取屏幕的属性
		self.screen = screen
		#加载飞船图像并获取其外界矩形
		self.image = pygame.image.load(r'alien_invasion\images\ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#飞船的移动标志
		self.moving_right_flage = False
		self.moving_left_flage = False
		self.moving_up_flage = False
		self.moving_down_flage = False
		#飞船的开火标志
		self.fire_flage = False
		
		#ai_settings属性获取
		self.ai_settings = ai_settings
		#在飞船的属性center中存储小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
	
	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image,self.rect)
		
	def ship_moving(self):
		#飞船左右移动
		if self.moving_right_flage and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed
		if self.moving_left_flage and self.rect.left > self.screen_rect.left:
			self.centerx -= self.ai_settings.ship_speed
		#飞船上下移动
		if self.moving_up_flage and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_settings.ship_speed
		if self.moving_down_flage and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed
		#得到的值存入ship的rect属性中
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def ship_center(self):
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - self.rect.height/2
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		
