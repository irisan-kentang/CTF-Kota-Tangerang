#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char flag[] = {37, 56, 7, 94, 8, 10, 2, 0, 50, 26, 16, 3, 56, 36, 108, 57, 44, 69, 5, 45, 9, 6, 107, 6, 58, 16, 49, 52, 54, 46, 24, 75, 60, 26, 84, 68, 106, 12, 15, 4};
char key[] = {95, 95, 115, 51, 99, 114, 101, 116, 95, 107, 101, 121, 95, 95};

int get_index(char* string, char c) {
    char *e = strchr(string, c);
    if (e == NULL) {
        return -1;
    }
    return (int)(e - string);
}

char shift(char val, int num) {
    char *x = "abcdefghijklmnopqrstuvwxyz";
    char *y = "0123456789";
    char *base;

    if (strstr(x, &val)) {
        base = x;
    }
    else if (strstr(y, &val)) {
        base = y;
    }
    else {
        return val;
    }

    int pos = get_index(base, val) + num;

    return base[(pos % (int) strlen(base))];

}

char get_flag(int index){
    char *tmp = malloc(64);

    for (int i=0; i<40; i++) {
        tmp[i] = shift(flag[i] ^ key[i % 14], 20);
    }

    return tmp[index];
}

int main(int argc, char *argv[]) {
    char ans[40];

    printf("Enter flag: ");
    scanf("%s", ans);

    for (int i=0; i<40; i++) {
        if (ans[i] != get_flag(i)) {
            printf("Incorrect flag!");
            return 0;
        }
    }

    printf("Correct flag!");
    return 0;
}