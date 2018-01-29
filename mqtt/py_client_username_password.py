import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("/test_sub1") #在这里订阅

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # msg.payload 传递字符串 json
    print(msg.topic+" "+str(msg.payload))


# Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client(client_id="my_cli1") #加上client_id后服务台好管理
client.username_pw_set(username="wwj_u",password="wwj_p")
client.on_connect = on_connect
client.on_message = on_message


client.connect("127.0.0.1", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
