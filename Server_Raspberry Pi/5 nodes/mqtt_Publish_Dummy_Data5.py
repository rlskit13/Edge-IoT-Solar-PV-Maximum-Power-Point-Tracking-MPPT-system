#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import json
import paho.mqtt.client as mqtt
import random, threading, json
#from datetime import datetime

#====================================================
# MQTT Settings 
MQTT_Broker = "iot.eclipse.org"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_PV_1 = "Reference/Sensor/PV_1"
MQTT_Topic_PV_2 = "Reference/Sensor/PV_2"
MQTT_Topic_PV_3 = "Reference/Sensor/PV_3"
MQTT_Topic_PV_4 = "Reference/Sensor/PV_4"
MQTT_Topic_PV_5 = "Reference/Sensor/PV_5"
#MQTT_Topic = "Reference/Home/BedRoom/#"
#====================================================

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: ") + str(MQTT_Broker)

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print ("")


#====================================================
# FAKE SENSOR 
# Dummy code used as Fake Sensor to publish some random values
# to MQTT Broker

#toggle = 0

def publish_reference_Sensor_Values_to_MQTT(SensorID, Data1):
	#threading.Timer(3.0, publish_reference_Sensor_Values_to_MQTT).start()
	#global toggle
	if SensorID == "PV-1":
		#Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))
		Voltage_Fake_Value = "{0:.2f}".format(Data1)
		#Current_Fake_Value = "{0:.2f}".format(Data2)
		#Power = "{0:.2f}".format(Data3)
		PV_1_Data = {}
		PV_1_Data['Sensor_ID'] = "PV-1"
		#PV_1_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		PV_1_Data['Voltage'] = Voltage_Fake_Value
		#PV_1_Data['Current'] = Current_Fake_Value
		#PV_1_Data['Power'] = Power 
		PV_1_json_data = json.dumps(PV_1_Data)

		print ("Publishing PV 1 reference Voltage Value: " + str(Voltage_Fake_Value))
		publish_To_Topic (MQTT_Topic_PV_1, PV_1_json_data)


	elif SensorID == "PV-2":
		#Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
		Voltage_Fake_Value = "{0:.2f}".format(Data1)
		#Current_Fake_Value = "{0:.2f}".format(Data2)
		#Power = "{0:.2f}".format(Data3)
		PV_2_Data = {}
		PV_2_Data['Sensor_ID'] = "PV-2"
		#PV_2_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		PV_2_Data['Voltage'] = Voltage_Fake_Value
		#PV_2_Data['Current'] = Current_Fake_Value
		#PV_2_Data['Power'] = Power 
		PV_2_json_data = json.dumps(PV_2_Data)

		print ("Publishing PV 2 reference Voltage Value: " + str(Voltage_Fake_Value))
		publish_To_Topic (MQTT_Topic_PV_2, PV_2_json_data)

	elif SensorID == "PV-3":
		#Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
		Voltage_Fake_Value = "{0:.2f}".format(Data1)
		#Current_Fake_Value = "{0:.2f}".format(Data2)
		#Power = "{0:.2f}".format(Data3)
		PV_3_Data = {}
		PV_3_Data['Sensor_ID'] = "PV-3"
		#PV_3_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		PV_3_Data['Voltage'] = Voltage_Fake_Value
		#PV_3_Data['Current'] = Current_Fake_Value
		#PV_3_Data['Power'] = Power 
		PV_3_json_data = json.dumps(PV_3_Data)

		print ("Publishing PV 3 reference Voltage Value: " + str(Voltage_Fake_Value))
		publish_To_Topic (MQTT_Topic_PV_3, PV_3_json_data)

	elif SensorID == "PV-4":
		#Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
		Voltage_Fake_Value = "{0:.2f}".format(Data1)
		#Current_Fake_Value = "{0:.2f}".format(Data2)
		#Power = "{0:.2f}".format(Data3)
		PV_4_Data = {}
		PV_4_Data['Sensor_ID'] = "PV-4"
		#PV_4_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		PV_4_Data['Voltage'] = Voltage_Fake_Value
		#PV_4_Data['Current'] = Current_Fake_Value
		#PV_4_Data['Power'] = Power 
		PV_4_json_data = json.dumps(PV_4_Data)

		print ("Publishing PV 4 reference Voltage Value: " + str(Voltage_Fake_Value))
		publish_To_Topic (MQTT_Topic_PV_4, PV_4_json_data)

	elif SensorID == "PV-5":
		#Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(1, 30)))
		Voltage_Fake_Value = "{0:.2f}".format(Data1)
		#Current_Fake_Value = "{0:.2f}".format(Data2)
		#Power = "{0:.2f}".format(Data3)
		PV_5_Data = {}
		PV_5_Data['Sensor_ID'] = "PV-5"
		#PV_5_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S:%f")
		PV_5_Data['Voltage'] = Voltage_Fake_Value
		#PV_5_Data['Current'] = Current_Fake_Value
		#PV_5_Data['Power'] = Power 
		PV_5_json_data = json.dumps(PV_5_Data)

		print ("Publishing PV 5 reference Voltage Value: " + str(Voltage_Fake_Value))
		publish_To_Topic (MQTT_Topic_PV_5, PV_5_json_data)

	

#publish_reference_Sensor_Values_to_MQTT()

