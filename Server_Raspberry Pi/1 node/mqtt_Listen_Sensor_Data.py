#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import paho.mqtt.client as mqtt
from Feedback import sensor_Data_Handler
#from mqtt_Publish_Dummy_Data import publish_reference_Sensor_Values_to_MQTT

# MQTT Settings 
MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Sensor/#"
#MQTT_Topic_Humidity = "Reference/Sensor/PV_1"
#MQTT_Topic_Temperature = "Reference/Home/BedRoom/DHT22/Temperature"

#Subscribe to all Sensors at Base Topic
def on_connect(self, mosq, obj, rc):
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	data = 0
	print ("MQTT Data Received...")
	print ("MQTT Topic: " + msg.topic) 
	print ("Data: " + str(msg.payload))
	sensor_Data_Handler(msg.topic, msg.payload)
	

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))


# Publish reference data

#publish_reference_Sensor_Values_to_MQTT()

# Continue the network loop
mqttc.loop_forever()
