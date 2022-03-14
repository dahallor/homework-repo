#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>


void run_input(char *args[]);
void run_cd(char *args[]);
void redirect(char *args[], int index);
int reset(int saved_in, int saved_out);
void backgrounding(char *args[]);
void fork_exec(char *arguments[], char bg[]);


int main(int argc, char *argv[])
{
	
	char cwd[256];
	char symbol[] = "V=(° °)=V ";
	char bg[] = "n";
	char changed_dir[] = "n";
	char redirection[] = "n";
	char input[255];
	char *args[256];
	char *sub_args[256];
	int saved_in = dup(0);
	int saved_out = dup(1);
	int index = 0;

	while(1){
		//initalization
		memset(sub_args, 0, sizeof(sub_args));
		if(strcmp(redirection, "y") == 0){
			strcpy(redirection, "n");
			reset(saved_in, saved_out);
		}
		if(strcmp(bg, "y") == 0){
			strcpy(bg, "n");
		}
		if(strcmp(changed_dir, "y") == 0){
			strcpy(changed_dir, "n");
		}
		getcwd(cwd, sizeof(cwd));
		printf("%s~%s", cwd, symbol);
		if(fgets(input, 255, stdin) == NULL){
			printf("\n");
			exit(0);
		}
		if(strlen(input) <= 1){
			continue;
		}
		//tokenization
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
		//check for built-in commands
		int i = 0;
		int j = 0;
		while(args[i] != NULL){
			if(strcmp(args[i], "cd") == 0){
				run_cd(args);
				strcpy(changed_dir, "y");
				break;
			}
			else if(strcmp(args[i], ">") == 0){
				index = i;
				strcpy(redirection, "y");
				redirect(args, index);
				i++;
				continue;
			}
			else if(strcmp(args[i], "<") == 0){
				index = i;
				strcpy(redirection, "y");
				redirect(args, index);
				i++;
				continue;
			}
			else if(strcmp(args[i], ">>") == 0){
				index = i;
				strcpy(redirection, "y");
				redirect(args, index);
				i++;
				continue;
			}
			else if(strcmp(args[i], "&") == 0){
				strcpy(bg, "y");
				i++;
				continue;
			}
			if(strcmp(redirection, "n") == 0){
				sub_args[j] = args[i];
			}
			i++;
			j++;
		}
		sub_args[j] = NULL;
		//fork & exec
		if(strcmp(changed_dir, "n") == 0){
			fork_exec(sub_args, bg);
		}
	}
}

void fork_exec(char *arguments[], char bg[])
{
	int id = fork();

	if(id == 0){
		run_input(arguments);
		}
	else if(strcmp(bg, "n") == 0){
		while(wait(NULL) != id);
	}
}


void run_cd(char *args[])
{
	chdir(args[1]);

}

void run_input(char *args[])
{
	execvp(args[0], args);
	printf("exec didn't run\n");
	exit(1);

}

void redirect(char *args[], int index)
{
	int fd;	
	if(strcmp(args[index], "<") == 0){
		fd = open(args[index+1], O_RDONLY);
		dup2(fd, 0);
		close(fd);
	}
	if(strcmp(args[index], ">") == 0){
		fd = open(args[index+1], O_WRONLY | O_CREAT, 0777);
		dup2(fd, 1);
		close(fd);

	}
	if(strcmp(args[index], ">>") == 0){
		fd = open(args[index+1], O_WRONLY | O_CREAT | O_APPEND);
		dup2(fd, 1);
		close(fd);
	}
}

int reset(int saved_in, int saved_out)
{
	dup2(saved_in, 0);
	dup2(saved_out, 1);

	return 0;

}
