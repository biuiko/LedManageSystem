# LED管理系统
基于Dajngo开发/软件项目实训

## 网站管理员：
- [x] 增加用户
- [x] 修改用户信息
- [x] 查看用户信息
- [x] 查看每个用户所拥有的LED信息
- [x] 对用户的视频和图片进行管理

## 用户
- [x] 登录（不允许用户自行注册）
- [x] 增加LED显示屏
- [x] 删除LED 
- [x] 上传图片和视频
- [x] 查看LED内容
- [ ] 设置LED端播放模式（单集循环、列表循环等）
- [x] 查看LED状态
- [x] 管理视频和图片信息

## 网址访问
[用户登录地址](http://139.9.236.103/led/)

[管理员登录地址](http://139.9.236.103/admin/)

直接访问视频播放界面：http://139.9.236.103/led/video/[用户id]/[LEDid]

直接访问图片播放界面：http://139.9.236.103/led/picture/[用户id]/[LEDid]

## 目录结构

├─led

│  │  admin.py          管理员所要管理和可以查看到的内容

│  │  apps.py           为项目注册一个应用(LED应用)

│  │  models.py     自己定义的数据库中的表结构

│  │  tests.py          测试

│  │  urls.py           为每一个事件注册一个URL

│  │  views.py          逻辑层代码

│  │  __init__.py       代表这是一个包

│  ├─migrations     数据库迁移目录包含数次建库建表操作以及对表的修改操作

│  ├─static         前端用到的各种静态文件包括css,js等

│  └─templates

│      │  base.html 模板界面

│      └─led

│              index.html           开始界面

│              LedMessage.html      LED管理页面

│              manage_pic.html      LED图片管理页面

│              manage_video.html    LED视频管理页面

│              show_led.html        LED图片展示页面

│              show_video_led.html  LED视频展示页面

└─led_system

        settings.py         配置文件

        urls.py             为应用等注册URL

        wsgi.py             部署时用到的文件

        __init__.py         代表这是一个包




## 杂七杂八
- 基于Django开发
- 使用网页来模拟LED端
- 默认图片随机播放，视频循环播放
