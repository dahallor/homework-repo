#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[])
{
	CComp target;
	FILE *fp;
	int index;

	if(argc != 2) {
		fprintf(stderr, "Usage: ccitem id\n");
		exit(1);
	}
	fp = fopen("ccomp.db", "r+");
	flock(fileno(fp), LOCK_EX);
	index = atoi(argv[1]);
	fseek(fp, index * sizeof(CComp), SEEK_SET);
	fread(&target, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	if(index != target.id) {
		fprintf(stderr, "No such item\n");
		exit(2);
	}
	printf("\n");
	printf("Id: %d\n", target.id);
	printf("Maker: %s\n", target.maker);
	printf("Model: %s\n", target.model);
	printf("Year: %d\n", target.year);
	printf("CPU: %s\n", target.cpu);
	printf("Desc: %s\n", target.desc);
	printf("----------------------\n\n");
	exit(0);
}
