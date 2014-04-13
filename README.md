# 微信公众平台+Django

详见[官方wiki](http://mp.weixin.qq.com/wiki/index.php)

## How to run

- 在mp.weixin.qq.com申请公众账号，使用“开发模式”，配置`Token`，在`settings.py`中填入自己的`Token`
- 配置服务器地址，`python2 ./manage.py runserver`运行

## 其他功能

在`plugins`添加文件即可实现其他功能，参见`sample.py`。
