#include <stdio.h>

void main() {
    int numb[200];
    int PositiveCount = 0;
    int NegativeCount = 0;
    int ZeroCount = 0;
    int i;


    printf("Enter 200 integer values:\n");
    for (i = 0; i < 200; i++) {
    scanf("%d", &numb[i]);
    }

    for (i = 0; i < 200; i++) {
        if (numb[i] > 0) {
           PositiveCount++;
        } else if (numb[i] < 0) {
            NegativeCount++;
        } else {
            ZeroCount++;
        }
    }


    printf("\nCounts:\n");
    printf("Positive numbers: %d\n", PositiveCount);
    printf("Negative numbers: %d\n", NegativeCount);
    printf("Zeroes: %d\n", ZeroCount);

   }
