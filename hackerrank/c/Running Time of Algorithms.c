#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

/* Head ends here */
int insertionSort(int ar_size, int *  ar) {
    
    int value, key, i;
    int shifts = 0;
    
    for(i = 1; i < ar_size; ++i) {
    
        key = i;
        value = ar[i];
        
        while(key > 0 && value < ar[key-1]) {
            ar[key] = ar[key-1];
            --key;
            ++shifts;
        }
    
        ar[key] = value;
    }
    
    return shifts;
}

/* Tail starts here */
int main(void) {
   
    int _ar_size;
    scanf("%d", &_ar_size);
    int _ar[_ar_size], _ar_i;
    for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
        scanf("%d", &_ar[_ar_i]); 
    }

    printf("%d", insertionSort(_ar_size, _ar));
   
    return 0;
}