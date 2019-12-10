import paho.mqtt.client as mqtt

def on_messsage(client,userdata,flags,rc):
    print("Hello")

client=mqtt.Client()
client.connect("192.168.75.127",1883,60)


client.subscribe("data",1)
client.subscribe("Manish",1)


client.on_messsage=on_messsage

client.loop_forever()
