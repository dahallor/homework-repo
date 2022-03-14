#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"


int main(int argc, char* argv[])
{
	CComp dates;
	FILE *fp;
	int year1 = atoi(argv[1]);
	int year2 = atoi(argv[2]);

	fp = fopen("ccomp.db", "r");
	flock(fileno(fp), LOCK_EX);

	if(year1 > year2){
		fprintf(stderr, "Lowest numbered year must come first\n");
		exit(1);
	}
	for(int i = 0; !feof(fp); i++){
		fread(&dates, sizeof(CComp), 1, fp);
		if(year1 <= dates.year && dates.year <= year2 && i == dates.id){
			printf("\n");
			printf("Id: %d\n", dates.id);
			printf("Maker: %s\n", dates.maker);
			printf("Model: %s\n", dates.model);
			printf("Year: %d\n", dates.year);
			printf("CPU: %s\n", dates.cpu);
			printf("Desc: %s\n", dates.desc);
			printf("------------------\n");		
			}
			
		}




	flock(fileno(fp), LOCK_UN);
	fclose(fp);





}
