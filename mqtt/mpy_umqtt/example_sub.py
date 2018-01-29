import time
from umqtt.simple import MQTTClient

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    # 都是bytes
    print((topic, msg))

def main(server="mqtt.just4fun.site"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(sub_cb)
    c.connect()
    #c.subscribe(b"/test_umqtt")
    c.subscribe(b"/test_umqtt",qos=1)
    while True:
        if True:
            # Blocking wait for message
            print("running...")
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()
