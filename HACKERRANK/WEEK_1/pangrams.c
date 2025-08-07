#include <stdio.h>

int main() {
    char str[1000];
    int i, j;
    int count = 0;
    int found;

    
    gets(str); 

    
    for (char ch = 'a'; ch <= 'z'; ch++) {
        found = 0; 

        for (i = 0; str[i] != '\0'; i++) {
            
            if (tolower(str[i]) == ch) {
                found = 1;
                break;
            }
        }

        if (found == 1) {
            count++;
        }
    }

    
    if (count == 26) {
        printf("pangram\n");
    } else {
        printf("not pangram\n");
    }

    return 0;
}