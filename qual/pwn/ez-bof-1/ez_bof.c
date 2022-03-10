#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

// echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
// gcc -fno-stack-protector -z execstack -o bug bug.c

int main(int argc, char const *argv[])
{
    char name[0x64];
    puts("Nama Kamu Siapa? ");
    gets(name);
    if (name > 0x64)
        system("echo \"Hi, %s. Selamat Datang di Tangerang Kota CTF 2022!\n flagnya :)\"; cat flag.txt");
    else
        puts("Ok thanks");
    return 0;
    // printf("Hi, %s. Selamat Datang di Tangerang Kota CTF 2022!\n", name);
    // return 0;
}