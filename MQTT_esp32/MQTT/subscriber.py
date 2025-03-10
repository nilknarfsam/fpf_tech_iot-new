import time
import ubinascii
from umqtt.simple import MQTTClient
import machine
import json  # Importar o módulo json

last_message = None
atuador = None
tempo = None

pino_13 = machine.Pin(13, machine.Pin.OUT)
pino_4 = machine.Pin(4, machine.Pin.OUT)
pino_12 = machine.Pin(14, machine.Pin.OUT)
pino_26 = machine.Pin(26, machine.Pin.OUT)

# Default MQTT broker to connect to
MQTT_BROKER = "10.31.0.178"
PORT = 1883
CLIENT_ID = ubinascii.hexlify(machine.unique_id())

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    global last_message
    global atuador
    global tempo
    # Decodificar a mensagem e convertê-la em um dicionário
    if type(msg.decode()) is str:
        last_message = msg.decode()
    else:

        last_message = json.loads(msg.decode())
        atuador = last_message["atuador"]
        tempo = last_message["tempo"]
    print(f"Mensagem recebida: {(topic, last_message)}")

def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()

def main():
    global last_message
    global atuador
    global tempo
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe("#")
    print(f"Connected to MQTT Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    
    while True:
        # Non-blocking wait for message
        mqttClient.check_msg()
        # Sleep to avoid 100% CPU usage (in a real app other useful actions would be performed instead)
        time.sleep(1)
        
        if last_message is not None:
            # Ação do atuador
            if atuador == 1:
                pino_13.value(1)
                time.sleep(tempo)
                pino_13.value(0)
            elif atuador == 2:
                pino_4.value(1)
                time.sleep(2)
                pino_4.value(0)
            elif atuador == 3:
                pino_12.value(1)
                time.sleep(tempo)
                pino_12.value(0)
            elif atuador == 4:
                pino_26.value(1)
                time.sleep(tempo)
                pino_26.value(0)
            last_message = None

    print("Disconnecting...")
    mqttClient.disconnect()

if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print("Error: " + str(e))
        reset()
