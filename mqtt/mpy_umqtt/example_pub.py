from umqtt.simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

def main(server="mqtt.just4fun.site"):
    c = MQTTClient("umqtt_client_pub", server)
    c.connect()
    # c.publish(b"/test_umqtt", b"hello") #qos=1
    c.publish(b"/test_umqtt", b"hello",qos=1,retain=True)
    c.disconnect()

if __name__ == "__main__":
    main()
