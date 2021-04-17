**一. 分析需求**  

1. 需求说明 

在项目开发过程中,我们有时会频繁的更新代码, 流程大概为:

(1) 本地git push提交代码至git托管平台

(2) 登陆到部署有网站源码的线上服务器

(3) cd到项目根目录, 执行git pull 指令拉取最新代码

![](https://img.jbzj.com/file_images/article/202011/20201128154013711.jpg?20201028154051)

整个流程纯手动更新,每次耗时在1分钟左右, 这样一天下来,浪费了很多时间在这些琐碎的事情上.

现在的需求是,在每次本地提交代码后,线上服务器自动拉取最新代码,完成部署更新.即所谓的自动化部署.

2. 方案 

现在一些主流代码托管平台如github、 gitlab、git@osc
等均已提供webhook功能,在用户push了代码后，会自动回调一个您设定的http地址。
用户可以自己根据不同的需求，来编写自己的脚本程序（比如发邮件，自动部署等）；目前，webhook支持多种触发方式，如Push、 Tag Push、
Issue、评论、合并请求 等。

附webhook的简介:

Webhook就是用户通过自定义回调函数(callback)的方式来改变Web应用的一种行为，这些回调函数可以由不是该Web应用官方的第三方用户或者开发人员来维护，修改。通过Webhook，你可以自定义一些行为通知到指定的URL去。Webhook的“自定义回调函数”通常是由一些事件触发的，比如推送代码到代码库或者博客下新增一个评论，源站点会为Webhook进行HTTP请求的URI配置。用户通过配置，就可以使一个网站上的事件调用在另一个网站上表现出来，这些事件调用可以是任何事件，但通常应用的是系统集成和消息通知。

方案流程：

![](https://img.jbzj.com/file_images/article/202011/20201128154013712.png?20201028154058)

所以自动部署主要实现方式就是：

- 修改代码 push 

- github(其他仓库平台)发送请求给你的网站服务器 

- 网站服务器收到更新请求，执行自动部署脚本 

- 自动部署脚本执行代码拉取，打包，修改文件等动作完成网站的更新部署 

**二、具体实现**  

Github仓库设置  

在GitHub上需要更新的代码仓库添加webhooks, 在指定仓库→settings→webhooks  

![](https://img.jbzj.com/file_images/article/202011/20201128154013713.png?20201028154058)

编写GitHub推送回调  

python开启web服务（hook.py）

```python

    import hmac
    import os
    from flask import Flask, request, jsonify
    
    app = Flask(__name__)
    # github中webhooks的secret
    github_secret = 'xxxxxxxx'
    
    def encryption(data):
      key = github_secret.encode('utf-8')
      obj = hmac.new(key, msg=data, digestmod='sha1')
      return obj.hexdigest()
    
    @app.route('/hook', methods=['POST'])
    def post_data():
      """
      github加密是将post提交的data和WebHooks的secret通过hmac的sha1加密，放到HTTP headers的
      X-Hub-Signature参数中
      """
      post_data = request.data
      token = encryption(post_data)
      # 认证签名是否有效
      signature = request.headers.get('X-Hub-Signature', '').split('=')[-1]
      if signature != token:
        return "token认证无效", 401
      # 运行shell脚本，更新代码
      os.system('sh deploy.sh')
      return jsonify({"status": 200})
    
    if __name__ == '__main__':
      app.run(port=8989)
```

编写shell脚本（deploy.sh）

> cd "$(dirname "$0")"  
>  echo '--------Git pull------------'  
>  git pull  
>  echo '-----Already up-to-date------'  
>  echo '----- restart supervision-----'  
>  supervisorctl restart blog  
>  echo '----- reload nginx-----'  
>  nginx -s reload  
>

注意： 此次部署的hook.py 和deploy.sh都是在仓库的同一目录下

开启服务  

supervisor部署webhook  

```python

    [program:webhook]
    directory=/data/wwwroot/docs
    command=/home/dukenan/.envs/flask_py3/bin/python3 hook.py
    autostart=true
    autorestart=false
    startsecs=1
    ;使用root账户
    user=root
    stderr_logfile=/etc/supervisor/logs/webhooks/stderr.log 
    stdout_logfile=/etc/supervisor/logs/webhooks/stdout.log 
    redirect_stderr=true
    loginfo=info
```

部署NGINX的参考  

```python

    server {
      listen 80; 
      server_name 服务器IP; # 配置域名
      client_max_body_size 300M;
      location / { 
        proxy_pass http://127.0.0.1:8989; #转发本地8989端口
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }  
    }
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

