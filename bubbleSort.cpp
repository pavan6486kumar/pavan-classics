#include<stdio.h>
int main(){
	int n;
	int arr[100];
	printf("enter number of elements : \n");
	scanf("%d",&n);
	printf("enter array elements : \n");
	for(int i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	printf("Original Array\n");
	for(int i=0;i<n;i++){
		printf("%d\t",arr[i]);
	}
	for(int i=0;i<n-1;i++){
		for(int j=0;j<n-1;j++){
			if(arr[j]>arr[j+1]){
				int temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
	printf("\n");
	printf("Sorted Array:\n");
	for(int i=0;i<n;i++){
		printf("%d\t",arr[i]);
	}
}
