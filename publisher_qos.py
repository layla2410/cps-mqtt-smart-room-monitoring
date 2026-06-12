import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "home/room1/temperature"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

print("Publisher QoS running... (Ctrl+C to stop)")

try:
    while True:
        for qos in [0, 1, 2]:
            suhu = round(random.uniform(24.0, 32.0), 2)
            client.publish(TOPIC, str(suhu), qos=qos)
            print(f"Published: {suhu} to topic {TOPIC} with QoS {qos}")
            time.sleep(2)
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
