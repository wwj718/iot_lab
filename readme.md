# iot lab

# mqtt相关的需求
*  订阅topic, todo:具体topic
*  消息确认(QoS)
*  消息保留(log)
*  要求认证(clientid/pass)
    *  方案(EMQ)
        *  [MQTT 认证设置](http://emqtt.com/docs/v2/guide.html#user-guide)
        *  系统默认开启匿名认证(etc/emq.conf 配置启用匿名认证)
        *  使用`etc/plugins/emq_auth_clientid.conf`
*  websocket
*  安装server
    *  方案 EMQ
*  cli工具
    *  方案
        *  npm install -g mqtt(mqtt.js)
        *  mosquitto_sub
*  http发布消息
    *  方案:[HTTP 发布接口](http://emqtt.com/docs/v2/guide.html#http-publish)
*  websocket连接
    *  方案:[MQTT WebSocket 连接](http://emqtt.com/docs/v2/guide.html#mqtt-websocket)

# 参考
*  [MQTT协议中文版](https://www.gitbook.com/book/mcxiaoke/mqtt-cn)
*  [mqtt 基础](http://yanbin.is-programmer.com/posts/82950.html)
*  [EMQ - 百万级开源MQTT消息服务器](http://emqtt.com/docs/v2/index.html)
*  [Paho Python Client 学习笔记](http://shaocheng.li/post/blog/2017-05-23)

