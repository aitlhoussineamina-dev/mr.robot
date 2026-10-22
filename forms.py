import pyfiglet
logo = pyfiglet.figlet_format("cyber tool")
print(logo)

import datetime
from datetime import datetime

import rich
from rich import print

import requests


print("              1.[italic red]ip adress of the server        [/]5.[italic red]general information of the")
print("              2.[italic red]web server status_code         [/]6.[italic red]ip location finder             ")
print("              3.[italic red]paths scaning                  [/]7.[italic red]base64 decode ")
print("              4.[italic red]base58 decode                  [/]8.[italic red]server information")      
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

elif choice == "6" :
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

elif choice == "7" : 
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

elif choice == "8" :
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

else :
    print("invalid chose!")
