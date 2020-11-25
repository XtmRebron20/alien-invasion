import pygame.font
class Scoreboard():
	def __init__(self,ai_settings,screen,stats):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings 
		self.stats = stats
		
		#得分颜色和字体
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont('arial',48)
		
		self.prep_score()
		self.prep_level()
		self.prep_ships_left()
	def prep_score(self):
		#得分转换为图像
		score_str = 'Score: '+str(int(self.stats.score))
		self.score_image = self.font.render(score_str,True,
			self.text_color,self.ai_settings.bg_color)
		#定位至右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def prep_level(self):
		#等级转换图像
		level_str = 'Level '+str(int(self.stats.level))
		self.level_image = self.font.render(level_str,True,
			self.text_color,self.ai_settings.bg_color)
		#定位至顶部中间
		self.level_rect = self.score_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = 20
	
	def prep_ships_left(self):
		#生命转换图像
		ships_left_str = 'HP: '+str(int(self.stats.ships_left))
		self.ships_left_image = self.font.render(ships_left_str,True,
			self.text_color,self.ai_settings.bg_color)
		#定位至顶部中间
		self.ships_left_rect = self.score_image.get_rect()
		self.ships_left_rect.left = self.screen_rect.left
		self.ships_left_rect.top = 20
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.screen.blit(self.ships_left_image,self.ships_left_rect)

		
		 
		
