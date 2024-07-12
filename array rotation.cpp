#include<stdio.h>
int main()
{
	char arr[20];
	printf("enter any string : ");
	scanf("%s",&arr);
	int i=0,count=0;
	while(arr[i]!='\0'){
		count+=1;
		i++;
	}
	char temp=arr[0];
	for(int i=0;i<count-1;i++){
		arr[i]=arr[i+1];
	}
	arr[count-1]=temp;
	for(int i=0;i<count-1;i++){
		printf("%c",arr[i]);
	}
	printf("%c",arr[count-1]);
}
