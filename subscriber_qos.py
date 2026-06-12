import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "home/room1/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(TOPIC, qos=2)
    print(f"Subscribed to topic: {TOPIC} with QoS 2")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} | Topic: {msg.topic} | QoS: {msg.qos}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print("Subscriber QoS running... (Ctrl+C to stop)")
client.loop_forever()
