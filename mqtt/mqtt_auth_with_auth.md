
# mqtt_auth_with_auth


### 版本
`./bin/emqttd_ctl status #emqttd 2.3.3 is running`

### 配置
`cat etc/plugins/emq_auth_clientid.conf`

```
auth.client.1.clientid = my_id1
auth.client.1.password = my_passwd1
auth.client.1.clientid = my_id2
auth.client.1.password = my_passwd2
```

加载:`./bin/emqttd_ctl plugins load emq_auth_clientid`

Q: 怎么使用clientid

clientid与`username／password`是一起工作的？


使用username／password做实验，控制台websocket来调试

### [客户端连接](http://emqtt.com/clients#python)
`pip install `


```
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.subscribe("/test_sub1")

client.connect("127.0.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```


### 发布消息
npm install -g mqtt

```
mqtt pub -u 'wwj_u' -P 'wwj_p' -t '/test_sub1' -h '127.0.0.1' -p 1883 -m 'from mqtt.js'```

### payload json
```
#!/usr/bin/python
import json
import paho.mqtt.client as mqtt


send_msg = {
        'data_to_send': variable1,
        'also_send_this': variable2
}

client.publish("topic", payload=json.dumps(send_msg), qos=2, retain=False)
```

也可以传递python数据结构，不过eval有风险，可能被hack

### webhook
emq_web_hook
