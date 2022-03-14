#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include <string.h>
#include "cc.h"

int main(int argc, char *argv[])
{
	CComp num;
	FILE *fp;
	int i;

	if(argc != 2){
		fprintf(stderr, "Invalid ID number. Please enter a valid ID number\n");
		exit(1);
	}

	i = atoi(argv[1]);
	fp = fopen("ccomp.db", "r+");
	flock(fileno(fp), LOCK_EX);
	fseek(fp, i * sizeof(CComp), SEEK_SET);
	fread(&num, sizeof(CComp), 1, fp);
	if(i != num.id){
		fprintf(stderr, "ID does not exist, please enter a valid ID number\n");
		exit(1);
	}
	num.id = -1;
	fseek(fp, i * sizeof(CComp), SEEK_SET);
	fwrite(&num, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);

	return 0;


}
