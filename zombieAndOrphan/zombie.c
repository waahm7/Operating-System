#include <stdio.h>
#include <stdlib.h> 
#include <sys/types.h> 
#include <unistd.h> 
int main() 
{ 
	int pid = fork(); 

	if (pid > 0){ 
		sleep(5);
		printf("Parrent process exit\n");
	} 
	else{		
		printf("Child process exit\n");
		exit(0); 
	}		 

	return 0; 
} 

