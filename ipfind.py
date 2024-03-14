import socket
import requests
import netifaces

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    ip_address = response.text
    return ip_address

def get_local_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == 'lo':
            continue
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            ip_address = addresses[netifaces.AF_INET][0]['addr']
            return ip_address

print("O endereço IP público da máquina é:", get_public_ip())
print("O endereço IP da máquina na rede local é:", get_local_ip())