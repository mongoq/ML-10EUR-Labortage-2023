#include <WiFi.h>

//Change the wifi credentials
const char* ssid = "esp32-wrt54g";
const char* pass = "esp32-cam";

WiFiServer server(2000);

void setup() {

  Serial.begin(115200);
  delay(10);
  WiFi.begin(ssid, pass);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wifi...");
  }

  server.begin();
  Serial.println("Server started.");
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New connection ...");
    while (client.connected()) {
      String message = "Hello from ESP32 on WRT54G!";
      client.print(message);
      Serial.println("Message sent: " + message);
      delay(1000); 
    }
    client.stop();
    Serial.println("Connection closed.");
  }
}
