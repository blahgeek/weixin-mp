# 微信公众平台+Django

详见[官方wiki](http://mp.weixin.qq.com/wiki/index.php)

## How to run

- 在mp.weixin.qq.com申请公众账号，使用“开发模式”，配置`Token`，在`settings.py`中填入自己的`Token`
- 配置服务器地址，`python2 ./manage.py runserver`运行

## Plugins

- 在`plugins`添加文件，参见`sample.py`。
- 在`plugins/__init__.py`的`__all__`中加入添加的插件文件名
