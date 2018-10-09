import pygame
import time
import random
width,height=480,700
screen=pygame.display.set_mode((width,height))
running=1
bullet=pygame.image.load(r"res\bullet1.png")
enemy_image=pygame.image.load(r"res\enemy1.png")
enemy_down=[pygame.image.load(r"res\enemy1_down1.png"),
            pygame.image.load(r"res\enemy1_down2.png"),
            pygame.image.load(r"res\enemy1_down3.png")]

class Timer:

     def __init__(self,interval=0.0003):

          self.timer=[time.time(),0]
          # print(self.timer)
          self.interval=interval
          self.draw_x=0

     def time_going(self):

          self.timer[1]=time.time()
          if self.timer[1]-self.timer[0]>=self.interval:#如

               self.timer[0]=self.timer[1]
               return True
          return False

     def time_blit(self,max_image):#敌机图片

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
          self.timer=Timer(0.005)#参数可以控制背景的刷新速度
          self.pos=[0,-height] # 它的背景图是两个合在一起的

     def draw_map(self,screen):

          if self.timer.time_going():

               self.pos[1]+=5
               if self.pos[1]>=0:
                    self.pos[1]=-height
          screen.blit(self.image,self.pos)#X轴坐标不变，y轴增加

class Bullet:

     group=[]
     def __init__(self,pos):

          self.pos=pos
          self.image=bullet
          Bullet.group.append(self)

     def draw_bullet(self,screen):

          self.run()#让子弹动起来
          screen.blit(self.image,self.pos)#绘制子弹
          bullet_rect=pygame.Rect(self.image.get_rect())#获取子弹位置
          bullet_rect.left=self.pos[0]
          bullet_rect.top=self.pos[1]
          for e in Enemy.Group:

               e_rect=pygame.Rect(e.image.get_rect())#获取敌机的位置值
               e_rect.left=e.pos[0]
               e_rect.top=e.pos[1]
               if e.pos[1]>690:
                    print('游戏结束')
                    ene=pygame.image.load('res/jie.png')
                    screen.blit(ene,(0,0))
                    me_down_sound = pygame.mixer.Sound('sound/me_down.wav')
                    me_down_sound.set_volume(1)
                    me_down_sound.play()
                    # for i in Enemy.Group:
                    #      Enemy.Group.remove(i)
               elif bullet_rect.colliderect(e_rect):#colliderect这个函数就是判断碰撞的
                    # ene=pygame.image.load('res/jie.png')
                    # screen.blit(ene,(0,0))
                    e.health-=10
                    try:

                         Bullet.group.remove(self)  # 有一个错误，这个不用管，我测试用的
                    except:
                         print('错误')
                    else:
                         print('错误')


     def run(self):

          self.pos[1]-=5
          if self.pos[1]<=0:#超出去的子弹自动销毁
               # pygame.quit()
               # exit()
               Bullet.group.remove(self)
class Player:


     def __init__(self):

          self.pos=[240,426]
          self.timer=Timer(0.005)
          self.fire_timer=Timer(0.08)
          self.image=[pygame.image.load(r"res\hero1.png"),
                      pygame.image.load(r"res\hero2.png")]

     def draw_player(self,screen):

          # self.pos=pygame.mouse.get_pos()
          x, y = pygame.mouse.get_pos()  #  获取鼠标中心点
          self.pos = (x-51,y-63)
          screen.blit(self.image[self.timer.time_blit(2)],self.pos)
          if self.fire_timer.time_going():

               self.fire()
     def fire(self):

          temp_pos=[self.pos[0]+51,self.pos[1]]# 51是我方机一半
          temp_bullet=Bullet(temp_pos)
     # def pdie():


class Enemy:

     Group=[]
     Group1 = []
     def __init__(self,pos):
          self.timer=Timer(0.000005)
          self.pos=pos
          self.die_timer=Timer(0.01) #死的速度
          self.image=enemy_image
          self.rect = self.image.get_rect()
          self.down=enemy_down
          self.health=30
          Enemy.Group1.append(self.rect)
          Enemy.Group.append(self)

     def draw_enemy(self,screen,rubbish):

          self.run(rubbish)
          screen.blit(self.image,self.pos)

     def run(self,rubbish):

          self.pos[1]+=0.9
          if self.health<=0:

               rubbish.append(self)
               Enemy.Group.remove(self)#移除击落敌机
     def play_dead(self,rubbish):

          screen.blit(self.down[self.die_timer.time_blit(3)],self.pos)#击毁后消失
          # print(self.die_timer.time_blit(3))
          if self.die_timer.draw_x==2:

               rubbish.remove(self)#击落后显示的图片的删除
     @staticmethod
     def make_enemy():

          pos=[random.randint(20,380),0]
          temp_enemy=Enemy(pos)

maper=Map()
player=Player()
rubbish=[]
