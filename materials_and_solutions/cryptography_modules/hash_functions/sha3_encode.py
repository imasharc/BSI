import hashlib
import sys

if (len(sys.argv) != 2):
    raise Exception('Syntax: python3 program.py string_in')

sha3 = hashlib.sha3_512()
sha3.update(sys.argv[1].encode('utf-8'))
print(sha3.digest())
