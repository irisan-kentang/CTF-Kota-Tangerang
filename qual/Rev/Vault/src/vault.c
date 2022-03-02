#include <stdio.h>
#include <string.h>
#include <unistd.h>

char pin_code[] = "427601";
int flag[] = {116, 97, 110, 103, 101, 114, 97, 110, 103, 107, 111, 116, 97, 123, 108, 116, 114, 52, 99, 105, 110, 103, 95, 102, 116, 119, 125};

int main(int argc, char *argv[]) {
    char ans[7];

    printf("Enter Pin code: ");
    scanf("%s", &ans);

    if (!strcmp(ans, pin_code)){
        printf("Correct!\nHere's the flag: ");
        for (int x=0; x<27; x+=1) 
            printf("%c", flag[x]);
    }
    else {
        printf("Wrong Pin!");
    }
    
    return 0;
}
