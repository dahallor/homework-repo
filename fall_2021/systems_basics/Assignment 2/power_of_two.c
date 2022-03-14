#include <stdio.h>
#include <stdlib.h>

int main()
{	
	int powOfTwo[] = {1, 2, 4, 8, 16, 32, 64};
	for(int n = 1; n <= 100; n++){
		int i = 0;
		int n_prime = n;
		char confirmation = 'n';
		while(1){
			for(int j = 0; j <= 7; j++){
				if(powOfTwo[j] == n_prime){
					printf("%d\t%d\n", n, i);
					confirmation = 'y';
				}	
			}
			if(confirmation == 'y'){
				break;
			}
			if(n_prime%2 == 0){
				n_prime = n_prime/2;
				i++;
				continue;		
			}
			if(n_prime%2 != 0){
				n_prime = n_prime*3 + 1;
				i++;
				continue;
			}
		}
	}	
	return 0;
}


