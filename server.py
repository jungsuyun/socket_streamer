import socket
import cv2
import pickle
import struct

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = '192.168.0.24'

    print("HOST IP : ", host_ip)
    port = 5050
    socket_address = (host_ip, port)

    server_socket.bind(socket_address)

    server_socket.listen(5)
    print("Listening at : ", socket_address)

    while True:
        client_socket, addr = server_socket.accept()
        print("Got Connection From: ", addr)

        if client_socket:
            vid = cv2.VideoCapture(0)
            while vid.isOpened():
                img, frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)
                if cv2.waitKey(1) == ord('q'):
                    client_socket.close()
                    break