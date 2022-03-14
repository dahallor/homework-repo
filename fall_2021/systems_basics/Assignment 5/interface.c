#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>


void child_p(char choice[], char cmd[], char *vector[]);


int main(int argc, char* argv[])
{
	char cmd[50] = "placehold";
	char buffer[50];
	char *vector[50];
	char choice[10];
	int id;
	

	while(atoi(choice) != 8){
		printf("\nHello!\n");
		printf("Please select the number of the program you wish to run:\n");
		printf("1) ccadd\n2) ccitem\n3) cclist\n4) ccdel\n5) ccmatch\n6) ccyear\n7) ccedit\n8) exit\n\n");
		fgets(choice, 10, stdin);
		
		id = fork();
		if(id == 0){
			//child
			for(int i = 0; i < 50; i++){
				vector[i] = NULL;
			}
			child_p(choice, cmd, vector);
		}
		else{
			//parent
			wait(NULL);
		}

	}


}





void child_p(char choice[10], char cmd[20], char *vector[2])
{
	if(atoi(choice) == 1){
		strcpy(cmd, "ccadd");
		vector[0] = "ccadd";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);
	}
	if(atoi(choice) == 2){
		strcpy(cmd, "ccitem");
		vector[0] = "ccitem";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);
	}
	if(atoi(choice) == 3){
		strcpy(cmd, "cclist");
		vector[0] = "cclist";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);
	}
	if(atoi(choice) == 4){
		strcpy(cmd, "ccdel");
		vector[0] = "ccdel";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);
	}
	if(atoi(choice) == 5){
		strcpy(cmd, "ccmatch");
		vector[0] = "ccmatch";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);
	}
	if(atoi(choice) == 6){
		strcpy(cmd, "ccyear");
		vector[0] = "ccyear";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);

	}
	if(atoi(choice) == 7){
		strcpy(cmd, "ccedit");
		vector[0] = "ccedit";
		execv(cmd, vector);
		perror("exec didn't run\n\n");
		exit(2);

	}
	if(atoi(choice) == 8){
		printf("Goodbye!\n");
		exit(0);
	}
	else{
		printf("Invalid option\n\n");
		exit(1);
	}
}
