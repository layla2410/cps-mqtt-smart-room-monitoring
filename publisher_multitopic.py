import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

print("Publisher Multi-Topic running... (Ctrl+C to stop)")

try:
    while True:
        suhu1 = round(random.uniform(24.0, 32.0), 2)
        hum1 = round(random.uniform(40.0, 70.0), 2)
        motion1 = random.choice(["DETECTED", "CLEAR"])

        suhu2 = round(random.uniform(24.0, 32.0), 2)
        hum2 = round(random.uniform(40.0, 70.0), 2)

        client.publish("home/room1/temperature", str(suhu1), qos=0)
        print(f"Published: {suhu1} to home/room1/temperature")

        client.publish("home/room1/humidity", str(hum1), qos=0)
        print(f"Published: {hum1} to home/room1/humidity")

        client.publish("home/room1/motion", motion1, qos=1)
        print(f"Published: {motion1} to home/room1/motion")

        client.publish("home/room2/temperature", str(suhu2), qos=0)
        print(f"Published: {suhu2} to home/room2/temperature")

        client.publish("home/room2/humidity", str(hum2), qos=0)
        print(f"Published: {hum2} to home/room2/humidity")

        print("---")
        time.sleep(3)
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
