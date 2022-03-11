#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char const *argv[])
{
    char name[0x64];
    puts("Nama Kamu Siapa? ");
    gets(name);
    if (name > 0x64)
        system("echo \"Hi, %s. Selamat Datang di Tangerang Kota CTF 2022!\n flagnya :)\"; cat flag.txt");
    else
        puts("Ok thanks :)");
    return 0;

}
