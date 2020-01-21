/**
 * @author: Jan Schröder
 * @purpose: publish sensor data via mqtt 
 * @last_date: 22.10.2019
 */

#include "WiFi.h" // Enables the ESP8266 to connect to the local network (via WiFi)
#include <PubSubClient.h>

const int pin32 = 32;

const int trigPin = 2;
const int echoPin = 27;

int forceReading32;

long duration;
int distance;

const char* ssid = "AndroidAP3D04";
const char* pw = "cwhb2400";

const char* mqtt_server = "192.168.43.47";
const char* sensor_name = "fsr_ult_1";
char readerS1[25];
char readerS2[25];

WiFiClient espClient;
PubSubClient client(espClient);

String msgS1 = "";
String msgS2 = "";

void setup_wifi(){
    delay(100);
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, pw);
    while (WiFi.status() != WL_CONNECTED)
    {
      delay(500);
      Serial.println("Connecting to WiFi..");
    }

    Serial.println("Connected to the WiFi network");      
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
 
    if (client.connect(sensor_name)){
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 6 seconds");
      // Wait 6 seconds before retrying
      delay(6000);
    }
  }
}
void setup() {

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  

}

void loop(){

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034/2;
  
  forceReading32 = analogRead(pin32);

  Serial.print("Data32 = ");
  Serial.println(forceReading32);

  Serial.print("DataDistance = ");
  Serial.println(distance); 

  msgS1 = forceReading32;
  msgS2 = distance;
  
  msgS1.toCharArray(readerS1, 25);
  msgS2.toCharArray(readerS2, 25);
    
  client.publish("fsr3", readerS1);
  client.publish("dist2", readerS2);
  delay(1500);
}
