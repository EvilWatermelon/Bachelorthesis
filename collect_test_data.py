import paho.mqtt.client as mqttClient
import time
import sys

sensors = [0, 0, 0, 0, 0, 0, 0, 0]
pubMsg = ""

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

def on_message(client, userdata, message):

    if message.topic == "fsr1":
        print("Message received 1: "  + message.payload.decode("utf-8"))
        sensors[0] = message.payload.decode("utf-8")

    if message.topic == "fsr2":
        print("Message received 2: "  + message.payload.decode("utf-8"))
        sensors[1] = message.payload.decode("utf-8")

    if message.topic == "dis":
        print("Message received 3: "  + message.payload.decode("utf-8"))
        sensors[2] = message.payload.decode("utf-8")

    if message.topic == "fsr3":
        print("Message received 4: "  + message.payload.decode("utf-8"))
        sensors[3] = message.payload.decode("utf-8")

    if message.topic == "dist2":
        print("Message received 5: "  + message.payload.decode("utf-8"))
        sensors[4] = message.payload.decode("utf-8")

    if message.topic == "fsr4":
        print("Message received 6: "  + message.payload.decode("utf-8"))
        sensors[5] = message.payload.decode("utf-8")

    if message.topic == "fsr5":
        print("Message received 7: "  + message.payload.decode("utf-8"))
        sensors[6] = message.payload.decode("utf-8")

    if message.topic == "dist3":
        print("Message received 8: "  + message.payload.decode("utf-8"))
        sensors[7] = message.payload.decode("utf-8")

    print(sensors)
    file2write=open("probanden.txt",'a')
    file2write.write(str(sensors) + "\n")
    file2write.close()

def on_publish(client, userdata, result):
    print("Data published \n")
    pass

Connected = False

broker_adress = "MQTT-Broker IP Adress"
port=1883

client = mqttClient.Client("mosq/E4hpAcdlgjIy5b74cE")
client.on_connect= on_connect
client.on_message= on_message

client.connect(broker_adress, port=port)  #connect to broker
client.loop_start()#start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

client.subscribe("fsr1")
client.subscribe("fsr2")
client.subscribe("fsr3")
client.subscribe("fsr4")
client.subscribe("fsr5")
client.subscribe("dis")
client.subscribe("dist2")
client.subscribe("dist3")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

client1 = mqttClient.Client("controller1")
client1.on_publish = on_publish
client1.connect(broker_adress, port=port)
ret = client.publish("living_room", pubMsg)
