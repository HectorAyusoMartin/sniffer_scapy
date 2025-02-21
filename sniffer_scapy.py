from scapy.all import sniff , PcapReader, wrpcap


class SnifferScapy:
    
    def __init__(self):
        self.captured_packets = []
        
        
    def start_capture(self, interface='any', filter=''):
        """Inicia la captura de paquetes"""
        
        print('[+]Captura de paquetes iniciada. Pulsa Ctrl + C para detener el proceso.')
        
        try:
            
            self.captured_packets = sniff(
                iface = interface,
                #timeout=10,
                filter = filter,
                prn = lambda x: x.summary(),
                store = True
            )
        
        except KeyboardInterrupt:
            print(f'Captura finalizada. El número de paquetes capturados es {len(self.captured_packets)}')
            
    def read_capture(self, pcapfile, filters=''):
        """Le un archivo cpap y lo carga en la [lista]"""
        
        try:
            self.captured_packets = [pkt for pkt in PcapReader(pcapfile)]
            #La forma equivalente de hacer esto de forma "normal", sin hacer uso de compresión de listas es:
            
            #self.captured_packets = []
            #for pkt in PcapReader(pcapfile):
                #self.captured_packets.append(pkt)
                
            print(f'Lectura del fichero pcap {pcapfile} realizada correctamente')
        
        except Exception as e:
            print(f'Error al leer el paquete de captura PCAP {pcapfile}. Error: {e}')
        
    def filter_by_protocol(self, protocol):
        """Filtra los paaquetes por protocolo en la [lista] contenedora de paquetes"""
        
        filtered_packets = [pkt for pkt in self.captured_packets if pkt.haslayer(protocol)]
        return filtered_packets
    
    def filter_by_text(self,text=''):
        """Filta por un texto determinado"""
        filtered_packets = []
        for pkt in self.captured_packets:
            found = False
            layer = pkt
            while layer:
                for field in layer.fields_desc:
                    field_name = field.name
                    field_value = layer.getfieldval(field_name)
                    if text in field_name or text in field_value:
                        filtered_packets.append(pkt)
                        found = True
                        break
                if found:
                    break
                layer = layer.payload
                
        return filtered_packets
    
    def print_packets_details(self, packets=None):
        """Mostrar paquetes por pantalla"""
        if packets is None:
            packets = self.captured_packets
        
        for packet in packets:
            packet.show
            print('---'*20)
            
    def export_to_pcap(self, packets, filename='capture.pcap'):
        """ Exportar la [lista de paquetes] a un archivo .pcap""" 
        
        wrpcap(filename, packets)
        print('Paquetes guardados en disco satisfactoriamente')
        
        
        
             
            
        
                
                      
                    
        
                       
    