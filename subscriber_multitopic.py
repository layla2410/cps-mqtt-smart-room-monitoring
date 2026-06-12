import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

# Subscribe ke topik spesifik (bukan wildcard)
TOPICS = [
    ("home/room1/temperature", 0),
    ("home/room1/humidity", 0),
    ("home/room2/temperature", 0),
]

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    for topic, qos in TOPICS:
        client.subscribe(topic, qos=qos)
        print(f"Subscribed to: {topic} (QoS {qos})")

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} | Topic: {msg.topic} | QoS: {msg.qos}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print("Subscriber Multi-Topic running... (Ctrl+C to stop)")
client.loop_forever()
