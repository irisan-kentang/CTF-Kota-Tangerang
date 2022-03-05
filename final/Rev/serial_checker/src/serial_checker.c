#include <stdio.h>
#include <stdlib.h>

int validate_serial(char *ss){

    if (ss[9] - ss[7] + ss[27]  != 78) {
        return 0;
    }
    if (ss[25] - ss[21]  != 12) {
        return 0;
    }
    if (ss[8] - ss[27] * ss[21]  != -5539) {
        return 0;
    }
    if (ss[22] % ss[28] + ss[27]  != 80) {
        return 0;
    }
    if (ss[25] % ss[1]  != 12) {
        return 0;
    }
    if (ss[25] % ss[17]  != 42) {
        return 0;
    }
    if (ss[27] + ss[24] - ss[22]  != 63) {
        return 0;
    }
    if (ss[7] % ss[10]  != 83) {
        return 0;
    }
    if (ss[13] - ss[5]  != 23) {
        return 0;
    }
    if (ss[22] * ss[22]  != 7396) {
        return 0;
    }
    if (ss[10] - ss[2] * ss[2]  != -4140) {
        return 0;
    }
    if (ss[2] % ss[2]  != 0) {
        return 0;
    }
    if (ss[25] % ss[2]  != 22) {
        return 0;
    }
    if (ss[23] - ss[25]  != -42) {
        return 0;
    }
    if (ss[20] - ss[26] - ss[1]  != -58) {
        return 0;
    }
    if (ss[28] + ss[10]  != 166) {
        return 0;
    }
    if (ss[25] - ss[12]  != 9) {
        return 0;
    }
    if (ss[22] - ss[28] % ss[26]  != 74) {
        return 0;
    }
    if (ss[1] % ss[4]  != 75) {
        return 0;
    }
    if (ss[28] % ss[6] + ss[3]  != 163) {
        return 0;
    }
    if (ss[7] % ss[6]  != 0) {
        return 0;
    }
    if (ss[25] - ss[12]  != 9) {
        return 0;
    }
    if (ss[3] * ss[15]  != 5412) {
        return 0;
    }
    if (ss[9] % ss[14]  != 4) {
        return 0;
    }
    if (ss[7] + ss[5] * ss[0]  != 3953) {
        return 0;
    }
    if (ss[18] - ss[6]  != -7) {
        return 0;
    }
    if (ss[8] + ss[2]  != 151) {
        return 0;
    }
    if (ss[28] % ss[20] + ss[9]  != 167) {
        return 0;
    }
    if (ss[8] - ss[14]  != 4) {
        return 0;
    }
    if (ss[8] - ss[7]  != 3) {
        return 0;
    }
    if (ss[22] * ss[20]  != 7396) {
        return 0;
    }
    if (ss[13] + ss[24]  != 142) {
        return 0;
    }
    if (ss[4] * ss[16]  != 5893) {
        return 0;
    }
    if (ss[25] - ss[28] + ss[21]  != 81) {
        return 0;
    }
    if (ss[17] * ss[10]  != 3825) {
        return 0;
    }
    if (ss[18] - ss[16]  != 5) {
        return 0;
    }
    if (ss[23] % ss[25]  != 45) {
        return 0;
    }
    if (ss[21] + ss[5] % ss[16]  != 120) {
        return 0;
    }
    if (ss[10] + ss[8]  != 171) {
        return 0;
    }
    if (ss[19] % ss[10] + ss[17]  != 124) {
        return 0;
    }
    if (ss[17] + ss[0] % ss[26]  != 62) {
        return 0;
    }
    if (ss[0] * ss[14] + ss[3]  != 7134) {
        return 0;
    }
    if (ss[4] * ss[8]  != 7138) {
        return 0;
    }
    if (ss[23] - ss[0] % ss[27]  != 34) {
        return 0;
    }
    if (ss[26] - ss[1] * ss[10]  != -6306) {
        return 0;
    }
    if (ss[21] - ss[21]  != 0) {
        return 0;
    }
    if (ss[16] - ss[7] * ss[19]  != -6486) {
        return 0;
    }
    if (ss[26] + ss[22] - ss[22]  != 69) {
        return 0;
    }
    if (ss[2] + ss[0]  != 151) {
        return 0;
    }
    if (ss[10] % ss[10]  != 0) {
        return 0;
    }
    if (ss[19] - ss[20] * ss[14]  != -6973) {
        return 0;
    }
    if (ss[27] - ss[5] - ss[22]  != -56) {
        return 0;
    }
    if (ss[9] - ss[6]  != 3) {
        return 0;
    }
    if (ss[2] + ss[27] + ss[6]  != 223) {
        return 0;
    }
    if (ss[25] % ss[23] - ss[8]  != -44) {
        return 0;
    }
    if (ss[7] + ss[0] % ss[17]  != 124) {
        return 0;
    }
    if (ss[15] - ss[17]  != 21) {
        return 0;
    }
    if (ss[22] % ss[13]  != 18) {
        return 0;
    }
    if (ss[20] - ss[7]  != 3) {
        return 0;
    }
    if (ss[23] * ss[25]  != 3915) {
        return 0;
    }
    if (ss[8] * ss[15] + ss[12]  != 5754) {
        return 0;
    }
    if (ss[21] % ss[1]  != 0) {
        return 0;
    }
    if (ss[19] % ss[15]  != 13) {
        return 0;
    }
    if (ss[6] + ss[24]  != 157) {
        return 0;
    }
    if (ss[7] - ss[25] % ss[26]  != 65) {
        return 0;
    }
    if (ss[22] + ss[21] + ss[8]  != 247) {
        return 0;
    }
    if (ss[24] % ss[18] + ss[17]  != 119) {
        return 0;
    }
    if (ss[24] + ss[5]  != 119) {
        return 0;
    }
    if (ss[13] % ss[26]  != 68) {
        return 0;
    }
    if (ss[17] + ss[8]  != 131) {
        return 0;
    }
    if (ss[9] - ss[1]  != 11) {
        return 0;
    }
    if (ss[28] + ss[27]  != 156) {
        return 0;
    }
    if (ss[12] % ss[19]  != 78) {
        return 0;
    }
    if (ss[28] - ss[8] % ss[1]  != 70) {
        return 0;
    }
    if (ss[14] % ss[21]  != 7) {
        return 0;
    }
    if (ss[4] - ss[14] - ss[17]  != -44) {
        return 0;
    }
    if (ss[26] * ss[12]  != 5382) {
        return 0;
    }
    if (ss[15] * ss[8] * ss[23]  != 255420) {
        return 0;
    }
    if (ss[17] + ss[13] % ss[10]  != 113) {
        return 0;
    }
    if (ss[25] % ss[27] - ss[3]  != -70) {
        return 0;
    }
    if (ss[18] % ss[18]  != 0) {
        return 0;
    }
    if (ss[25] - ss[15]  != 21) {
        return 0;
    }
    if (ss[7] * ss[6]  != 6889) {
        return 0;
    }
    if (ss[2] + ss[15]  != 131) {
        return 0;
    }
    if (ss[24] * ss[6] * ss[19]  != 485218) {
        return 0;
    }
    if (ss[0] + ss[9]  != 172) {
        return 0;
    }
    if (ss[23] % ss[26] % ss[9]  != 45) {
        return 0;
    }
    if (ss[6] + ss[17] - ss[8]  != 42) {
        return 0;
    }
    if (ss[0] % ss[17] * ss[28]  != 3321) {
        return 0;
    }
    if (ss[18] + ss[2]  != 141) {
        return 0;
    }
    if (ss[14] * ss[27]  != 6150) {
        return 0;
    }
    if (ss[25] + ss[0]  != 173) {
        return 0;
    }
    if (ss[18] * ss[21]  != 5700) {
        return 0;
    }
    if (ss[12] - ss[8]  != -8) {
        return 0;
    }
    if (ss[20] + ss[11] % ss[14]  != 131) {
        return 0;
    }

    return 1;
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main(int argc, char *argv[]) {
    char *serial_number = malloc((sizeof (char)) * 29 + 1);

    setup();
    printf("Enter a serial number: ");
    scanf("%s", serial_number);

    if (validate_serial(serial_number)) {
        system("cat flag.txt");
    }
    else {
        printf("Incorrect!");
    }

    exit(0);
}