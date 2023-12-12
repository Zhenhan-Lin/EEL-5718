import socket
import time
import argparse
import csv

def send_tcp_packets(destination_ip, destination_port, interval_sec, num_packets, packet_size):
    startTime = time.time()
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #tcp_socket.connect((destination_ip, destination_port))
    tcp_socket.settimeout(10)  # Set socket timeout to 10 second

    sent_packets = 0
    received_packets = 0
    rtt_sum = 0
    total_data_sent = 0  # Track total data sent in bytes
    lost_data = 0
    
    try:
        tcp_socket.connect((destination_ip, destination_port))
    except socket.timeout:
        print("Connection Failure")
        return
    tcp_socket.settimeout(1)  # Set socket timeout to 1 second

    for i in range(num_packets):
        data = b"Packet " + str(i).encode() + b" " * (packet_size - len(b"Packet ") - len(str(i).encode()))
        start_time = time.time()
        total_data_sent += len(data)  # Count the data size
        tcp_socket.send(data)
        sent_packets += 1

        try:
            response = tcp_socket.recv(512*3000)
            
            received_packets += 1
            end_time = time.time()
            rtt = end_time - start_time
            rtt_sum += rtt
            response_text = response.decode().strip()
            # print(f"{rtt:.6f}")
            #print(f"Received response: {response_text}, RTT: {rtt:.6f}s")
            #print(f"Received response: {response.decode()}, RTT: {rtt:.6f}s")
        except socket.timeout:
            lost_data += len(data) 
            # print("None")
            #print(f"No response received for packet {i} within 1 second")

        time.sleep(interval_sec)

    tcp_socket.close()
    endTime = time.time()
    packet_loss_rate = 1 - (received_packets / sent_packets)
    avg_rtt = rtt_sum / received_packets if received_packets > 0 else 0
    transfered_bytes = total_data_sent - lost_data
    takeTime = endTime - startTime
    throughput = transfered_bytes / (endTime - startTime) * 8

    print(f"Packet Loss Rate: {packet_loss_rate:.2%}")
    print(f"Average RTT: {avg_rtt:.6f}s")
    print(f"Throughput: {throughput:.2f} bits/sec")
    print(f"Transfered Bytes: {transfered_bytes:.2f} bytes")
    print(f"Take Time:{takeTime}")

    return [interval_sec, num_packets, throughput, avg_rtt, packet_loss_rate, transfered_bytes]

# 设置命令行参数
parser = argparse.ArgumentParser(description='Send SCTP packets to a specified IP and port.')
parser.add_argument('destination_ip', default='10.0.0.1', type=str, help='Destination IP address')
parser.add_argument('destination_port', default='5201', type=int, help='Destination port number')
parser.add_argument('topology_name', default='tree', type=str, help='Number of used topology')
# parser.add_argument('exp_time', default='5', type=int, help='Run times')
# parser.add_argument('num_packets', default='500', type=int, help='Number of packets to send')


# 解析命令行参数
args = parser.parse_args()

# sctp 512k, udp 256k
# send_sctp_packets(args.destination_ip, args.destination_port, args.interval_sec, args.num_packets, args.packet_size)
msg_sizes = [2000, 4000, 8000, 16000, 32000, 64000, 128000]
intervals = [0.00001, 0.00005, 0.0001, 0.0005, 0.001]
exp_times = 3
num_packets = 500
filename = 'tcp_{}_result.csv'.format(args.topology_name)

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ['msg_size', 'exp_number', 'interval_sec', 'num_packets', 'throughput', 'latency_rtt', 'packet_loss',
         'transfered_bytes'])

    for msg_size in msg_sizes:
        for interval in intervals:
            for exp_number in range(1, exp_times + 1):
                result = send_tcp_packets(args.destination_ip, args.destination_port, interval, num_packets, msg_size)
                if result:
                    writer.writerow([msg_size, exp_number] + result)

print(f"Experiments completed. Results written to {filename}")