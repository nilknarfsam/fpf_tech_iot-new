import time
import machine
from umqtt.simple import MQTTClient
import random

# Default MQTT server to connect to
SERVER = "10.31.0.178"
PORT = 1883
CLIENT_ID = "teste"
TOPIC = "temperature"
    

mqttClient = MQTTClient(CLIENT_ID, SERVER, PORT, keepalive=60)
mqttClient.connect()
print(f"Connected to MQTT  Broker :: {SERVER}")

while True:
    random_temp = random.randint(20, 50)
    print(f"Publishing temperature :: {random_temp}")
    mqttClient.publish(TOPIC, str(random_temp).encode())
    time.sleep(3)
mqttClient.disconnect()
    

