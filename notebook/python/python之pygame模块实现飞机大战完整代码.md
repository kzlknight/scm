本文实例为大家分享了python之pygame模块实现飞机大战的具体代码，供大家参考，具体内容如下

Python飞机大战步骤：

1.数据区  
2.主界面  
3.飞船  
4.事件监控及边界  
5.外星人  
6.记分系统  

飞机大战效果图：

![](https://img.jbzj.com/file_images/article/202011/20201129143558456.jpg)

![](https://img.jbzj.com/file_images/article/202011/20201129143859103.jpg)

**源码：**

```python

    """
    功能：飞机大战
    time：2019/10/3
    
    """
    import os
    import pygame
    import sys
    import time
    from pygame.sprite import Sprite, Group
    
    """
    1.定义主界面
    2.定义飞船位置
    3.边界及键盘操作
    4.记分系统
    """
    #1.数据区
    #定义一个参数类
    class Settings():
     def __init__(self):
     #屏幕设置
     self.screen_width = 1100
     self.screen_height = 600
     self.background = (230,230,230)
     self.background_image = pygame.image.load("C:/Users/Administrator/Desktop/xxx.jpg")
     #子弹设置
     self.bullet_width = 3
     self.bullet_height = 15
     self.bullet_color = 60,60,60
     # 屏幕上子弹的个数
     self.bullets_allow = 3
     #外星人设置
     self.fleet_drop_speed = 10
     self.ship_limit = 3
     #玩家升级后加快游戏速度
     self.speed_scale = 1.2
     #外星人点数提高的速度
     self.score_speed = 1.5
     #初始化随游戏变化的属性
     self.init_setting()
    
     #每个外星人的分数
     self.alien_points = 50
     def init_setting(self): #初始化随游戏变化的属性
     self.ship_speed = 1.6
     self.bullet_speed_factor = 2.5
     self.alien_speed_factor = 1
    
     #设置左右移动的标志，1右移，-1左移
     self.fleet_direction =1
     def increase_speed(self):
     #提高速度设置和外星人点数
     self.ship_speed *= self.speed_scale
     self.bullet_speed_factor *= self.speed_scale
     self.alien_speed_factor *=self.speed_scale
    
     self.alien_points = int(self.alien_points*self.score_speed)
     print(self.alien_points) #输出打印看点数是否增加
    
    #2.函数区
    #1）定义一个屏幕
    def update_screen(setting_1,screen,stats,score_b,ship,aliens,bullets,my_button):
     # 每次循环时绘制屏幕
     screen.fill(setting_1.background)
     #在飞船和外星人后面重新绘制子弹
     #screen.blit(setting_1.background_image,(0,0))
     for bullet in bullets.sprites():
     bullet.draw_bullet()
     #显示得分
     score_b.show_score()
     #让最近绘制的屏幕可见
     ship.ship_1()
     aliens.draw(screen)
     #如果屏幕属于非活跃状态，就绘制play按钮
     if not stats.game_active:
     my_button.draw_button()
     #让最近绘制的屏幕可见
     pygame.display.flip()
    # 主函数
    def run_deploy():
     pygame.init() #初始化
     setting_1 = Settings() #Settings类实例化
     screen = pygame.display.set_mode((setting_1.screen_width,setting_1.screen_height))
     pygame.display.set_caption("飞机大战")
     #创建Play按钮
     my_button = Button(setting_1,screen,"Play")
     #创建一艘飞船
     ship = Ship(setting_1.ship_speed,screen)
     # 创建一个存储子弹的编组
     bullets = Group()
     #创建一个外星人编组
     aliens = Group()
     #创建存储游戏统计信息的实例
     stats = Game_stats(setting_1)
     #创建记分牌
     score_b = Scoreboard(setting_1,screen,stats)
    
     #开始游戏
     while True:
     events(setting_1,screen,stats,score_b,my_button,ship,aliens,bullets) #事件监测
     if stats.game_active:
     #当游戏为活跃状态是，更新游戏元素
     ship.moving_1() #飞船移动
     update_bullet(setting_1,screen,stats,score_b,ship,aliens,bullets) #更新子弹并删除子弹
     update_aliens(setting_1,screen,stats,score_b,ship,aliens,bullets)
    
     update_screen(setting_1,screen,stats,score_b,ship,aliens,bullets,my_button) #更新屏幕
    
    #2）定义一个飞船
    class Ship(Sprite):
     def __init__(self,setting_1,screen):
     #初始化飞船，并设置其起始位置
     super(Ship,self).__init__()
     self.screen = screen
     self.ship_speed_setting = setting_1
    
     #加载飞船并获取外接矩阵
     self.image = pygame.image.load("../image001/ship.bmp")
     self.rect = self.image.get_rect()
     self.screen_rect = screen.get_rect()
     self.center = float(self.rect.centerx)
    
     #将图片放在底部中央
     self.rect.centerx = self.screen_rect.centerx
     self.rect.bottom = self.screen_rect.bottom
    
     #移动标志(目的是连续移动)
     self.moving_right_fag = False
     self.moving_left_fag = False
    
     def moving_1(self):
     """根据移动标志调整飞船位置"""
     if self.moving_right_fag and self.rect.right < self.screen_rect.right: # screen_rect.right 表示的为界面的宽度
     self.rect.centerx += self.ship_speed_setting
     if self.moving_left_fag and self.rect.left > 0:
     self.rect.centerx -= self.ship_speed_setting
    
     def ship_1(self):
     """指定的位置绘制飞船"""
     self.screen.blit(self.image,self.rect)
    
     def center_ship(self):
     #飞船居中
     self.center =self.screen_rect.centerx
    
    #3)检测键盘及鼠标响应
    def check_keydown_events(event,setting_1,screen,ship,bullets):
     """响应按键"""
     if event.key == pygame.K_RIGHT: #右移
     ship.moving_right_fag = True
     #print(pygame.K_RIGHT)
     elif event.key == pygame.K_LEFT: #左移
     ship.moving_left_fag = True
     elif event.key == pygame.K_SPACE:
     if len(bullets) <= setting_1.bullets_allow: #当子弹编组中子弹个数小于界面上限制的个数时，才会出现新的 子弹
     #创建一颗子弹，将其放入编组中
     new_bullet = Bullet(setting_1,screen,ship)
     bullets.add(new_bullet)
    
    def check_keyup_events(event,ship):
     if event.key ==pygame.K_RIGHT: #右移
     ship.moving_right_fag = False
     elif event.key == pygame.K_LEFT:
     ship.moving_left_fag = False
    
    def events(setting_1,screen,stats,score_b,my_button,ship,aliens,bullets):
     #设置监听鼠标及键盘事件
     for event in pygame.event.get():
     if event.type == pygame.QUIT: #判断没有任何输入的情况下，返回一个空列表
     # print(pygame.QUIT)
     # print(pygame.event)
     sys.exit()
    
     elif event.type == pygame.KEYDOWN: #判断键盘事件，返回键盘的整数ID，用于识别按键
     check_keydown_events(event,setting_1,screen,ship,bullets)
    
     elif event.type == pygame.KEYUP:
     check_keyup_events(event,ship)
    
     elif event.type == pygame.MOUSEBUTTONDOWN: #单击按钮
     mouse_x,mouse_y = pygame.mouse.get_pos()
     check_play_button(setting_1,screen,stats,score_b,my_button,ship,aliens,bullets,mouse_x,mouse_y)
    
    
    def check_fleet_edgs(setting_1,aliens):
     """检查外星人移动到的边缘，并采取措施"""
     for alien in aliens.sprites():
     if alien.check_edgs():
     change_fleet_direction(setting_1,aliens)
     break
    
    def change_fleet_direction(setting_1,aliens): #采取的措施
     #将整群人下移，并改变方向
     for alien in aliens.sprites():
     alien.rect.y += setting_1.fleet_drop_speed
     setting_1.fleet_direction *= -1
    
    def ship_hit(setting_1,screen,stats,score_b,ship,aliens,bullets):
     """响应被外星人撞到的飞船"""
     #将飞船数减1
     if stats.ship_left > 0:
     print(stats.ship_left)
     #将飞船数减1
     stats.ship_left -= 1
    
     #更新记分牌
     score_b.prep_ships()
    
     #清空外星人和子弹列表
     aliens.empty()
     bullets.empty()
    
     #创建一群新的外星人，并将飞船放在低端中央
    
     creet_fleet(setting_1,screen,ship,aliens)
     ship.center_ship()
     #暂停1秒
     time.sleep(1)
     else:
     stats.game_active = False
     pygame.mouse.set_visible(True) #显示光标
    
    def check_aliens_bottom(setting_1,screen,stats,score_b,ship,aliens,bullets):
     """检查是否有外星人到达屏幕底部"""
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
     if alien.rect.bottom >= screen_rect.bottom:
     # print(2*alien.rect.bottom,"###")
     # print(screen_rect.bottom)
    
     #向飞船撞到一样处理
     ship_hit(setting_1,screen,stats,score_b,ship,aliens,bullets)
     break
    def check_play_button(setting_1,screen,stats,score_b,my_button,ship,aliens,bullets,mouse_x,mouse_y):
     """单击按钮开始游戏"""
     button_clicked = my_button.rect.collidepoint(mouse_x,mouse_y)
     if button_clicked and not stats.game_active :
     #重置游戏速度
     setting_1.init_setting()
     pygame.mouse.set_visible(False) #隐藏光标
     #重置游戏统计信息
     stats.reset_stats()
     stats.game_active = True
    
     #重复记分牌图形
     score_b.prep_score()
     score_b.prep_high_score()
     score_b.prep_level()
     score_b.prep_ships()
    
     #清空外星人和子弹列表
     aliens.empty()
     bullets.empty()
    
     #创建外星人群，然后居中
     creet_fleet(setting_1,screen,ship,aliens)
     ship.center_ship()
    
    def check_high_score(stats,score_b):
     """检查是否但是了最高得分"""
     if stats.score > stats.high_score:
     stats.high_score = stats.score
     score_b.prep_high_score()
    
    
    
    # 3）定义射击的子弹
    
    class Bullet(Sprite):
     """飞船发射的子弹类"""
    
     def __init__(self,setting_1,screen,ship):
     """在飞船所处的位置创建一个子弹对象"""
     super(Bullet,self).__init__() # 初始化父类，此处主要初始化的是Sprite类
     self.screen = screen
     #根据pygame的Rect方法绘制子弹矩形 Rect方法跟4个参数 (x,y,d,h)
     self.rect = pygame.Rect(0,0,setting_1.bullet_width,setting_1.bullet_height)
     self.rect.centerx = ship.rect.centerx
     self.rect.top = ship.rect.top
     self.y = float(self.rect.y)
    
     self.color = setting_1.bullet_color
     self.speed_factor = setting_1.bullet_speed_factor
    
     def update(self):
     """向上移动子弹"""
     #更新子弹的位置
     self.y -= self.speed_factor
     #更新子弹的rect位置
     self.rect.y = self.y
    
     def draw_bullet(self):
     """在屏幕上绘制子弹"""
     pygame.draw.rect(self.screen,self.color,self.rect)
    #创建一个子弹更新机制
    def update_bullet(setting_1,screen,stats,score_b,ship,aliens,bullets):
     #更新子弹位置，并删除子弹
     bullets.update()
     #删除已消失的子弹，原因是由于pygame无法在屏幕外绘制子弹，而实际上是存在的，为了减少的内存的消耗，和对性能的影响
     for bullet in bullets.copy():
     if bullet.rect.bottom <=0:
     bullets.remove(bullet)
     check_bullet_alien_collision(setting_1,screen,stats,score_b,ship,aliens,bullets)
    
    def check_bullet_alien_collision(setting_1,screen,stats,score_b,ship,aliens,bullets):
    
     #检查是否有子弹击中外星人，如果是，就删除外星人和子弹,直接调用pygame的groupcollide方法
     collsinos = pygame.sprite.groupcollide(bullets,aliens,True,True)
     #击中外星人后记分
     if collsinos:
     for aliens in collsinos.values(): #为了消除一个外星人被两个子弹击中，或者1个子弹击中多个外星人
     stats.score += setting_1.alien_points*len(aliens)
     score_b.prep_score()
     check_high_score(stats,score_b)
     #如果消灭了所有外星人，子弹将全部消失，一群外星人重新出现
     if len(aliens) == 0 :
     #删除现有的子弹，加快游戏节奏
     bullets.empty()
     setting_1.increase_speed()
    
     #整群外星人消灭完，等级提升1级
     stats.level += 1
     score_b.prep_level()
     creet_fleet(setting_1,screen,ship,aliens)
    # 4）定义一个外星人类
    class Alien(Sprite):
     """表示单个外星人的类"""
     def __init__(self,setting_1,screen):
     super(Alien,self).__init__() #初始化外星人，并设置其位置
     self.screen = screen
     self.setting_1 = setting_1
    
     #加载外星人图片，设置rect属性
     self.image=pygame.image.load("../image001/alien.bmp") # 此处变量为image，不要进行变化，如果为images，程序会报错
     self.rect = self.image.get_rect()
     #外星人的初始位置
     self.rect.x = self.rect.width
     self.rect.y = self.rect.height
    
     #存储外星人的位置
     self.x = float(self.rect.x)
     def blitme(self):
     """绘制外星人"""
     self.screen.blit(self.image,self.rect)
     #检查外星人是否运动到边沿
     def check_edgs(self):
     screen_rect =self.screen.get_rect()
     if self.rect.right >= screen_rect.right:
     return True
     elif self.rect.left <= 0:
     return True
    
     def update(self):
     """向左移或右移外星人"""
     self.x += (self.setting_1.alien_speed_factor * self.setting_1.fleet_direction) #注意，此处应该乘以左右移动标志，如果传错参数，可能会导致外星人右移后整体消失
     self.rect.x = self.x #更新位置
    
    
    
    def get_number_alien_x(setting_1,alien_width): # 计算每一行可容纳的外星人数
     val_spaces_x = setting_1.screen_width -2*alien_width
     num_alien_x = int(val_spaces_x/(2*alien_width))
     return num_alien_x
    
    def get_number_alien_y(setting_1,ship_height,alien_height):
     avl_spaces_y = (setting_1.screen_height-(3*alien_height)-ship_height)
     number_rows = int(avl_spaces_y/(2*alien_height))
     return number_rows
    
    def creat_aliens(setting_1,screen,aliens,alien_number,row_number):
     """创建一个外星人，并放在当前行"""
     alien = Alien(setting_1,screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2*alien_width*alien_number
     alien.rect.x = alien.x
     alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
     aliens.add(alien) #注意此处添加的单个外星人，如果添加成aliens，第一行外星人会不显示，可以用print进行检查
    
    def creet_fleet(setting_1,screen,ship,aliens):
     """创建外星人人群"""
     alien = Alien(setting_1,screen)
     number_alien_x = get_number_alien_x(setting_1,alien.rect.width)
     number_rows = get_number_alien_y(setting_1,ship.rect.height,alien.rect.height)
     #创建外星人群
     for row_number in range(number_rows):
     #创建第一行外星人
     for alien_number in range(number_alien_x):
     creat_aliens(setting_1,screen,aliens,alien_number,row_number)
    
    def update_aliens(setting_1,screen,stats,score_d,ship,aliens,bullets):
     check_fleet_edgs(setting_1,aliens)
     aliens.update()
    
     # 检查外星人是否与飞船碰撞
     if pygame.sprite.spritecollideany(ship,aliens):
     #print("ship hit")
     ship_hit(setting_1,screen,stats,score_d,ship,aliens,bullets)
     #检查是否有外星人到达底部
     check_aliens_bottom(setting_1,screen,stats,score_d,ship,aliens,bullets)
    
    #5）射杀外星人
    #6) 消灭所有的外星人后，外星人群在重新生成,当发生碰撞，游戏结束
    #7) 限制飞船的个数3
    class Game_stats():
     """ 统计游戏信息"""
     def __init__(self,setting_1):
     #初始化
     self.setting_1 =setting_1
     self.reset_stats()
     #游戏活动状态标志，当为负数时，为False
     self.game_active = False
     #定义在__init__，目的是任何情况下都不重置最高分
     self.high_score = 0
     def reset_stats(self):
     """初始化游戏运行期间可能变化的统计信息"""
     self.ship_left = self.setting_1.ship_limit
     self.score = 0
     self.level = 1 # 等级
    
    #8）添加启动按钮和游戏结束时方便启动
    class Button():
     """添加游戏启动按钮"""
     def __init__(self,setting_1,screen,msg):
     """初始化按钮属性"""
     self.screen = screen
     self.screen_rect = screen.get_rect()
    
     #设置按钮的尺寸及其他属性
     self.width,self.height = 200,100
     self.button_color = (228,222,213)
     self.text_color = (255,255,255)
     self.font = pygame.font.SysFont(None,100)
    
     #创建按钮的rect对象
     self.rect = pygame.Rect(0,250,self.width,self.height)
     self.rect.centerx = self.screen_rect.centerx
    
     #按钮的标签只需创建一次
     self.prep_msg(msg)
     def prep_msg(self,msg):
     """将msg渲染成图形，然后居中"""
     self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
     self.msg_image_rect = self.msg_image.get_rect()
     self.msg_image_rect.center = self.rect.center
    
     def draw_button(self):
     #绘制一个按钮，在绘制文本
     self.screen.fill(self.button_color,self.rect)
     self.screen.blit(self.msg_image,self.msg_image_rect)
    
    
    #9)记分系统
    class Scoreboard():
     """显示得分信息"""
    
     def __init__(self,setting_1,screen,stats):
     self.screen = screen
     self.screen_rect = screen.get_rect()
     self.setting_1 = setting_1
     self.stats = stats
    
     #显示的分
     self.text_color = (30,30,30)
     self.font = pygame.font.SysFont(None,48)
    
     #准备初始得分图形
     self.prep_score()
     self.prep_high_score()
     self.prep_level()
     self.prep_ships()
     def prep_score(self):
    
     """得分图形渲染"""
     round_score = int(round(self.stats.score,-1)) # round 四舍五入 ,圆整到10、100、1000的整数倍
     score_str = "{:,}".format(round_score) #输出的格式
     self.score_image = self.font.render(score_str,True,self.text_color,self.setting_1.background)
    
     #将得分显示在左上角
     self.score_rect = self.score_image.get_rect()
     self.score_rect.right = self.screen_rect.right - 20
     self.screen_rect.top = 20
    
     def prep_high_score(self): #显示最高得分
     #将最高分的图形渲染
     high_score = int(round(self.stats.high_score,-1)) # round 四舍五入 ,圆整到10、100、1000的整数倍
     high_score_str = "{:,}".format(high_score) #输出的格式
     self.hight_score_image = self.font.render(high_score_str,True,self.text_color,self.setting_1.background)
    
     #将得分显示在中间角
     self.high_score_rect = self.hight_score_image.get_rect()
     self.high_score_rect.centerx = self.screen_rect.centerx
     self.high_score_rect.top = self.score_rect.top
     def prep_level(self): #显示等级
     """等级渲染图形"""
     self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.setting_1.background)
    
     #将等级显示在得分的下方
    
     self.level_rect = self.level_image.get_rect()
     self.level_rect.right = self.score_rect.right
     self.level_rect.top = self.score_rect.bottom +10
     def prep_ships(self): #显示剩余的飞船数
     self.ships = Group()
     for ship_number in range(self.stats.ship_left):
     ship = Ship(self.setting_1,self.screen)
     ship.rect.x = 10 + ship_number*ship.rect.width
     ship.rect.y = 10
     self.ships.add(ship)
    
    
     def show_score(self):
     """在屏幕上显示得分"""
     self.screen.blit(self.score_image,self.score_rect)
     self.screen.blit(self.hight_score_image,self.high_score_rect)
     self.screen.blit(self.level_image,self.level_rect)
     self.ships.draw(self.screen)
    
    #3.调用区
    if __name__ == "__main__":
     run_deploy()
```

所遇到的有5个坑：

**坑1：** 在绘制子弹的时候，执行代码中报错AttributeError: ‘pygame.Surface' object has no
attribute ‘bullet_width',分析了大半天，原因是由于形参传错导致的。一定要在程序中保持形参的一致性。

![](https://img.jbzj.com/file_images/article/202011/2020112914281010.png)

**坑2：**
我在定义读取飞船和外星人的图片时，定义了images参数，我定义了两个images参数，起初在读取图片时，飞船和外星人都能显示在界面上，而当我对外星人进行事件操作，时，程序发生错误
AttributeError: ‘Alien' object has no attribute
‘image'。纠结了好半天，才发现此处的参数应该为image，修改完之后问题解决。飞船的images下面再说

![](https://img.jbzj.com/file_images/article/202011/2020112914281011.png)

**坑3：**
在定义的外星人的左右移动时，我误将移动标志fleet_direction写成其他值，导致外星人右移消失不见，由于程序未发生报错，于是我采用了print语句，最后才发现是由于移动标志出错导致的。  
self.x += (self.setting_1.alien_speed_factor * self.setting_1.fleet_direction)  

**坑4：**
在对外星人碰到飞船和碰到界面底部导致游戏结束时，由于的飞船碰到底部逻辑定义有误，导致在最后一个飞船（定义了3个）触碰到界面底部无法终止游戏。由于程序中也没有报错，只能慢慢分析，最终原因是由于对游戏活动状态判断有误，最终将活动状态有True改为False解决<

![](https://img.jbzj.com/file_images/article/202011/20201129143913023.jpg)

**坑5：** 第2坑中提到的飞船images参数，导致画剩余的3个飞船是报错（前面绘制的飞船都没有问题） AttributeError: ‘Ship'
object has no attribute 'image  

![](https://img.jbzj.com/file_images/article/202011/2020112914281113.png)

**小技巧：** 在对图片上色值采取时，可以在网上在线提取图片中的色值。

** 性能：  ** 在用图片和背景色作为界面的背景时，图片大大降低了游戏的性能。

**注：** 纸上得来终觉浅，绝知此事要躬行。

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

