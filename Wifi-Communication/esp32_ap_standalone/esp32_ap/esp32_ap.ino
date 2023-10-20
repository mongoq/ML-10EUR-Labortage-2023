#include <WiFi.h>

const char* ssid = "ESP32-AP";
const char* password = "1234";

WiFiServer server(2000);

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);

  Serial.println("Access Point started.");
  Serial.print("SSID: ");
  Serial.println(ssid);

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Connection ...");
    while (client.connected()) {
      String message = "Hello from ESP32 AP!";
      client.print(message);
      Serial.println("Message sent: " + message);
      delay(1000); 
    }
    client.stop();
    Serial.println("Connection closed.");
  }
}
