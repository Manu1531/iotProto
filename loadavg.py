import paho.mqtt.client as mqtt
import os
def on_messsage(client,userdata,flags,rc):
    print("Hello")
load1,load2,load3=os.getloadavg()
client=mqtt.Client()
client.connect("192.168.75.127",1883,60)


#client.subscribe("data",1)

client.publish('pc/load/1mavg',load1)
client.publish('pc/load/5mavg',load2)
client.publish('pc/load/10mavg',load3)


client.on_messsage=on_messsage

client.loop_forever()