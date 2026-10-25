# 🤖 Mr. Robot - All-in-One Cybersecurity Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Linux%20%2F%20Termux-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

**Mr. Robot** is a modular Python-based reconnaissance and network utility toolkit designed for ethical hacking, penetration testing, and web analysis. It consolidates multiple powerful utilities into a single interactive command-line interface.

---

## 🚀 Features

The toolkit features an interactive menu with **10 distinct tools**:

| Option | Module Name | Description |
| :---: | :--- | :--- |
| **1** | **Server IP Resolver** | Resolves domain names to their corresponding server IP addresses using socket programming. |
| **2** | **Web Status Checker** | Fetches and displays HTTP status codes for target URLs. |
| **3** | **Path Scanner** | Brute-forces common web directories, files, and backup paths (`robots.txt`, `admin.php`, `.history`, etc.). |
| **4** | **Base58 Decoder** | Decodes Base58-encoded strings back to plain text. |
| **5** | **OSINT Module** | *[Placeholder / Under Development]* |
| **6** | **General Info (WHOIS)** | Queries domain registration and WHOIS information via `api.whois.vu`. |
| **7** | **IP Location Finder** | Geolocates target IP addresses and generates an interactive Folium map visualization. |
| **8** | **Base64 Decoder** | Decodes Base64-encoded hashes/strings. |
| **9** | **Server Header Inspector** | Inspects and displays HTTP response headers (`Server`, `X-Powered-By`, etc.) of a web server. |
| **10** | **Network Monitor / ARP** | Performs ARP spoofing and sniffs local network DNS queries using Scapy and multithreading. |

---

## 🛠️ Prerequisites & Dependencies

Make sure you have **Python 3.x** installed. The script relies on several external Python libraries:

- `pyfiglet`
- `rich`
- `requests`
- `base58`
- `geocoder`
- `folium`
- `scapy`

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/aitlhoussineamina-dev/mr.robot.git
cd mr.robot
```

### 2. Run the Environment Setup Script
The project includes an interactive setup script that sets up a virtual environment and installs all required dependencies:

```bash
chmod +x setup.sh
./setup.sh
```

> **Note:** Run the script as a non-root user when prompted. It will verify permissions and guide you through the process.

### 3. Manual Installation (Alternative)
If you prefer to set up dependencies manually:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

---

## 💻 Usage

Once dependencies are installed, launch the interactive toolkit:

```bash
python3 all_in_one.py
```

Select an option from the menu by entering the corresponding number:

```text
==================================================
 1. IP Address of the Server    5. OSINT Module
 2. Web Server Status Code     6. General Information (WHOIS)
 3. Paths Scanning              7. IP Location Finder
 4. Base58 Decode               8. Base64 Decode
                                9. Server Information (Headers)
                                10. Network Monitor (ARP/DNS)
==================================================
Choice your option :
```

---

## ⚙️ How It Works (Code Structure)

- **`all_in_one.py`**: Main application script containing the interactive CLI menu, Rich text formatting, network requests, decoding modules, and Scapy packet monitoring logic.
- **`setup.sh`**: Automated Bash script ensuring virtual environment isolation and library installation before tool execution.

---

## ⚠️ Disclaimer

This tool is designed strictly for **educational purposes and authorized security testing** (ethical hacking). Do not use this tool against targets without explicit permission. The developer assumes no liability for misuse or damage caused by this software.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
