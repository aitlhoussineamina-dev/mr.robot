# 🤖 Mr. Robot - Cyber Tool

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Bash-orange.svg)

A lightweight, terminal-based reconnaissance and utility suite written in Python. **Mr. Robot** combines domain lookup, directory brute-forcing, decoding utilities, server header analysis, and interactive IP geolocation mapping into a single command-line interface.

---

## 📸 Key Features

| Option | Feature | Description |
| :---: | :--- | :--- |
| **1** | **IP Resolver** | Resolve web domain names to direct server IP addresses using native socket lookups. |
| **2** | **HTTP Status Checker** | Quickly verify website availability and retrieve standard HTTP status codes. |
| **3** | **Path Scanner** | Scan target URLs for common sensitive endpoints (`/admin.php`, `/robots.txt`, `/secret`, etc.). |
| **4** | **Base58 Decoder** | Decode Base58-encoded hash strings back into readable text. |
| **5** | **Domain Info (WHOIS)** | Query public domain registration details via WHOIS web API integration. |
| **6** | **IP Location Finder** | Geolocate IP addresses and automatically export interactive map markers using `folium`. |
| **7** | **Base64 Decoder** | Instantly decode Base64 strings directly in the terminal. |
| **8** | **Server Info Inspection** | Fetch and display server response headers for quick security profiling. |

---

## 📋 Prerequisites

Ensure you have the following installed on your system before proceeding:

* **Linux** (Ubuntu, Debian, Kali, or Arch recommended)
* **Python 3.x**
* **Bash** shell with `sudo` / `root` privileges (required for script dependencies setup)

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aitlhoussineamina-dev/mr.robot.git
   cd mr.robot
   ```

2. **Run the environment setup script:**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   > 💡 **Note:** When prompted `are you root? :`, enter `yes`. The script will automatically create a Python virtual environment (`venv`) and install required libraries (`rich`, `pyfiglet`, `geocoder`, `folium`, `requests`, `base58`).

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

---

## 🚀 Usage

Run the main interactive script:

```bash
python3 all_in_one.py
```

### Menu Interface
```text
 1. IP address of the server          5. General information of the domain
 2. Web server status code            6. IP location finder
 3. Paths scanning                    7. Base64 decode
 4. Base58 decode                     8. Server information
```

---

## 📁 Repository Structure

```text
mr.robot/
├── all_in_one.py   # Main Python interactive application
├── setup.sh        # Environment preparation and dependency script
└── README.md       # Project documentation
```

---

## 🛡️ Disclaimer

This project is created strictly for **educational and authorized security assessment purposes**. The author assumes no responsibility for misuse or damage caused by this software. Always obtain explicit permission prior to scanning or testing external web servers or infrastructure.

---

## 📜 License

Distributed under the [MIT License](LICENSE).
