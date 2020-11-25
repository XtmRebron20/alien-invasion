import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,
		ai_settings.screen_height))
	pygame.display.set_caption("外星人入侵")
	#创建一个‘开始’按钮
	button_play = Button(screen,ai_settings)
	#创建一个用于保存游戏信息的类和一个记分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	#创建一艘飞船
	new_ship = Ship(screen,ai_settings)
	
	#创建一个用于存储子弹的Group
	all_bullets = Group()
	#创建一个用于存储外星人的Group
	all_aliens = Group()
	#创建一群外星人
	gf.make_aliens(ai_settings,screen,all_aliens,new_ship)
	
	#开始游戏主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_event(new_ship,ai_settings,screen,all_bullets,stats,
			button_play,all_aliens,sb)
		if stats.game_active == True:
			'''#创建新子弹
			gf.make_new_bullet(new_ship,all_bullets,ai_settings,screen,new_ship)'''
			#所有子弹移动
			gf.all_bullets_moving(all_bullets,all_aliens,ai_settings,
				screen,new_ship,stats,sb)
			#所有外星人移动
			gf.aliens_moving(all_aliens,ai_settings,new_ship,stats,
				screen,all_bullets,sb)
			#飞船移动
			new_ship.ship_moving()
		#每次循环时都会绘制屏幕
		gf.update_screen(screen,new_ship,ai_settings,all_bullets,
			all_aliens,stats,button_play,sb)
run_game()
