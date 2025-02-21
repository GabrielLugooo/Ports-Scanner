<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# GENERADOR DE CONTRASEÑAS

<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Scanner%20Puertos%20Español-000000" alt="Generador Español" /></a>
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Scanner%20Puertos%20Inglés-green" alt="Generador Inglés" /></a>

### Objetivos

Este proyecto, PortScanner, es una herramienta basada en Python diseñada para escanear puertos abiertos en una dirección IP específica.

Ayuda a los usuarios a identificar posibles vulnerabilidades al detectar qué puertos están accesibles.

Esto puede ser útil para evaluaciones de seguridad en redes y pruebas de penetración.

### Habilidades Aprendidas

- Uso de la biblioteca `socket` en Python para comunicación en redes.
- Comprensión del escaneo de puertos y su papel en la ciberseguridad.
- Manejo de la entrada del usuario y administración eficiente de tiempos de espera en conexiones de red.
- Detección de servicios en puertos abiertos.
- Exportación de resultados del escaneo a un archivo para su análisis.
- Implementación de multi-threading para mejorar la velocidad del escaneo.
- Escaneo de puertos tanto TCP como UDP.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

### Proyecto

#### Código con Comentarios (Español)

```python
# PortScanner
# Importar las librerias necesarias
import socket
import threading
from colorama import Fore, Style, init

# Inicializar colorama para salida en colores
init()
lock = threading.Lock()

# Escanear TCP
def escanear_tcp(ip, puerto, archivo):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((ip, puerto))

    if resultado == 0:
        try:
            servicio = socket.getservbyport(puerto, 'tcp')
        except:
            servicio = "Servicio Desconocido"
        resultado_texto = f"{Fore.GREEN}[+] Puerto TCP Abierto: {puerto} ({servicio}){Style.RESET_ALL}"
    else:
        resultado_texto = f"{Fore.RED}[-] Puerto TCP Cerrado: {puerto}{Style.RESET_ALL}"

    with lock:
        print(resultado_texto)
        archivo.write(resultado_texto + "\n")
    sock.close()

# Escanear UDP
def escanear_udp(ip, puerto, archivo):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    try:
        sock.sendto(b"", (ip, puerto))
        data, _ = sock.recvfrom(1024)
        resultado_texto = f"{Fore.GREEN}[+] Puerto UDP Abierto: {puerto}{Style.RESET_ALL}"
    except socket.timeout:
        resultado_texto = f"{Fore.RED}[-] Puerto UDP Cerrado: {puerto}{Style.RESET_ALL}"
    except Exception:
        resultado_texto = f"{Fore.YELLOW}[?] Posiblemente Abierto UDP: {puerto} (Sin respuesta){Style.RESET_ALL}"

    with lock:
        print(resultado_texto)
        archivo.write(resultado_texto + "\n")
    sock.close()

# Se le requiere al usuario que ingrese la IP a escanear
ip = input("Ingrese la dirección IP de destino: ")

with open("resultados_escaneo.txt", "w") as archivo:
    hilos = []

    for puerto in range(1, 1025):  # Rango reducido para mayor velocidad
        h1 = threading.Thread(target=escanear_tcp, args=(ip, puerto, archivo))
        h2 = threading.Thread(target=escanear_udp, args=(ip, puerto, archivo))
        hilos.append(h1)
        hilos.append(h2)
        h1.start()
        h2.start()

    for h in hilos:
        h.join()
```

### Limitaciones

El Scanner de Puertos es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
