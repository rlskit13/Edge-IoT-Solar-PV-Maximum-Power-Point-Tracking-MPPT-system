// This example uses an Arduino/Genuino Zero together with
// a WiFi101 Shield or a MKR1000 to connect to shiftr.io.
//
// IMPORTANT: This example uses the new WiFi101 library.
//
// You can check on your device after a successful
// connection here: https://shiftr.io/try.
//
// by Gilberto Conti
// https://github.com/256dpi/arduino-mqtt

#include <WiFi101.h>
#include <MQTT.h>

const char ssid[] = "0D289_MaxisBroadband";
const char pass[] = "67355040";

int V = 0;
int I = 0;
float V_SENSE = 0.0f;
float I_SENSE = 0.0f;
float V_PV = 0.0f;
float I_PV = 0.0f;
float V_Rin = 10000.0f;
float V_Rout = 100.0f;
float I_Rout = 100.0f;

int analogPin_v = 3;
int analogPin_i = 5;
int ref_volpin = 9;
long ref_vol;
String data;

WiFiClient net;
MQTTClient client;

unsigned long lastMillis = 0;

void connect() {
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.print("\nconnecting...");
  while (!client.connect("arduino", "try", "try")) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nconnected!");

  client.subscribe("Reference/Sensor/PV_MKR");
  // client.unsubscribe("/hello");
}
long stringToLong(String s)
{
   char arr[12];
   s.toCharArray(arr, sizeof(arr));
   return atol(arr);
}


void messageReceived(String &topic, String &payload) {
  Serial.println("incoming: " + topic + " - " + payload);
  ref_vol = stringToLong(payload);
  analogWrite(ref_volpin, ref_vol);
  //digitalWrite(7, HIGH);
  
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  pinMode(7, OUTPUT);
  // Note: Local domain names (e.g. "Computer.local" on OSX) are not supported by Arduino.
  // You need to set the IP address directly.
  client.begin("192.168.0.6", net);
  client.onMessage(messageReceived);

  connect();
}



void loop() {
  client.loop();

  if (!client.connected()) {
    connect();
  }

  // publish a message roughly every second.
  //if (millis() - lastMillis > 1000) {
  //  lastMillis = millis();
  //  voltage = voltage+1;
  //  current = current+1;
    V = analogRead(analogPin_v);
    I = analogRead(analogPin_i);
    V_SENSE = (float)V*5.0f/1023.0f;
    I_SENSE = (float)I*5.0f/1023.0f;
    V_PV = (float)(V_SENSE*V_Rin)/(2.50f*V_Rout);
    I_PV = (float)I_SENSE/(I_Rout*0.005);
    data = String(V_PV) + "/" + String(I_PV);
    client.publish("Sensor/PV_MKR", data);
    //digitalWrite(7, LOW);
    Serial.print(data); 
//    delay(500);

  //}

    Serial.print("\n");
}
