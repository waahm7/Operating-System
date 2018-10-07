#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>
#include <string.h>

int main(){
	int arr[1000];
	int sum=0;
	for(int i=0;i<1000;i++)
		arr[i]=i+1;
	//created 256 bytes of shared memory
	void* sharedMemory=mmap(NULL,256,PROT_READ | PROT_WRITE,MAP_ANONYMOUS | MAP_SHARED,0,0);
	int pid=1;
	int childNum = -1;
    while(childNum<9&&pid>0){
    	
    	pid=fork();
    	if(pid<0){
			printf("Error\n");
			exit(-1);
		}
    	childNum++;
    }
	if(pid==0){
		sum=0;
		for(int i=0+(100*childNum);i<(100+(100*childNum));i++)
			sum+=arr[i];

		printf("This is child %d : %d\n",childNum,sum);
		memcpy((sharedMemory)+(sizeof(sum)*childNum),&sum,sizeof(sum));
		exit(0);		
	}

	else if(pid>0){
		for(int i=0;i<10;i++)
			wait(NULL);
	    unsigned int total=0;
	    for(int i=0;i<10;i++){
	   		int num=(*(unsigned int*)(sharedMemory+(i*sizeof(int))));
	   		total+=num;
	    }
	   	printf("parrent:%d\n",total);
	
	}

	return 0;
}
	