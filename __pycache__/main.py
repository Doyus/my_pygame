import pygame
from init_mod import *
timer=[time.time(),0]



while running:

     try:
          screen.fill((255,255,255))
          maper.draw_map(screen)
          player.draw_player(screen)
          for bullet in Bullet.group:
          
               bullet.draw_bullet(screen)
     
          timer[1]=time.time()
          if timer[1]-timer[0]>=0.5:
          

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
     except:

          pass
