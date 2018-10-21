#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
int arr[1000];
void *sumOf100Numbers(void *val)
{
    int sum = 0;
    int i = (int)val;
    int end=i+100;
    for(;i < end; i++)
        sum += arr[i];
    return ((void *)sum);
}
int main()
{
    for (int i = 0; i < 1000; i++)
        arr[i] = i + 1;
    pthread_t threads[10];

    for (int i = 0; i < 10; i++)
        pthread_create(&threads[i], (NULL), sumOf100Numbers, (void *)(i*100));
    static int sum=0,tsum=0;
    for (int i = 0; i < 10; i++){
        pthread_join(threads[i], (void **)&tsum);
    	printf("sum is %d thread is %d\n",i, tsum);
        sum+=tsum;
    }
    printf("sum is %d\n", sum);
    return 0;
}
