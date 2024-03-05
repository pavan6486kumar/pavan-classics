#include<stdio.h>
#include<math.h>
int main()
{
	int N,n,k,temp1,temp2,temp3,temp4,temp5,pcount=0,count=0;
	printf("enter any number : ");
	scanf("%d",&N);
	int tcount=0;
	temp1=N;
	while(temp1>0){
		temp1=temp1/10;
		tcount+=1;
    }
    temp2=N;
    temp5=N;
    for(int i=0;i<tcount;i++){
    	count=0;
    	temp3=N;
    	temp2=temp5;
        temp2=temp2/pow(10,tcount-(i+1));
        while(temp3>0){
            k=temp3%10;
            if(k==i){
                count+=1;
            }
            temp3=temp3/10;
        }
        if(temp2==count){
            pcount+=1;
        }
        temp4 = pow(10,tcount-(i+1));
        temp5=temp5%temp4;
    }
    if(tcount==pcount){
    	printf("Congractulations!!!, your number is an auto biographical number.\n");
	}
	else{
		printf("oh! sorry, you guessed a wrong number. Please try again!!!\n");
	}
}
