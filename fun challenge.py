from scapy.all import *
import base64
import random
import time

# Function to send fragmented flag packets
def send_fragmented_flag():
    encoded_flag = base64.b64encode(b"THE_FLAG").decode()
    fragments = [encoded_flag[i:i+5] for i in range(0, len(encoded_flag), 5)]
    for frag in fragments:
        send(IP(dst="192.168.1.1") / ICMP() / frag)
        time.sleep(random.uniform(0.1, 1))

#////////////////////////////////BREAK///////////////////////////////////////////

# Function to generate noise with ICMP packets
def send_icmp_noise(count):
    for _ in range(count):
        ip = f"192.168.1.{random.randint(2, 254)}"
        send(IP(dst=ip)/ICMP()/("X" * random.randint(1, 50)))
        time.sleep(random.uniform(0.1, 1))

# Function to generate noise with other protocols
def send_noise(count):
    # arrays for distraction 
    urls = ["www.google.com", "www.yahoo.com", "www.bing.com"]
    domains = ["minecraft.com", "steam.com", "notsus.com"]
    
    for _ in range(count):
        # HTTP noise
        url = random.choice(urls)
        try:
            ip = socket.gethostbyname(url)
            send(IP(dst=ip)/TCP(dport=80, flags="S")/("X" * random.randint(1, 50)))
        except:
            pass
        
        # UDP noise
        ip = f"192.168.1.{random.randint(2, 254)}"
        payload = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 50)))
        send(IP(dst=ip)/UDP(dport=random.randint(1000,9999))/payload)

        # DNS noise
        domain = random.choice(domains)
        send(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain)))
        
        time.sleep(random.uniform(0.1, 1))

if __name__ == "__main__":
    send_icmp_noise(30)  
    send_noise(30) 
    send_fragmented_flag()
    send_icmp_noise(30)
    send_noise(30)
    send_fragmented_flag()
print("Packet's have finished sending through network")

