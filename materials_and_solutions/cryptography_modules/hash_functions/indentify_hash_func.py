import hashlib
import sys

if (len(sys.argv) != 3):
    raise Exception('Syntax: python3 program.py string_in hash_out')

string_in = sys.argv[1].encode('utf-8')
hash_out = sys.argv[2]

for alg in hashlib.algorithms_available:
    try:
        hash_tmp = hashlib.new(alg)
        hash_tmp.update(string_in)
        if hash_tmp.hexdigest() == hash_out:
            print('Algorithm used: ', alg)
    except:
        print('Exception: ', alg)
