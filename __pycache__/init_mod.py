import pygame
import time
import random
width,height=480,852
screen=pygame.display.set_mode((width,height))
running=1
bullet=pygame.image.load(r"res\bullet1.png")
enemy_image=pygame.image.load(r"res\enemy1.png")
enemy_down=[pygame.image.load(r"res\enemy1_down1.png"),
            pygame.image.load(r"res\enemy1_down2.png"),
            pygame.image.load(r"res\enemy1_down3.png")]

class Timer:

     def __init__(self,interval=0.5):

          self.timer=[time.time(),0]
          print(self.timer)
          self.interval=interval
          self.draw_x=0

     def time_going(self):

          self.timer[1]=time.time()
          if self.timer[1]-self.timer[0]>=self.interval:

               self.timer[0]=self.timer[1]
               return True
          return False

     def time_blit(self,max_image):

          self.timer[1]=time.time()

          if self.timer[1]-self.timer[0]>=self.interval:

               self.draw_x+=1
               if self.draw_x==max_image:
                    self.draw_x=0
                #如果该动作结束，则重头开始换帧

               self.timer[0]=self.timer[1]
            #刷新时间的起点
          return self.draw_x

class Map:

     def __init__(self):

          self.image=pygame.image.load(r"res\bg.png")
          self.timer=Timer(0.05)
          self.pos=[0,-height]

     def draw_map(self,screen):

          if self.timer.time_going():

               self.pos[1]+=5
               if self.pos[1]>=0:
                    self.pos[1]=-height
          screen.blit(self.image,self.pos)

class Bullet:

     group=[]
     def __init__(self,pos):

          self.pos=pos
          self.image=bullet
          Bullet.group.append(self)

     def draw_bullet(self,screen):

          self.run()
          screen.blit(self.image,self.pos)
          bullet_rect=pygame.Rect(self.image.get_rect())
          bullet_rect.left=self.pos[0]
          bullet_rect.top=self.pos[1]
          for e in Enemy.Group:

               e_rect=pygame.Rect(e.image.get_rect())
               e_rect.left=e.pos[0]
               e_rect.top=e.pos[1]
               if bullet_rect.colliderect(e_rect):

                    e.health-=10
                    Bullet.group.remove(self)

          # '''
          #     bullrect=pygame.Rect(arrow.get_rect())
          #      bullrect.left=bullet[1]
          #      bullrect.top=bullet[2]
          # '''

     def run(self):

          self.pos[1]-=5
          if self.pos[1]<=0:

               Bullet.group.remove(self)
class Player:


     def __init__(self):

          self.pos=[240,426]
          self.timer=Timer(0.05)
          self.fire_timer=Timer(0.08)
          self.image=[pygame.image.load(r"res\hero1.png"),
                      pygame.image.load(r"res\hero2.png")]

     def draw_player(self,screen):

          self.pos=pygame.mouse.get_pos()
          screen.blit(self.image[self.timer.time_blit(2)],self.pos)
          if self.fire_timer.time_going():

               self.fire()
     def fire(self):

          temp_pos=[self.pos[0]+51,self.pos[1]]
          temp_bullet=Bullet(temp_pos)

class Enemy:

     Group=[]
     def __init__(self,pos):

          self.pos=pos
          self.die_timer=Timer(0.3)
          self.image=enemy_image
          self.down=enemy_down
          self.health=30
          Enemy.Group.append(self)

     def draw_enemy(self,screen,rubbish):

          self.run(rubbish)
          screen.blit(self.image,self.pos)

     def run(self,rubbish):

          self.pos[1]+=0.3
          if self.health<=0:

               rubbish.append(self)
               Enemy.Group.remove(self)
     def play_dead(self,rubbish):

          screen.blit(self.down[self.die_timer.time_blit(3)],self.pos)
          if self.die_timer.draw_x==2:

               rubbish.remove(self)
     @staticmethod
     def make_enemy():

          pos=[random.randint(20,460),0]
          temp_enemy=Enemy(pos)

maper=Map()
player=Player()
rubbish=[]
