read -p "are you root? : " root

if [[ $root == "yes" ]] ; then
 echo "     [+]create the enviroment..."
 sudo apt install python3-venv
 python -m venv venv
 source venv/bin/activate
 echo "     [+]install the libaries..."
 pip install requests
 pip install socket
 
 pip install base64
 pip install base58
 pip install datetime
 pip install rich 
 pip install pyfiglet
 pip install geocoder
 pip install folium

elif [[ $root == "no" ]] ; then
 echo "you most to be root to use this programme are you root!"

fi 
