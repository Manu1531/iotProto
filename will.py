import paho.mqtt.client as mqtt
#import os
def on_messsage(client,userdata,flags,rc):
    print("Connected")

client=mqtt.Client()
client.will_set("Manish","client disconnected",0,True) #topic qos,retain flag is given here
client.connect("192.168.75.127",1883,60)
   # client.publisher("Manish","disconnected")

client.on_messsage=on_messsage

client.loop_forever()