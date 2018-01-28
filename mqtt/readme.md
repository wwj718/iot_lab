# readme
学习使用mqtt

# mqtt.js

### Browser
cdn: https://unpkg.com/mqtt/dist/mqtt.min.js


# Command Line Tools
```
mqtt pub -t 'mqtt/wwj_demo' -h 'q.emqtt.com' -m 'from MQTT.js'

mqtt sub -t 'mqtt/wwj_demo' -h 'q.emqtt.com' -v
```

# Q
*  test.mosquitto.org不支持websocket 握手错误
*  broker.hivemq.com 无法用`mqtt pub`给websocket发送pub
*  q.emqtt.com 可以从websocket发往websocket和`mqtt sub`,但不能从`mqtt pub`发往websocket，是端口问题？