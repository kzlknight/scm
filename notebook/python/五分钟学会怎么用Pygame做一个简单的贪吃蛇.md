Pygame 是一组用来开发游戏软件的 Python 程序模块，基于 SDL 库的基础上开发。我们今天将利用它来制作一款大家基本都玩过的小游戏――贪吃蛇。

![](https://img.jbzj.com/file_images/article/202101/202116172018943.jpg?202106172036)

##  一、需要导入的包

```python

    import pygame
    import time
    import random
```

  * pygame：获取图形组件构建游戏 
  * time：主要用来设置帧率 
  * random：主要用来设置食物的刷新位置 

##  二、窗口界面设置

首先我们初始化游戏，建立一个窗口

```python

    pygame.init()
```

然后我们定义游戏中需要使用的颜色，在这个示例中，我们定义了六种颜色

```python

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
```

接下来，我们设置窗口的尺寸和标题栏，在这个示例中，我们将窗口设置为800*600

```python

    dis_width = 800
    dis_height = 600
    
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('贪吃蛇游戏')
```

##  三、游戏中的变量

初始化一个clock变量，使用开头导入的time包。这个变量将用来处理游戏的帧率。

```python

    clock = pygame.time.Clock()
```

定义蛇的速度与大小。可以随意更改，选择你适应的即可

```python

    snake_block = 10
    snake_speed = 12
```

设置分数显示和其他信息的字体大小与样式。

```python

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
```

##  四、设置功能函数

定义三个辅助功能函数，实现以下功能。

  * 显示计算分数 
  * 蛇的参数 
  * 其他消息显示，比如失败后的重玩提示。 

首先，定义一个计算分数的函数

```python

    def Your_score(score):
      value = score_font.render("Your Score: " + str(score), True, yellow)
      dis.blit(value, [0, 0]
```

接下来定义蛇的参数。我们定义了蛇的颜色，位置与大小，即snake_block。我们额外定义了一个snake_list作为输入，将在下面用到。

```python

    def our_snake(snake_block, snake_list):
     for x in snake_list:
     pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    
```

最后定义一个消息显示函数，这个辅助函数将msg和颜色作为输入参数。我们将设置字体，然后以所需的颜色显示信息。我们需要指定信息在游戏中显示的位置。

```python

    def message(msg, colour):
     mesg = font_style.render(msg, True, colour)
     dis.blit(mesg, [width / 6, height / 3])
```

##  五、构建游戏

开始建立游戏循环，让游戏运行并能响应键盘输入。首先定义两个变量game_over和game_close，用来描述游戏的状态。第一个提示游戏是否结束，下一个定义是否关闭游戏。都定义为false

```python

    game_over = False
    game_close = False
```

下一步，我们将定义x1和y1来表示蛇在游戏中的位置。我们分别初始化它们的宽度/2和高度/2。同时，我们将定义变量x1_change和y1_change来表示蛇的位置根据用户提供的输入而发生的变化。

```python

    x1 = width / 2
    y1 = height / 2
    
    x1_change = 0
    y1_change = 0
```

另外，我们还需要定义snake_List和snake_length变量，分别存储蛇的所有头部位置和蛇的长度。

```python

    snake_List = []
    snake_length = 1
```

吃掉食物新食物产生的位置，用random模块来实现。

```python

    foodx = round(random.randrange(0, width ― snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height ― snake_block) / 10.0) * 10.0
```

接下来，我们将启动一个循环，直到game_over变成True为止。

在这个循环中，我们将首先定义在 game_close 变量为 True 时要执行的指令。

下面的代码将帮助我们处理game_close等于True时的情况。

```python

    while game_close == True:
          dis.fill(blue)
          message("Lost! q quit or p again", red)
          Your_score(Length_of_snake - 1)
          pygame.display.update()
    
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                game_over = True
                game_close = False
              if event.key == pygame.K_p:
                gameLoop()
```

如你所见，我们已经定义了很多东西。我们用蓝色填充显示（你当然可以选择你的颜色）。游戏结束时，我们显示一条消息，显示该用户输掉了游戏，我们应该询问用户是想再玩一次还是退出游戏。

我们也会显示用户的分数，等于蛇的长度减1。每当我们的蛇吃到食物时，我们都会更新1分。

现在，为了接受用户关于他是想再玩一次还是退出游戏的输入，我们定义了一个for-loop。当我们要求用户输入关于他的决定时，我们定义了输入的可能性。

如果用户输入的是'p'，那么我们将继续我们的游戏循环。如果用户输入的是'q'，那么我们就需要退出游戏。

现在，在处理完game_close的条件后，我们将定义所有需要的步骤，这将使我们的蛇根据用户的输入移动。我们将接受W、A、S、D和上、下、左、右键组合来进行游戏。你可以自由选择你的按键来玩游戏。

```python

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      game_over = True
     if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
       x1_change = -snake_block
       y1_change = 0
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
       x1_change = snake_block
       y1_change = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
       y1_change = -snake_block
       x1_change = 0
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
       y1_change = snake_block
       x1_change = 0
```

在上面的代码中，我们根据用户提供的输入改变x1_change和y1_change的值。同时，如果用户想退出游戏，我们也会退出游戏。

接下来，我们将定义输掉游戏的条件。同时，我们借助x1_change和y1_change更新x1和y1的值。我们还将用蓝色填充整个显示屏，并通过在显示屏中传递蛇和食物的出现位置来绘制它们。

```python

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
      game_close = True
     x1 += x1_change
     y1 += y1_change
     dis.fill(blue)
     pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
```

接下来，我们定义一个名为snake_Head的列表，它将在每次迭代后存储蛇头的值。我们将x1和y1的值追加到它上面。然后，我们将该snake_Head追加到snake_List中。

然后我们检查条件检查snake_List的长度是否大于snake_length。如果是，则删除snake_List中的第一个元素。

然后，我们检查当前的snake_Head是否等于snake_List中的任何一个元素，除了新增加的那个元素，也就是被检查的snake_Head。如果是，那么我们就关闭游戏，玩家就输了。

这是因为在snake_List中出现snake_Head意味着它曾经被添加到snake_List中，再次找到相同的值意味着蛇碰到了自己。所以，此时游戏介绍。

然后我们调用函数our_snake和Your_score(前面定义的)，并将所需参数传递给这些函数，以显示更新后的蛇和玩家的分数。

```python

     snake_Head = []
     snake_Head.append(x1)
     snake_Head.append(y1)
     snake_List.append(snake_Head)
     if len(snake_List) > snake_length:
      del snake_List[0]
    
     for x in snake_List[:-1]:
      if x == snake_Head:
       game_close = True
    
     our_snake(snake_block, snake_List)
     Your_score(snake_length ― 1)
    
     pygame.display.update()
```

接下来，我们将在蛇吃完前一个食物后，形成新的食物。所以，为了做到这一点，我们需要在显示屏中找到一个新的随机位置来生成食物。另外，由于蛇刚吃完食物，我们需要将蛇的长度增加1。

最后，我们将蛇的速度作为参数给clock.tick，作为游戏的帧率。

```python

    if x1 == foodx and y1 == foody:
     foodx = round(random.randrange(0, width ― snake_block) / 10.0) * 10.0
     foody = round(random.randrange(0, height ― snake_block) / 10.0) * 10.0
     snake_length += 1
    
    clock.tick(snake_speed)
```

功能已经完全实现，我们最后退出游戏，并再次调用游戏循环

```python

    pygame.quit()
      quit()
    
    gameLoop()
```

##  六、完整代码

```python

    import pygame
    import time
    import random
    
    pygame.init()
    
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    
    dis_width = 800
    dis_height = 600
    
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('贪吃蛇')
    
    clock = pygame.time.Clock()
    
    snake_block = 10
    snake_speed = 15
    
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    
    def Your_score(score):
      value = score_font.render("Score: " + str(score), True, yellow)
      dis.blit(value, [0, 0])
    
    def our_snake(snake_block, snake_list):
      for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    
    def message(msg, color):
      mesg = font_style.render(msg, True, color)
      dis.blit(mesg, [dis_width / 6, dis_height / 3])
    
    def gameLoop():
      game_over = False
      game_close = False
    
      x1 = dis_width / 2
      y1 = dis_height / 2
    
      x1_change = 0
      y1_change = 0
    
      snake_List = []
      Length_of_snake = 1
    
      foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
      while not game_over:
    
        while game_close == True:
          dis.fill(blue)
          message("Lost! q quit or p again", red)
          Your_score(Length_of_snake - 1)
          pygame.display.update()
    
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                game_over = True
                game_close = False
              if event.key == pygame.K_p:
                gameLoop()
    
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            game_over = True
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
              x1_change = -snake_block
              y1_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
              x1_change = snake_block
              y1_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
              y1_change = -snake_block
              x1_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
              y1_change = snake_block
              x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
          game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
          del snake_List[0]
    
        for x in snake_List[:-1]:
          if x == snake_Head:
            game_close = True
    
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
    
        pygame.display.update()
    
        if x1 == foodx and y1 == foody:
          foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
          foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
          Length_of_snake += 1
    
        clock.tick(snake_speed)
    
      pygame.quit()
      quit()
    
    gameLoop()
```

更多关于python的文章，欢迎关注python客栈。

![](https://img.jbzj.com/file_images/article/202012/20201224160001239.png?2020112416011)

以上就是五分钟学会怎么用Pygame做一个简单的贪吃蛇的详细内容，更多关于pygame 贪吃蛇的资料请关注脚本之家其它相关文章！

