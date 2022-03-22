#include <stdio.h>

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);

    int target = 0;
    char nama[100];

    printf("Nama Kamu Siapa?\n");
    scanf("%s", nama);
    printf("Hello, ");
    printf(nama, &target);
    printf("!\n");

    if (target == 0x539)
    {
        system("cat flag.txt");
    }
}