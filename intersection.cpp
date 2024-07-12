#include<stdio.h>
int main()
{
	int array1[6]={1,3,6,78,35,55},array2[7]={12,24,35,24,88,120,155},array3[]={},count=0;
	for(int i=0;i<6;i++){
		for(int j=0;j<7;j++){
			if(array1[i]==array2[j]){
				array3[count]=array1[i];
				count+=1;
			}
			else{
				printf("");
			}
		}
	}
	for(int k=0;k<count;k++){
		printf("%d",array3[k]);
	}
}
