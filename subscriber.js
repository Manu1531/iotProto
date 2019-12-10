var mqtt = require('mqtt')
var client= mqtt.connect('mqtt://192.168.75.127')
client.on('connect',function(){

client.subscribe('presence')
client.publish('presence','hello mqtt')
})

client.on('message',function(topic,message){
    console.log(message.toString())
    client.end()
})