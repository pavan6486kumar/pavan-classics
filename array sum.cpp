#include<stdio.h>
int main()
{
  char arr[5];
  int sum=0;
  for(int i=0;i<5;i++){
  	printf("enter integer element %d : ",i+1);
    scanf("%d",&arr[i]);
  }
  for(int i=0;i<5;i++){
    sum+=arr[i];
  }
  printf("the sum of integers in array is : %d\n",sum);
}
