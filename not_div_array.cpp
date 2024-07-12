#include<stdio.h>
int main()
{
	int array1[6]={15,45,17,25,18,12},array2[3]={4,6,8},count=0;
	printf("the elements in first array which are not divisible by any one of the elements in second array are : \n");
	for(int i=0;i<6;i++){
		for(int j=0;j<3;j++){
			if(array1[i]%array2[j]==0){
				count+=1;
			}
			else{
				printf("");
			}
		}
		if(count==0){
			printf("%d\n",array1[i]);
		}
	}
}
