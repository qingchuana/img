---
title: Hexo+Github博客搭建教程（个人操作过程）
abbrlink: 7774
date: 2023-07-17 17:57:14
typora-root-url: ./..\..\..\..\typora img
---



# [Hexo](https://so.csdn.net/so/search?q=Hexo&spm=1001.2101.3001.7020)+Github博客搭建教程（个人操作过程）

最近自己尝试利用hexo+github搭建了blog，来记录一下过程

##一、准备环境

## 1、node环境

首先，安装 nodejs， 因为Hexo是基于 Node.js 驱动的一款博客框架。

**http://nodejs.cn** 

## 2、git 环境

然后，安装git, 一个分布式版本控制系统，用于项目的版本控制管理，作者是 Linux 之父。

⭐Git（官网）**https://git-scm.com/**

太慢的话可以自行找资源

    安装过程一路next就行（安装路径可改）
    
    两者安装完成之后，右击此电脑>属性>高级系统设置>环境变量>系统变量下的Path 可以看到两者已自动修改了环境变量，这是我们可以通过cmd命令（win+r后输入cmd）查看两者版本。(确认是否安装成功及可以使用) 查看Node.js版本命令：node -v 查看Git版本命令：git --version

## 3.之后进入GitHub创建一个仓库

> **确认注册后会让用户选择公有还是私有仓库(私有的个人仓库好像需要Money好像是每月7美金)**
> **个人博客的话直接选免费的就行了**
> **注意仓库的取名格式：用户名.github.io(这将是以后的访问域名)**
>
> 

![image-20230717133445506](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230717133445506.png)

> **到这里代表我们Github账号以及仓库都已经创建完毕**
> **可以把下面这段仓库的地址复制下来留着后面配置时会用到**

![image-20230716091944628](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716091944628.png)



## 4. 接下来进入本地配置安装Hexo

**在磁盘中创建一个用来存放Github本地仓库文件的目录(可自定义目录存放，顾名思义blog==博客)**

![image-20230716092108512](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092108512.png)



选中创建的目录(文件夹)右键选择使用Gti Bash Here打开Git命令窗口(这就是开始安装的Git工具，现在开始使用)
也可以使用Windows的cmd命令行(不推荐)
(因为是从国外服务器下载，受网络的影响比较大，有可能会出现异常，所以我们需要连接国内淘宝官方的服务器来进行)
输入命令：npm install -g cnpm --registry=https://registry.npm.taobao.org
注：之后再次使用命令则是以cnpm开头~而不是npm
![image-20230716092323573](https://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092323573.png)

> **正式开始安装hexo**
> **输入命令：cnpm install -g hexo-cli**

![image-20230716092359590](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092359590.png)

> **之后就是初始化Hexo**
> **输入命令：hexo init**

![image-20230716092518819](https://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092518819.png)



**这时我们创建的目录(文件夹)下已经多出许多文件**

![image-20230716092548657](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092548657.png)

新建完成后，指定文件夹Hexo目录下有：

    node_modules: 依赖包
    public：存放生成的页面
    scaffolds：生成文章的一些模板
    source：用来存放你的文章
    themes：主题**
    _config.yml: 博客的配置文件**

这样本地的网站配置也弄好啦，输入hexo g生成静态网页，然后输入hexo s打开本地服务器，

> **这时启动hexo之后在浏览器输入localhost:4000就可以在本地浏览博客(自带一篇Hello World博客)**
> **输入命令：hexo s**
> **关闭hexo ctrl + c**

![image-20230716092739503](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092739503.png)

![image-20230716092810228](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716092810228.png)

## 5. 设置ssh

> **生成sshkey**
> **输入命令：cd ~/.ssh进入.ssh文件**
>
> **输入命令：ssh-keygen -t rsa -C ‘注册时的邮箱地址’** 

![image-20230716093006803](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716093006803.png)

**此时我们去查看C盘目录(此文件夹所在C:\用户\用户名目录下)**

![image-20230716093119089](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716093119089.png)

**使用记事本打开id_rsa.put文件并复制生成的key**

**在已登陆的Github主页点击右侧头像 》 Settings设置**

再点击SSH and GPG keys 》 New SSH key

**将刚刚在.ssh目录下所复制id_rsa.pub文件中的信息复制进key(注意空格)，在给它取个名字(随意)**



> **这里需要在本地进行验证一次**
> **输入命令：ssh -T git@github.com 并且输入yes之后，行末尾会显示你的用户名**
>
> ![image-20230716093403459](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716093403459.png)

**绑定成功并且会邮箱收到邮件**

> **接着在本地绑定与Github的用户名和邮箱**
> **输入命令：git config --global user.name “注册时用户名”**
> **输入命令：git config --global user.email “注册时邮箱”**

![image-20230716093550811](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716093550811.png)



## 6. 上传测试博客

> 打开并修改本地仓库目录下_config.yml文件



> **在文件的末尾修改(repository属性的地址就是之前创建仓库后所保存的http地址)**
> deploy:
> type: git
> repository: https://github.com/用户名/用户名.github.io.git
>
> branch: master

> **此时需要安装一个上传工具**
> **输入命令：cnpm install hexo-deployer-git**

> **可以新建一篇测试文章(不新建的话也会有一篇自带的Hello World文章)**
> **输入命令：hexo new “文章名称”**



![image-20230716094542664](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716094542664.png)

> **新建文章之后需要生成一遍文件**
> **输入命令：hexo g**
>
> ![image-20230716094611137](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716094611137.png)
>
> 

> **新建文章后可在本地先预览一遍**
> **输入命令：hexo s浏览器输入：localhost:4000(ctrl + c 关闭)**

![在这里插入图片描述](http://raw.githubusercontent.com/qingchuana/img/main/img/20200331230142753.png)

![image-20230716094741275](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716094741275.png)

> **最后直接部署到Github就可以啦**
> **输入命令：hexo d**
>
> 

![image-20230716095642961](http://raw.githubusercontent.com/qingchuana/img/main/img/image-20230716095642961.png)

