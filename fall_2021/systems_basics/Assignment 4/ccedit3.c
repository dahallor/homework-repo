#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include <string.h>
#include "cc.h"



void edit_db(int id, char selection[], char answer[], FILE *fp, CComp editor);

int main(int argc, char * argv[])
{
	CComp editor;
	FILE *fp;
	int id;
	char answer[255];
	char input[255];
	char selection[255] = "";
	

	fp = fopen("ccomp.db", "r+");
	flock(fileno(fp), LOCK_EX);

	printf("Please enter ID number of entry you wish to edit\n");
	fgets(input, 255, stdin);
	id = atoi(input);

	printf("Do you wish to edit the maker of this entry? Enter what you want the value to be or press ENTER to skip\n");
	fgets(answer, 255, stdin);
	if(strcmp(answer, "\n") != 0){
		answer[strlen(answer)-1] = '\0';
		strcpy(selection, "make");
		edit_db(id, selection, answer, fp, editor);
	}

	printf("Do you wish to edit the model of this entry? Enter what you want the value to be or press ENTER to skip\n");
	fgets(answer, 255, stdin);
	if(strcmp(answer, "\n") != 0){
		answer[strlen(answer)-1] = '\0';
		strcpy(selection, "model");
		edit_db(id, selection, answer, fp, editor);
	}

	printf("Do you wish to edit the year of this entry? Enter what you want the value to be or press ENTER to skip\n");
	fgets(answer, 255, stdin);
	if(strcmp(answer, "\n") != 0){
		strcpy(selection, "year");
		edit_db(id, selection, answer, fp, editor);
	}

	printf("Do you wish to edit the CPU of this entry? Enter what you want the value to be or press ENTER to skip\n");
	fgets(answer, 255, stdin);
	if(strcmp(answer, "\n") != 0){
		answer[strlen(answer)-1] = '\0';
		strcpy(selection, "CPU");
		edit_db(id, selection, answer, fp, editor);
	}

	printf("Do you wish to edit the description of this entry? Enter what you want the value to be or press ENTER to skip\n");
	fgets(answer, 255, stdin);
	if(strcmp(answer, "\n") != 0){
		answer[strlen(answer)-1] = '\0';
		strcpy(selection, "desc");
		edit_db(id, selection, answer, fp, editor);
	}

}


void edit_db(int id, char selection[], char overwrite[], FILE *fp, CComp editor)
{
	fseek(fp, id * sizeof(CComp), SEEK_SET);
	fread(&editor, sizeof(CComp), 1, fp);

	if(strcmp(selection, "make") == 0){
		strncpy(editor.maker, overwrite, Nmaker-1);
		editor.maker[Nmaker-1] = '\0';
	}
	if(strcmp(selection, "model") == 0){
		strncpy(editor.model, overwrite, Nmodel-1);
		editor.model[Nmodel-1] = '\0';
	}
	if(strcmp(selection, "year") == 0){
		editor.year = atoi(overwrite);
	}
	if(strcmp(selection, "CPU") == 0){
		strncpy(editor.cpu, overwrite, Ncpu-1);
		editor.cpu[Ncpu-1] = '\0';
	}
	if(strcmp(selection, "desc") == 0){
		strncpy(editor.desc, overwrite, Ndesc-1);
		editor.desc[Ndesc-1] = '\0';
	}
	fseek(fp, id * sizeof(CComp), SEEK_SET);	
	fwrite(&editor, sizeof(CComp), 1, fp);
}


