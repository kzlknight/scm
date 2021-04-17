贪吃蛇作为一款经典小游戏，早在 1976 年就面世了，我最早接触它还是在家长的诺基亚手机中。

![](https://img.jbzj.com/file_images/article/202012/2020120710294855.gif)

尽管贪吃蛇的历史相对比较久远，但它却有着十分顽强的生命力，保持经久不衰，其中很重要的原因便是游戏厂家不断的对其进行更新迭代。现在，这款游戏无论是游戏场景、规则等都变得十分丰富。

![](https://img.jbzj.com/file_images/article/202012/2020120710294856.gif)

接下来，我们看一下如何通过 Python 简单的实现这款小游戏。

**规则**

  * 要有游戏主界面、贪吃蛇、食物 
  * 能够控制贪吃蛇移动并获取食物 
  * 贪吃蛇吃了食物后，增加自身长度、分数，食物消失并随机生成新的食物 
  * 贪吃蛇触碰到周围边界或自己身体时，游戏结束 

**环境**

  * 操作系统：Windows 
  * Python 版本：3.6 
  * 涉及模块：sys、random、pygame 

**实现**

首先，安装第三方库 pygame，使用 ` pip install pygame ` 即可。

➢ 游戏主界面

```python

    SCREEN_X = 500
    SCREEN_Y = 500
    screen_size = (SCREEN_X, SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('贪吃蛇')
```

➢ 贪吃蛇

初始化

```python

    def __init__(self):
     self.dirction = pygame.K_RIGHT
     self.body = []
```

移动

```python

    def addNode(self):
     left, top = (0, 0)
     if self.body:
     left, top = (self.body[0].left, self.body[0].top)
     node = pygame.Rect(left, top, 20, 20)
     if self.dirction == pygame.K_LEFT:
     node.left -= 20
     elif self.dirction == pygame.K_RIGHT:
     node.left += 20
     elif self.dirction == pygame.K_UP:
     node.top -= 20
     elif self.dirction == pygame.K_DOWN:
     node.top += 20
     self.body.insert(0, node)
    
    def delNode(self):
     self.body.pop()
```

改变方向

```python

    def changeDirection(self, curkey):
     LR = [pygame.K_LEFT, pygame.K_RIGHT]
     UD = [pygame.K_UP, pygame.K_DOWN]
     if curkey in LR + UD:
     if (curkey in LR) and (self.dirction in LR):
      return
     if (curkey in UD) and (self.dirction in UD):
      return
     self.dirction = curkey
```

死亡判断

```python

    def isDead(self):
     # 撞墙
     if self.body[0].x not in range(SCREEN_X):
     return True
     if self.body[0].y not in range(SCREEN_Y):
     return True
     # 撞自己
     if self.body[0] in self.body[1:]:
     return True
     return False
```

➢ 食物

投放食物

```python

    def set(self):
     if self.rect.x == -20:
     allpos = []
     for pos in range(20, SCREEN_X - 20, 20):
      allpos.append(pos)
     self.rect.left = random.choice(allpos)
     self.rect.top = random.choice(allpos)
     print(self.rect)
```

吃掉食物

```python

    def remove(self):
     self.rect.x = -20
```

➢ 文字显示

显示方法

```python

    def show_text(screen, pos, text, color, font_bold=False, font_size=30, font_italic=False):
     # 设置文字大小
     cur_font = pygame.font.SysFont("宋体", font_size)
     # 加粗
     cur_font.set_bold(font_bold)
     # 斜体
     cur_font.set_italic(font_italic)
     # 设置内容
     text_fmt = cur_font.render(text, 1, color)
     # 绘制文字
     screen.blit(text_fmt, pos)
```

显示分数

```python

    show_text(screen, (50, 400), 'scores: ' + str(scores), (103, 213, 213))
```

显示死亡提示

```python

    show_text(screen, (150, 50), 'GAME OVER', (227, 29, 18), False, 50)
    show_text(screen, (140, 100), "Press space to try again", (0, 0, 22), False, 30)
```

➢ 吃到食物

当贪吃蛇吃掉食物，增加蛇身长度、分数，食物消失，重新投放食物。

```python

    if food.rect == snake.body[0]:
     scores += 1
     food.remove()
     snake.addNode()
    
    # 投放食物
    food.set()
```

➢ 最终效果

![](https://img.jbzj.com/file_images/article/202012/2020120710294857.gif)

打包

打包使用 pyinstaller，具体实现参考 [ 用Python实现童年小游戏俄罗斯方块
](https://www.jb51.net/article/185392.htm)

中的打包。

到此这篇关于用Python实现贪吃蛇童年小游戏功能的实例代码的文章就介绍到这了,更多相关Python贪吃蛇小游戏内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

