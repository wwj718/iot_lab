# 生产环境安装EMQ
mqtt.just4fun.site : 47.52.104.107

参考:[DEB 包安装](http://emqtt.com/docs/v2/install.html#deb)

```
wget http://emqtt.com/downloads/latest/ubuntu16_04-deb
sudo dpkg -i ./ubuntu16_04-deb
sudo apt-get install lksctp-tools
```

### 使用

```
配置文件
EMQ 配置文件: /etc/emqttd/emq.conf，插件配置文件: /etc/emqttd/plugins/*.conf。

日志文件
日志文件目录: /var/log/emqttd

数据文件
数据文件目录：/var/lib/emqttd/

启动停止
sudo service emqttd start|stop|restart

# curl 127.0.0.1:18083
```






### nginx conf

```
```

### 端口开放
1883、8083、18083

### 测试
ws://mqtt.just4fun.site:8083/mqtt //ok

使用`http://mitsuruog.github.io/what-mqtt/`测试

允许匿名