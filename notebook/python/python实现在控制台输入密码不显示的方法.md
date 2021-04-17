本文实例讲述了python实现在控制台输入密码不显示的方法。分享给大家供大家参考。具体实现方法如下：

```python

    import console;
    namespace console{
      //控制台读取密码，并显示星号
      getPassword = function(){
        var tstr = {};
        var input = kbRead(true);
        while( input.wVirtualKeyCode != 0xD/*_VK_ENTER*/ ){
          if( input.uChar.asciiChar ){
            ..table.push(tstr,input.uChar.asciiChar);
            if( input.uChar.asciiChar > 0x80){
              ..table.push(tstr,kbRead(true).uChar.asciiChar);
            }
            ..io.stdout.write("*");
          }
          input = kbRead(true);
        }
        ..io.stdout.write('\n');
        return ..string.pack(tstr);
      }
    }
    io.open();
    io.stdout.write("请输入密码：");
    var pwd = console.getPassword();
    import win;
    win.msgbox(pwd,"密码");
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

