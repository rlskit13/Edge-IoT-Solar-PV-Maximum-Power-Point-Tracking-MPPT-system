#include <TimeLib.h>
#include <Debug.h>
#include <JSN270.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include "Ultrasonic.h"


//#define SSID      "tweety"		// your wifi network SSID
//#define KEY       "phangseeheng"		// your wifi network password
#define SSID      "V20_0213"    // your wifi network SSID
#define KEY       "kit12345"    // your wifi network password
#define AUTH       "WPA2" 		// your wifi network security (NONE, WEP, WPA, WPA2)

#define USE_DHCP_IP 1

#if !USE_DHCP_IP
#define MY_IP          "localhost"
#define SUBNET         "255.255.255.0"
#define GATEWAY        "192.168.43.1"
#endif

#define HOST_IP        "192.168.43.38"
#define REMOTE_PORT    1883
#define ID       "admin"			// id should not be null
#define PW       "admin"			// pw should not be null
#define SUB_TOPIC	"ultrasonic"
#define PUB_TOPIC	"ultrasonic"
#define MESSAGE "JSN270"		// no space allowed
//Define pins ultrasonic(trig,echo)
//Ultrasonic ultrasonic(A0,A1); 
const int trigPin = 10;
const int echoPin = 9;
long duration;
int distance;

SoftwareSerial mySerial(3, 2); // RX, TX
 
JSN270 JSN270(&mySerial);
void setup() {
	char c;
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  mySerial.begin(9600);
	Serial.begin(9600);

	Serial.println("--------- JSN270 MQTT Client Test --------");

	// wait for initilization of JSN270
	delay(5000);
	//JSN270.reset();
	delay(1000);

	//JSN270.prompt();
	JSN270.sendCommand("at+ver\r");		// mqtt test require jsn270 s2w ver 1.3.0 or above
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);

#if USE_DHCP_IP
	JSN270.dynamicIP();
#else
	JSN270.staticIP(MY_IP, SUBNET, GATEWAY);
#endif    
    
	if (JSN270.join(SSID, KEY, AUTH)) {
		Serial.println("WiFi connect to " SSID);
	}
	else {
		Serial.println("Failed WiFi connect to " SSID);
		Serial.println("Restart System");

		return;
	}
	delay(1000);

	JSN270.sendCommand("at+wstat\r");
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);        

	JSN270.sendCommand("at+nstat\r");
	delay(5);
	while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
		Serial.print((char)c);
	}
	delay(1000);

	JSN270.mqtt_set(HOST_IP, REMOTE_PORT, ID, PW, SUB_TOPIC, PUB_TOPIC);
	delay(1000);

	// subscribe topic
	JSN270.mqtt_sub();
	delay(1000);
	
}
// Variables
float temperature;
float pressure;
String timestamp;
time_t start_time;
uint32_t t_ms;
uint32_t start_mills;
String run_mills;
int milis_chars;
String data;



void loop() {
  
	char c;
  //print subscribed message
	if (JSN270.available()) {
		while(JSN270.receive((uint8_t *)&c, 1, 10) > 0) {
			Serial.print((char)c);
		}
	}
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  //distance = ultrasonic.Ranging(CM); //Use 'CM' for centimeters or 'INC' for inches
  //Print distance...
  Serial.print("Object found at: ");
  Serial.print(distance);
  Serial.println("cm");
  //every 1sec. 
  
  //run_mills = String(millis());
  //milis_chars = run_mills.length();
  //timestamp = String(year()) + "/" + String(month())+"/" + String(day()) + "__" + String(hour()) + ":" + String(minute()) + ":" + String(second());
  //Serial.println(timestamp);
  
  data = String(distance);
  const char *data_complete = data.c_str();
	// publish message
	JSN270.mqtt_pub(data_complete);
  //temperature = temperature + 1;
  //pressure = pressure + 10;
	//delay(10);

}
