import socket
import requests

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    ip_address = response.text
    return ip_address

print("O endereço IP público da máquina é:", get_public_ip())