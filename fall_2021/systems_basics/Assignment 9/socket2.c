#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <netdb.h>

#define MAX 2000

pthread_t thread1;
int sock = 0;


void* to_server();
void* to_client();

int main (int argc, char *argv[])
{
	struct sockaddr_in serv_add;
	struct hostent* host;
	char name[5] = "dh974";

	

	if((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0){
		perror("socket creation\n");
		exit(1);
	}
	host = gethostbyname("tux3");
	if(host == NULL) {
		perror("gethostbyname");
	}
	serv_add.sin_family = AF_INET;
	serv_add.sin_port = htons(2020);
	memmove(&(serv_add.sin_addr.s_addr), host->h_addr, host->h_length);
	


	if(connect(sock, (struct sockaddr *)&serv_add, sizeof(serv_add)) < 0){
		perror("Failed to connect socket\n");
		exit(2);
	}


	send(sock, name, sizeof(name), 0);
	if(pthread_create(&thread1, NULL, &to_server, NULL) != 0){
		perror("pthread create problem\n");
		exit(1);
	}
	to_client();
	
}

void* to_client()
{
	while(1){
		char recd_msg[MAX];
		
		memset(&recd_msg, 0, MAX);
		int check = recv(sock, &recd_msg, sizeof(recd_msg), 0);
		if(check <= 0){
			printf("Goodbye\n");
			close(sock);
			exit(0);
		}
		recd_msg[strlen(recd_msg)-1] = '\0';
		printf("%s\n", recd_msg);
	}

}



void* to_server()
{
	while(1){
		char send_msg[MAX];
		memset(&send_msg, 0, MAX);
		if(fgets(send_msg, MAX, stdin) == NULL){
			printf("Goodbye\n");
			close(sock);
			exit(0);
		}

		int buf = strlen(send_msg);
		char trunc_msg[buf];
		strcpy(trunc_msg, send_msg);
		send(sock, &trunc_msg, sizeof(trunc_msg), 0);
	}
		

}



