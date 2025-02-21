<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# PORT SCANNER

<a href="https://github.com/GabrielLugooo/Ports-Scanner" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Port%20Scanner-000000" alt="English Scanner" /></a>
<a href="https://github.com/GabrielLugooo/Ports-Scanner/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Port%20Scanner-green" alt="Spanish Scanner" /></a>

### Objective

This project, PortScanner, is a Python-based tool designed to scan open ports on a given IP address.

It helps users identify potential vulnerabilities by detecting which ports are accessible.

This can be useful for network security assessments and penetration testing.

### Skills Learned

- Working with the `socket` library in Python for network communication.
- Understanding port scanning and its role in cybersecurity.
- Handling user input and managing network timeouts efficiently.
- Detecting running services on open ports.
- Exporting scan results to a file for analysis.
- Implementing multi-threading to improve scanning speed.
- Scanning both TCP and UDP ports.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

### Project

#### Code with Comments (English)

```python
# PortScanner
# Import the necessary libraries
import socket
import threading
from colorama import Fore, Style, init

# Initialize colorama for colored output
init()
lock = threading.Lock()

# Scan TCP
def scan_tcp(ip, port, file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port, 'tcp')
        except:
            service = "Unknown Service"
        result_text = f"{Fore.GREEN}[+] Open TCP Port: {port} ({service}){Style.RESET_ALL}"
    else:
        result_text = f"{Fore.RED}[-] Closed TCP Port: {port}{Style.RESET_ALL}"

    with lock:
        print(result_text)
        file.write(result_text + "\n")
    sock.close()

# Scan UDP
def scan_udp(ip, port, file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    try:
        sock.sendto(b"", (ip, port))
        data, _ = sock.recvfrom(1024)
        result_text = f"{Fore.GREEN}[+] Open UDP Port: {port}{Style.RESET_ALL}"
    except socket.timeout:
        result_text = f"{Fore.RED}[-] Closed UDP Port: {port}{Style.RESET_ALL}"
    except Exception:
        result_text = f"{Fore.YELLOW}[?] Possibly Open UDP Port: {port} (No response){Style.RESET_ALL}"

    with lock:
        print(result_text)
        file.write(result_text + "\n")
    sock.close()

# Ask to user to imput the IP of destination
ip = input("Enter the target IP address: ")

with open("scan_results.txt", "w") as file:
    threads = []

    for port in range(1, 1025):  # Reduced range for speed
        t1 = threading.Thread(target=scan_tcp, args=(ip, port, file))
        t2 = threading.Thread(target=scan_udp, args=(ip, port, file))
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()

    for t in threads:
        t.join()
```

### Limitations

PortScanner it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
