#include<stdio.h>
int main()
{
  char arr[20];
  char arr1[20];
  int temp;
  int count=0,i=0,rcount=0,j=0;
  printf("enter a string : ");
  scanf("%s",&arr);
  while(arr[i]!='\0'){
    count+=1;
    i++;
  }
  for(int i=count-1;i>=0;i--){
    arr1[j]=arr[i];
    j++;
  }
  for(int i=0;i<count;i++){
  	if(arr[i]==arr1[i]){
  		rcount+=1;
	}
  }
  if(rcount==count){
  	printf("the given string is a palindrome.");
  }
  else{
  	printf("the given string is not a palindrome.");
  }
}
