#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


char *read_line(char input[], char *p[]);
void run_input(char *args[]);
void run_special(char *args[]);


int main(int argc, char *argv[])
{
	char symbol[] = "V=(° °)=V ";
	char input[255];
	char *args[256];
	int id;

	while(1){
		printf("%s", symbol);
		if(fgets(input, 255, stdin) == NULL){
			printf("\n");
			exit(0);
		}
		if(strlen(input) <= 1){
			continue;
		}
		else{
			int i = 0;
			char* token = strtok(input, " \n\t");
	
			while(token != NULL){
				args[i] = token;
				token = strtok(NULL, " \n\t");
				i++;
				}
			args[i] = NULL;
			}
		
		if(strcmp(args[0], "cd") == 0){
			run_special(args);
			continue;
			}
		id = fork();
		if(id == 0){
		run_input(args);
			}
		else{
			wait(NULL);
		}


		
	}
}




void run_special(char *args[])
{
	chdir(args[1]);

}

void run_input(char *args[])
{
	execvp(args[0], args);
	printf("exec didn't run\n");
	exit(1);

}
