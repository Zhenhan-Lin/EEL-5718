import socket
import argparse

def tcp_server(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"TCP Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        while True:
            try:
                data = client_socket.recv(512*3000)
                if not data:
                    break
                response_text = data.decode().strip()
                print(f"Received data: {response_text}")

                response = b"Server received: " + data
                client_socket.send(response)
            except Exception as e:
                print(f"Error: {e}")
                break

        print(f"Closing connection from {client_address}")
        client_socket.close()

# 设置命令行参数
parser = argparse.ArgumentParser(description='Send SCTP packets to a specified IP and port.')
parser.add_argument('server_ip', default='10.0.0.1', type=str, help='Destination IP address')
parser.add_argument('server_port', default='5201', type=int, help='Destination port number')
parser.add_argument('timeout_sec', default='5', type=float, help='Interval between packets in seconds')

# 解析命令行参数
args = parser.parse_args()

tcp_server(args.server_ip, args.server_port)
