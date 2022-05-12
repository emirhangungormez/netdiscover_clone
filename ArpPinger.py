import argparse
import scapy.all as scapy

class ARPPing():
	def __init__(self):
		print("ARPPing başlatıldı...")
		
	def kullanici_girdisini_al(self):
		parser = argparse.ArgumentParser()

		parser.add_argument('-i', '--ipadress', type=str, help="IP adresinizi girmelisiniz")
		args = parser.parse_args()

		if args.ipadress != None:
			return args
		else:
			print("bir ip adresini -i argümanı ile giriniz.")


	def arp_istegi(self,ip):
		
		arp_request_packet = scapy.ARP(pdst=ip)
		broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		combined_packet = broadcast_packet / arp_request_packet
		
		(answered_list, unanswered_list) = scapy.srp(combined_packet,timeout=1)
		answered_list.summary()
		
		#ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2)
		#scapy kütüphanesi kullanılmıştır.
		
if __name__ == "__main__":
	arp_ping = ARPPing()
	kullanici_girdisi = arp_ping.kullanici_girdisini_al()
	arp_ping.arp_istegi(kullanici_girdisi.ipadress)
		
		
		
