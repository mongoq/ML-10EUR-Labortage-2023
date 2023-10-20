#!/usr/bin/python3

import socket

# Replace with your ESP32 IP address
ESP_IP = '192.168.4.1'
ESP_PORT = 2000

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to ESP32 server
try:
    s.connect((ESP_IP, ESP_PORT))
except OSError as e:
    print("Cannot connect to ESP32-CAM.")
    print("Make sure you are in the right Wifi.")
    print(e)
    exit()

print("\n--------------------")
print("\nContacting ESP32-CAM on IP: " + ESP_IP)
print("Using Port: " + str(ESP_PORT))
print("\nReceiving inferences ...")
print("\n--------------------\n")

while True:
    response = s.recv(1024)
    print(response.decode())

# Close the socket
s.close()
