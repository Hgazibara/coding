#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

void printArray(int ar_size, int* ar) {
    int i;
    for(i = 0; i < ar_size; ++i) {
        printf("%-d ", ar[i]);
    } 
    printf("\n");
}

/* Head ends here */
void insertionSort(int ar_size, int *  ar) {
    int key = ar_size-1;
    int value = ar[key];
    
    while(key > 0 && value < ar[key-1]) {
        ar[key] = ar[key-1];
        printArray(ar_size, ar);
        --key;
    }
    
    ar[key] = value;
    printArray(ar_size, ar);
}

/* Tail starts here */
int main(void) {
   
    int _ar_size;
    scanf("%d", &_ar_size);
    int _ar[_ar_size], _ar_i;
    for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
        scanf("%d", &_ar[_ar_i]); 
    }

    insertionSort(_ar_size, _ar);
   
    return 0;
}