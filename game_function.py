import sys
import pygame
from bullet import Bullet
from pygame.sprite import Sprite
from alien import Alien
from time import sleep
from ship import Ship
from settings import Settings
from game_stats import GameStats
	
'''def make_new_bullet(ship,all_bullets,ai_settings,screen,new_ship):
	#建立一个新子弹
	if ship.fire_flage:
			sleep(0.1)
			new_bullet = Bullet(ai_settings,screen,new_ship)
			all_bullets.add(new_bullet)'''
def check_event(new_ship,ai_settings,screen,all_bullets,stats,
		button_play,all_aliens,sb):
	#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				#按下键盘后标志改变
				if event.key == pygame.K_RIGHT:
					new_ship.moving_right_flage = True	
				if event.key == pygame.K_LEFT:
					new_ship.moving_left_flage = True
				if event.key == pygame.K_UP:
					new_ship.moving_up_flage = True
				if event.key == pygame.K_DOWN:
					new_ship.moving_down_flage = True
				'''#按下空格键建立设置开火标志为True'''
				if event.key == pygame.K_SPACE:
					new_bullet = Bullet(ai_settings,screen,new_ship)
					all_bullets.add(new_bullet)
					'''new_ship.fire_flage = True'''
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#检测鼠标键按下
				mouse_x,mouse_y = pygame.mouse.get_pos()
				check_play_button(stats,button_play,mouse_x,mouse_y,
								all_aliens,all_bullets,new_ship,
								ai_settings,screen,sb)
				
			elif event.type == pygame.KEYUP:
				#松开键盘后标志改变
				if event.key == pygame.K_RIGHT:
					new_ship.moving_right_flage = False
				if event.key == pygame.K_LEFT:
					new_ship.moving_left_flage = False
				if event.key == pygame.K_UP:
					new_ship.moving_up_flage = False
				if event.key == pygame.K_DOWN:
					new_ship.moving_down_flage = False	
				'''#松开空格键建立设置开火标志为False
				if event.key == pygame.K_SPACE:
					new_ship.fire_flage = False'''
def check_play_button(stats,button_play,mouse_x,mouse_y,all_aliens,
					all_bullets,new_ship,ai_settings,screen,sb):
	if (button_play.rect.collidepoint(mouse_x,mouse_y)) and (not 
		stats.game_active): 
		#如果鼠标点击位置在按钮坐标内
		#重置所有数据
		
		stats.reset_stats()
		sb.prep_ships_left()
		sb.prep_score()
		sb.prep_level()
		ai_settings.initialize_speed()
		stats.game_active =True	
		
			
def update_screen(screen,ship,ai_settings,all_bullets,aliens,stats,
		button_play,sb):
	#每次循环时都会绘制屏幕
		#屏幕上色
		screen.fill(ai_settings.bg_color)
		#绘制每一个子弹
		for bullet in all_bullets:
			bullet.blitem()
		#绘制飞船
		ship.blitme()
		#绘制外星人
		for a_alien in aliens:
			a_alien.blit()
		#绘制得分
		sb.show_score()
		#绘制开始按钮
		if stats.game_active == False:
			button_play.draw_button()
		#让最近绘制的屏幕可见
		pygame.display.flip()
		
def all_bullets_moving(all_bullets,all_aliens,ai_settings,screen,
		new_ship,stats,sb):
	#所有子弹移动，如果超出范围，删除它
	for a_bullet in all_bullets:
		a_bullet.bullet_moving()
		if a_bullet.rect.bottom == 0:
			all_bullets.remove(a_bullet)
	#如果子弹击中外星人
	check_bullet_alien_collisions(ai_settings,screen,stats,sb,new_ship,
		all_aliens,all_bullets)
	#检测外星人是否全部被消灭
	if len(all_aliens) == 0:
		ai_settings.increase_speed()
		make_aliens(ai_settings,screen,all_aliens,new_ship)
		stats.level += 1
		sb.prep_level() 
		
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,new_ship,
		all_aliens,all_bullets):
	#响应子弹与飞船碰撞
	#如果发生碰撞，两者都删去
	collisions = pygame.sprite.groupcollide(all_bullets,all_aliens,True,
		True)
	#得分增加
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
					
def get_number_aliens_x(ai_settings,alien_width):
	#计算外星人列数
	availible_space_x = ai_settings.screen_width - 2*alien_width
	number_x = int(availible_space_x / (2*alien_width))
	return number_x
	
def get_number_aliens_y(ai_settings,alien_height,new_ship):
	#计算外星人行数
	availible_space_y = (ai_settings.screen_height - alien_height
						- 3*new_ship.rect.height)
	number_y = int(availible_space_y / (2*alien_height))
	return number_y

def make_aliens(ai_settings,screen,all_aliens,new_ship):
	#创建一群外星人
	alien_ex = Alien(screen,ai_settings)
	alien_ex_width = alien_ex.rect.width
	alien_ex_height = alien_ex.rect.height
	
	#获取外星人列数
	number_alien_x = get_number_aliens_x(ai_settings,alien_ex_width)
	#获取外星人行数
	number_alien_y = get_number_aliens_y(ai_settings,alien_ex_height,
		new_ship)
	
	for number_count_x in range(number_alien_x):
		for number_count_y in range(number_alien_y):
			alien=Alien(screen,ai_settings)
			alien.alien_x = (alien.rect.width + 
				2*alien.rect.width*number_count_x)
			alien.alien_y = (alien.rect.height + 
				2*alien.rect.height*number_count_y)
			
			alien.rect.x = alien.alien_x
			alien.rect.y = alien.alien_y
			
			all_aliens.add(alien)
def aliens_moving(all_aliens,ai_settings,new_ship,stats,screen,
		all_bullets,sb):
	#如果外星人到边缘，下降并且标志翻转
	for a_alien_1 in all_aliens:
		if a_alien_1.check_alien_position():
			for a_alien_2 in all_aliens:
				a_alien_2.alien_y += ai_settings.alien_y_speed
				a_alien_2.rect.y = a_alien_2.alien_y
	#左右移动
	all_aliens.update()
	#检测外星人撞击
	if pygame.sprite.spritecollideany(new_ship,all_aliens):
		ship_hit(ai_settings,stats,screen,new_ship,all_aliens,
			all_bullets,sb)
	check_aliens_bottom(ai_settings,stats,screen,new_ship,all_aliens,
		all_bullets,sb)
		
def check_aliens_bottom(ai_settings,stats,screen,new_ship,all_aliens,
		all_bullets,sb):
	#检测外星人是否到达底部
	screen_rect = screen.get_rect()
	for alien in all_aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,new_ship,all_aliens,
				all_bullets,sb)
			break
			
	
	
def ship_hit(ai_settings,stats,screen,ship,all_aliens,all_bullets,sb):
	#响应外星人撞到飞船
	#飞船数减少一个
	if stats.ships_left > 1:
		stats.ships_left -= 1
		sb.prep_ships_left()
	else:
		stats.game_active = False
	#清空外星人和子弹列表
	all_aliens.empty()
	all_bullets.empty()
	
	#飞船放到底部中央
	ship.ship_center()
	
	#创建一群新的外新人
	make_aliens(ai_settings,screen,all_aliens,ship)
	
	sleep(1)
	
