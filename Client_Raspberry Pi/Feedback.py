#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------


import json
#import sqlite3

# SQLite DB Name
#DB_Name =  "IoT.db"

#===============================================================
# Database Manager Class

#class DatabaseManager():
#	def __init__(self):
#		self.conn = sqlite3.connect(DB_Name)
#		self.conn.execute('pragma foreign_keys = on')
#		self.conn.commit()
#		self.cur = self.conn.cursor()
		
#	def add_del_update_db_record(self, sql_query, args=()):
#		self.cur.execute(sql_query, args)
#		self.conn.commit()
#		return

#	def __del__(self):
#		self.cur.close()
#		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def PV_1_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Voltage = json_Dict['Voltage']
	Current = json_Dict['Current']
	print ("Publishing PV 1 fake Voltage, Current, Power Value: " + str(Voltage) + ", " + str(Current) +  "...")
    

	#Push into DB Table
	#dbObj = DatabaseManager()
	#dbObj.add_del_update_db_record("insert into DHT22_Temperature_Data (SensorID, Date_n_Time, Temperature) values (?,?,?)",[SensorID, Data_and_Time, Temperature])
	#del dbObj
	#print ("Inserted Temperature Data into Database.")
	#print ("")

# Function to save Humidity to DB Table
def PV_2_Data_Handler(jsonData):
	#Parse Data 
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Voltage = json_Dict['Voltage']
	Current = json_Dict['Current']
	print ("Publishing PV 1 fake Voltage, Current, Power Value: " + str(Voltage) + ", " + str(Current) +  "...")
	#Push into DB Table
	#dbObj = DatabaseManager()
	#dbObj.add_del_update_db_record("insert into DHT22_Humidity_Data (SensorID, Date_n_Time, Humidity) values (?,?,?)",[SensorID, Data_and_Time, Humidity])
	#del dbObj
	#print ("Inserted Humidity Data into Database.")
	#print ("")


#===============================================================
# Master Function to Select DB Funtion based on MQTT Topic

def sensor_Data_Handler(Topic, jsonData):
	if Topic == "Reference/Sensor/PV_1":
		PV_1_Data_Handler(jsonData)
	elif Topic == "Reference/Sensor/PV_2":
		PV_2_Data_Handler(jsonData)	

#===============================================================
