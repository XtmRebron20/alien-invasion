class Settings():
	def __init__(self):
		#存储《外星人入侵》的所有设置的类
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#飞船数量
		self.ship_limit = 3
		
		#速度增长系数
		self.speed_modulus = 1.1
		
		#得分增长系数
		self.score_modulus = 1.5
		
	def initialize_speed(self):
		#每个外星人得分
		self.alien_points = 10
		
		#飞船的移动速度
		self.ship_speed = 2
		
		#子弹的移动速度
		self.bullet_speed = 1
		
		'''#子弹的开火速度
		self.fire_speed = 1'''
		
		#外星人左右速度
		self.alien_x_speed = 0.5
		
		#外星人下降速度
		self.alien_y_speed = 2
		
		#外星人左右移动标志(0左，1右)
		self.alien_x_moving_flage = 1
		
	def increase_speed(self):
		#所有速度增长
		#self.ship_speed *= self.speed_modulus
		self.bullet_speed *= self.speed_modulus
		self.alien_x_speed  *= self.speed_modulus
		self.alien_y_speed *= self.speed_modulus
		self.alien_points *= self.score_modulus 
