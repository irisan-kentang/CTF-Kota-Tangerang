#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char **argv)
{
    char nama[100];
    puts("Siapa Nama Kamu?");
    gets(nama);
    if (nama > 100)
        printf("Hi, %s. Selamat datang di Tangerang Kota CTF 2022 :)\n", nama);
    else
        puts("Nope :)");
}
