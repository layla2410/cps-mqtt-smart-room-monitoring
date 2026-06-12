import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

# Wildcard '+' menggantikan satu level topik
# Akan menerima dari home/room1/temperature DAN home/room2/temperature
TOPIC = "home/+/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(TOPIC, qos=0)
    print(f"Subscribed to: {TOPIC} (wildcard +)")

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} | Topic: {msg.topic} | QoS: {msg.qos}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print("Subscriber Wildcard '+' running... (Ctrl+C to stop)")
client.loop_forever()
