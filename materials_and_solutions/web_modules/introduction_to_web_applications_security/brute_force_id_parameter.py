import requests
import sys
import re

if (len(sys.argv) != 2):
    raise Exception('Syntax: python3 program.py ip_address')

ip_address = sys.argv[1]

for i in range(100):
    r = requests.get(f'{ip_address}/?id={i}')
    if re.search('CS[0-9]+', r.text):
        print(re.search('CS[0-9]+', r.text))
