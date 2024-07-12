#include<stdio.h>
int main()
{
  char arr[5],sum=0;
  for(int i=0;i<5;i++){
  	printf("enter integer element %d : ",i+1);
    scanf("%d",&arr[i]);
  }
  for(int i=4;i>=0;i--){
    printf("%d\n",arr[i]);
  }
}
