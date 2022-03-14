#include <sys/file.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cc.h"

int main(int argc, char *argv[])
{
	CComp match;
	FILE *fp;
	int i;
	char line[255];

	fp = fopen("ccomp.db", "r");
	flock(fileno(fp), LOCK_EX);

	if(argc != 2){
		fprintf(stderr, "Please enter valid input to search\n");
		exit(1);
	}
	
	
	for(i = 0; !feof(fp); i++){
		fread(&match, sizeof(CComp), 1, fp);
		if(i != match.id){
			continue;
		}
		if(strstr(match.maker, argv[1]) != NULL || strstr(match.model, argv[1]) != NULL || strstr(match.desc, argv[1]) != NULL){
			if(i == match.id){
				printf("\n");
				printf("Id: %d\n", match.id);
				printf("Maker: %s\n", match.maker);
				printf("Model: %s\n",match.model);
				printf("Year: %d\n", match.year);
				printf("CPU: %s\n", match.cpu);
				printf("Desc: %s\n", match.desc);
				printf("------------------\n");		
				}
		}

	}



	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	return 0;

	
}
