
# PortScanner
# Importar las librerias necesarias
import socket
import threading
from colorama import Fore, Style, init

# Inicializar colorama para salida en colores
init()
lock = threading.Lock()

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