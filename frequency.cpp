#include<stdio.h>
int main(){
	int array1[]={1,4,2,1,5,2,3,1,4,2,5},count;
	for(int i=0;i<10;i++){
		count=0;
		for(int j=0;j<11;j++){
			if(i==array1[j]){
				count+=1;
			}
		}
		printf("%d frequency in array is : %d\n",i,count);
	}
}
