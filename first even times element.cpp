#include<stdio.h>
int main(){
	int array1[]={1,1,7,4,54,7,88},count,i,j,temp;
	for(i=0;i<7;i++){
	    count=0;
	    for(j=0;j<7;j++){
	    	if(array1[i]==array1[j]){
	    		count+=1;
	    	}
		}
		if(count%2==0){
	       temp=array1[i];
	       break;
		}
	}
	printf("the first element which appears even number of times in an array is : %d\n",temp);
}
