import socket
import cv2
import numpy as np
import pyautogui
import struct  # Import the struct module

# Create a socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.6.82", 9999))  # Replace with the server's IP address

while True:
    try:
        # Capture the screen
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        _, img_encoded = cv2.imencode('.jpg', frame, encode_param)
        frame_data = np.array(img_encoded).tobytes()

        # Send the screen capture to the server with a length header
        frame_length = len(frame_data)
        client_socket.sendall(struct.pack('>Q', frame_length))
        client_socket.sendall(frame_data)
    except Exception as e:
        print(f"Error: {e}")
        break

# Clean up
client_socket.close()