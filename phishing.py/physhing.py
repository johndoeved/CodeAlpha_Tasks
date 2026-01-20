from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_analyzer(packet):
    print("=" * 60)

    # Check if packet has IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

        # TCP Protocol
        if TCP in packet:
            tcp_layer = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")

        # UDP Protocol
        elif UDP in packet:
            udp_layer = packet[UDP]
            print("Protocol       : UDP")
            print(f"Source Port    : {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        # Payload
        payload = bytes(packet[IP].payload)
        if payload:
            print(f"Payload        : {payload[:50]}")
        else:
            print("Payload        : None")

    else:
        print("Non-IP Packet Captured")

# Start sniffing with exception handling
try:
    print("Starting Packet Sniffer... Press Ctrl+C to stop.")
    sniff(prn=packet_analyzer, count=20)

except PermissionError:
    print("Error: Run this program as Administrator or use sudo.")

except KeyboardInterrupt:
    print("\nSniffing stopped by user.")

except Exception as e:
    print("Unexpected error:", e)
