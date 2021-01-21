#include <TimeLib.h>
#include <Debug.h>
#include <JSN270.h>
#include <Arduino.h>
#include <SoftwareSerial.h>

#define SSID      "tweety"		// your wifi network SSID
#define KEY       "phangseeheng"		// your wifi network password
#define AUTH       "WPA2" 		// your wifi network security (NONE, WEP, WPA, WPA2)

#define USE_DHCP_IP 1

#if !USE_DHCP_IP
#define MY_IP          "192.168.0.99"
#define SUBNET         "255.255.255.0"
#define GATEWAY        "192.168.0.1"
#endif

#define HOST_IP        "192.168.0.106"
#define REMOTE_PORT    1883
#define ID       "admin"			// id should not be null
#define PW       "admin"			// pw should not be null
#define SUB_TOPIC	"/jsn270"
#define PUB_TOPIC	"/jsn270"

#define MESSAGE ""		// no space allowed

SoftwareSerial mySerial(3, 2); // RX, TX
 
JSN270 JSN270(&mySerial);

void setup() {
	char c;

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
  // print subscribed message
	if (JSN270.available()) {
		while(JSN270.receive((uint8_t *)&c, 1, 1000) > 0) {
			Serial.print((char)c);
		}
	}
  run_mills = String(millis());
  milis_chars = run_mills.length();
  timestamp = String(now()) + run_mills.charAt(milis_chars-3) + run_mills.charAt(milis_chars-2) + run_mills.charAt(milis_chars-1);
  data = timestamp +"/"+ String(temperature) + "/" + String(pressure);
  const char *data_complete = data.c_str();
	// publish message
	JSN270.mqtt_pub(data_complete);
  temperature = temperature + 1;
  pressure = pressure + 10;

	delay(1000);

}
