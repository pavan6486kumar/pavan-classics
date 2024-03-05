#include<stdio.h>
#include<math.h>
int main()
{
	int num,count=0,arm=0,dig,temp1,temp2;
	printf("enter any positive integer : ");
	scanf("%d",&num);
	temp1 = num;
	temp2 = num;
	while(num>0){
		num=num/10;
		count+=1;
	}
	for(int i=0;i<count;i++){
		dig=temp1%10;
		temp1 = temp1/10;
		arm+=pow(dig,count);
	}
	if(temp2==arm){
		printf("the given number %d is an armstrong number",temp2);
	}
	else{
		printf("the given number %d is not an armstrong number",temp2);
	}
}
