import paho.mqtt.client as mqttclient
import time
import ssl
import logging

connected = False

broker_address = "kebnekaise.lmq.cloudamqp.com"
port = 8883
user = "xcilevvo:xcilevvo"
password = "E2UgHCgVov6HLcAHaTjQH3Y8AD6g8AjL"


def on_connect(client, userdata, flags, reason_code, properties):
    global connected

    if reason_code == 0:
        print("client is connected to broker")
        connected = True
    else:
        print("failed client connect:", reason_code)


logging.basicConfig(level=logging.DEBUG)

client = mqttclient.Client(
    mqttclient.CallbackAPIVersion.VERSION2,
    "MQTT"
)

client.username_pw_set(user, password)

client.tls_set(
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect

client.connect(broker_address, port)

client.loop_start()

while not connected:
    time.sleep(0.2)

result = client.publish("mqtt/firstcode", "hello MQTT2")

print("publish result:", result.rc)

client.loop_stop()
client.disconnect()
