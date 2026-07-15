import paho.mqtt.client as mqttclient
import ssl
import time
import logging

broker_address = "kebnekaise.lmq.cloudamqp.com"
port = 8883
user = "xcilevvo:xcilevvo"
password = "E2UgHCgVov6HLcAHaTjQH3Y8AD6g8AjL"

topic = "mqtt/secondcode"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)
        print("Subscribed to:", topic)
    else:
        print("Connection failed:", reason_code)


def on_message(client, userdata, msg):
    print("Message received")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())


logging.basicConfig(level=logging.DEBUG)

client = mqttclient.Client(
    mqttclient.CallbackAPIVersion.VERSION2,
    "MQTT-Subscriber"
)

client.username_pw_set(user, password)

client.tls_set(
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port)

# Keeps network loop running and waits for messages
client.loop_forever()
