#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void buy_flag()
{
    system("cat flag.txt");
}

void vuln()
{
    char buffer[128];
    printf("Oh my RoP\n");
    scanf("%s", buffer);
    printf("Thanks for the RoP!\n");
}

void main()
{
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    // char buffer[128];
    // printf("Oh my RoP\n");
    // scanf("%s", buffer);
    // printf("Thanks for the RoP!\n");
    int saldo = 10;
    int menu = 0;
    char get_menu[4];
    while (1)
    {
        int temp;
        printf("Oh My ROP\n");
        printf("Your RoP Power: $%d\n", saldo);
        printf("1. Tarik RoP Kamu\n");
        printf("2. Beli RoP Energy($313370)\n");
        printf("3. Feedback\n");
        printf("4. exit\n");
        printf("choose: \n");

        scanf("%1s", &get_menu);
        fflush(stdin);

        if (*get_menu == '1')
        {
            printf("Mau Tarik Berapa RoP?\n: ");
            scanf("%d", &temp);
            if (temp > saldo)
            {
                printf("not enough balance\n");
            }
            else if (saldo - temp)
            {
                saldo = saldo - temp;
                printf("balance updated!\n");
            }
            else
            {
                exit(0);
            }
        }

        else if (*get_menu == '2')
        {
            if (saldo > 313370)
            {
                buy_flag();
            }
            else if (saldo < 313370)
            {
                printf("not enough money!\n");
            }
            else
            {
                exit(0);
            }
        }

        else if (*get_menu == '3')
        {
            vuln();
        }

        else if (*get_menu == '4')
        {
            exit(0);
        }

        else
        {
            printf("only 1-4\n");
        }
    }
}