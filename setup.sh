#!/bin/bash

# طلب تأكيد الصلاحيات من المستخدم
read -p "Are you root/sudo user? (yes/no): " root

if [[ "$root" == "yes" ]]; then
    echo "[+] Creating the environment..."
    
    # تحديث المستودعات وتثبيت حزمة البيئة الافتراضية
    sudo apt update && sudo apt install -y python3-venv python3-pip
    
    # إنشاء البيئة الافتراضية وتفعيلها
    python3 -m venv venv
    source venv/bin/activate
    
    echo "[+] Installing the libraries..."
    # ترقية أداة pip أولاً
    pip install --upgrade pip
    
    # تثبيت المكتبات الخارجية فقط
    pip install requests base58 rich pyfiglet geocoder folium
    
    echo "[+] Environment setup successfully!"
else
    echo "[-] Operation cancelled. You must have sudo privileges to run this script."
fi
