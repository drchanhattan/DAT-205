import serial, mosquitto

client = mosquitto.Mosquitto("DAT205")
client.connect("127.0.0.1")

client.subscribe("Lights")

ser = serial.Serial("/dev/cu.usbmodem1421",9600,timeout=2)

def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)

    if msg.payload == "ON":
    
        ser.write("1")
    
    if msg.payload == "OFF":
    
        ser.write("0")

client.on_message = messageReceived

while (client != None): client.loop()
