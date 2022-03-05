#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

#define BLOCK_SIZE 8

char *make_key(size_t length) {

    char *tmp = malloc(256);
    char charset[] = "0123456789"
                     "abcdefghijklmnopqrstuvwxyz"
                     "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    
    int i = 0;
    while (length-- > 0) {
        size_t index = (double) rand() / RAND_MAX * (sizeof charset - 1);
        tmp[i++] = charset[index]; 
    }

    return tmp;
}

char *xor_str(char *x, char *y){
    char *base, *key;
    
    if (strlen(x) > strlen(y)){
        base = x;
        key = y;
    }
    else {
        base = y;
        key = x;
    }

    char *res = malloc((sizeof (char)) * strlen(base) + 1);

    for (int i=0; i<strlen(base); i++) {
        res[i] = base[i] ^ key[i % strlen(key)];
    }

    return res;
}

void cryptor(char *filename){
    FILE *fp = fopen(filename,"r");
    

    if (fp) {
        char* buffer = NULL;
        size_t len;
        ssize_t bytes_read = getdelim( &buffer, &len, '\0', fp);
        
        if (bytes_read != -1) {
            char *encrypted = malloc((sizeof (char)) * bytes_read + 1);
            char *current = malloc((sizeof (char)) * BLOCK_SIZE + 1);
            char *str;

            int pos = 0;

            for (int i=0; i<bytes_read; i+=BLOCK_SIZE) {
                char *temp = malloc((sizeof (char)) * BLOCK_SIZE + 1);
                char *key = make_key(BLOCK_SIZE);

                for (int j=0; j<BLOCK_SIZE; j++){
                    temp[j] = buffer[i+j];
                }

                if (!i) {
                    str = xor_str(temp, key);

                    strcat(encrypted, str);
                }
                else {
                    str = xor_str(
                        xor_str(temp, key),
                        current
                    );

                    strcat(encrypted, str);
                }

                strcpy(current, str);
            }

            FILE *fpo = fopen("flag.txt.enc","wb");
            if (fpo != NULL){
                fputs(encrypted, fpo);
                fclose(fpo);
            }
        }
    }
}

int main(void) {
  srand(time(((void *)0)));
  cryptor("flag.txt");
}

