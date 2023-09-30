import socket
import cv2
import numpy as np
import struct  # Import the struct module

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.6.81", 9999))
server_socket.listen(0)
print("Server listening on port 9999...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

while True:
    try:
        # Read the 8-byte length header
        length_header = client_socket.recv(8)
        if not length_header:
            break

        # Unpack the length header to get the frame length as an integer
        frame_length = struct.unpack('>Q', length_header)[0]

        # Receive the screen capture data
        frame_data = b''
        while len(frame_data) < frame_length:
            frame_data += client_socket.recv(frame_length - len(frame_data))

        # Convert frame data to image
        frame = np.frombuffer(frame_data, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Display the received frame
        cv2.imshow("Received Screen", frame)
        cv2.waitKey(1)  # Adjust frame display time as needed
    except Exception as e:
        print(f"Error: {e}")
        break

# Clean up
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()