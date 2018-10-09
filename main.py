import pygame
from init_mod import *
pygame.init()
timer=[time.time(),0]
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('sound/game_music.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('sound/game_music.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
while running:





     maper.draw_map(screen)
     player.draw_player(screen)
     for bullet in Bullet.group:

          bullet.draw_bullet(screen)

     timer[1]=time.time()
     if timer[1]-timer[0]>=0.3:#创建敌机的


          Enemy.make_enemy()
          timer[0]=timer[1]
     for enemy_ in Enemy.Group:

          enemy_.draw_enemy(screen,rubbish)

     for i in rubbish:

          i.play_dead(rubbish)
     pygame.display.flip()
     for event in pygame.event.get():

          if event.type==pygame.QUIT:

               pygame.quit()
               exit(0)
     # for i in Enemy.Group1:
     #      print(i.y)
     #      if i.y>700:
     #           print('游戏结束')
