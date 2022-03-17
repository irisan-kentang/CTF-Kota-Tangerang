#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string, random


def main():
    ranges = 8
    random_number = "".join(random.SystemRandom().choices(string.digits, k=ranges))
    for i in range(ranges):
        my_input = input("Masukan Angka: ")
        
        exec(my_input)  # be carefull with this function
        print("Anda memilih: ", my_input)
        if my_input == random_number:
            with open("flag.txt", "r") as f:
                baca = f.read()
                print("Flag = %s" % (baca))
                exit(1)
        else:
            print("Admin Memilih: ", random_number)
            print("Tidak Cocok :(\n")
        break


if __name__ == "__main__":
    main()
