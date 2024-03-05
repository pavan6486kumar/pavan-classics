#include<stdio.h>
int main(){
	int array1[]={15,4,7,99,54,67,88};
	for(int j=0;j<7;j++){
	    for(int i=0;i<6;i++){
		    if(array1[i]>array1[i+1]){
		        int temp=array1[i];
			    array1[i]=array1[i+1];
			    array1[i+1]=temp;
		    }
	    }
	}
	printf("the second largest number in the given array is : %d",array1[5]);
}
