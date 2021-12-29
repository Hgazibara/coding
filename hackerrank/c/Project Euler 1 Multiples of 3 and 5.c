#include <stdio.h>

int main(void) {
	
    int test_cases = 0;
	long long sum;
	int limit;
	
    scanf("%d", &test_cases);
    
    while(test_cases > 0) {
        
        sum = 0L;
        scanf("%d", &limit);

        long long last_number = ((limit-1)/3)*3;
        long long n = last_number/3;
        sum += (3 + last_number)*n/2;
        
        last_number = ((limit-1)/5)*5;
        n = last_number/5;
        sum += (5 + last_number)*n/2;
	
        last_number = (last_number/15)*15;
        n = last_number/15;
        sum -= (15+last_number)*n/2;
        
        printf("%lld\n", sum);
        --test_cases;
    }
	
	return 0;
}