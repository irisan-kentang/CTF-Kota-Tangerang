#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

random_number = random.randint(0, 9999)
my_input = input("Masukan Angka: ")

print("Anda memilih: ", str(my_input))
if my_input == random_number:
    with open("flag", "r") as f:
        baca = f.read()
        print("Congrats: ", baca)
        # print(f"Flag: {baca}")
        exit(1)
else:
    print("Mimin memilih : ", str(random_number))
    print("Tidak Cocok :(\n")
