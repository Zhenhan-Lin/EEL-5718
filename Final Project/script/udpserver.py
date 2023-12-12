import socket
import argparse

def udp_server(server_ip, server_port, timeout_sec):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((server_ip, server_port))

    print(f"UDP Server listening on {server_ip}:{server_port}")

    #udp_socket.settimeout(timeout_sec)  # Set the socket timeout for receiving

    while True:
        try:
            data, client_address = udp_socket.recvfrom(512*3000)
            response = b"Server received: " + data
            print(f"Connection from {client_address}")
            #response_text = response.decode().strip()
            
            print(f"Received data: {response}")

            
            udp_socket.settimeout(timeout_sec)  # Set the socket timeout for receiving
            udp_socket.sendto(response, client_address)
        except socket.timeout:
            print("waiting......")
            continue
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    udp_socket.close()


# 设置命令行参数
parser = argparse.ArgumentParser(description='Send SCTP packets to a specified IP and port.')
parser.add_argument('server_ip', default='10.0.0.1', type=str, help='Destination IP address')
parser.add_argument('server_port', default='5201', type=int, help='Destination port number')
parser.add_argument('timeout_sec', default='5', type=float, help='Interval between packets in seconds')

# 解析命令行参数
args = parser.parse_args()

udp_server(args.server_ip, args.server_port, args.timeout_sec)
