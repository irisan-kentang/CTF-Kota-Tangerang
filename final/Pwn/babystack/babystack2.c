#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main()
{

    int var;
    int check = 0x31337;
    char buf[0x64];

    fgets(buf, 112, stdin);

    printf("\n[buf]: %s\n", buf);
    printf("[check] %p\n", check);

    if ((check != 0x31337) && (check != 0xdeadb00f))
    {
        printf("\nNope, Coba lagi ya!\n");
    }
    else if (check == 0xdeadb00f)
    {
        system("cat flag.txt");
    }
    else
        puts("Nope :)");
    return 0;
}