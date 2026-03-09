# network/mqtt_client.py
# MQTT上传模块

class MQTTClient:
    def publish(self, topic, message):
        print(f"Publishing message to topic {topic}: {message}")