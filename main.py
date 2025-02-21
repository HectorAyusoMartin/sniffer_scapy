from sniffer_scapy import SnifferScapy

if __name__ == "__main__":
    
    sniffer = SnifferScapy()
    
    sniffer.start_capture()
    
    sniffer.print_packets_details()


