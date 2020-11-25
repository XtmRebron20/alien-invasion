import pygame.font
class Button():
	def __init__(self,screen,ai_settings,):
		#屏幕属性存储
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		#加载图片
		self.image = pygame.image.load(r'alien_invasion\images\button_play.png')
		self.rect = self.image.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
	def draw_button(self):
		self.screen.blit(self.image,self.rect)
