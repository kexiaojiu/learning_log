# Learning Log
***

## 1 项目说明
本项目建立“Learning Log”(学习笔记)的Web应用程序，让你用户能耐记录感兴趣的主题，并在学习每个主题，并在学习每个主题的过程中添加日志条目。“Learning Log”的主页对这个网站进行描述，并邀请用户注册或登陆。用户登录后，就可以创建主题、添加新条目以及阅读既有的条目。

## 2 重要模块
### 2.1 用户账户
Web应用程序的核心是让任何用户都能够注册账户并能够使用它。该模块保护一些表单，让用户能够添加主题和条目，以及编辑现有的条目。  
然后，实现了一个用户身份验证的系统。   
### 2.2 样式及部署
使用django-bootstrap3,把项目部署到Heroku,这个网站能够讲项目推送到其服务器，让任何有网络链接的人都可以使用它
 
## 3备注
根据使用的环境选择具体的安装文件，这里以64位window10 python3.5为例.  
virtualenv		$pip install --user vitualenv  
Django          $pip install Django  
django-bootstrap3 $pip install django-bootstrap3

