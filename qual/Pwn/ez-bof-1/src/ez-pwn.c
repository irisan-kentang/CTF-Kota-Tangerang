#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    int hack_me = 0x64;
    char buf[100];

    puts("Masukan Angka (Max 10 digits)");
    gets(buf);

    if (hack_me > 0x64)
        system("echo \"Hi, here is your flag: \"; cat flag.txt");
    else
        puts("Nope :)");
    return 0;
}
