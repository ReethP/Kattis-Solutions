#include<stdio.h>
#include<string.h>

int main(){
	char namearr[100], outputarr[50], holder;
	int index = 0;
	int arrindex = 0;

	scanf("%s", namearr);
	holder = namearr[index];


	while(holder != '\0'){
		holder = namearr[index];
		if(index == 0){
			outputarr[arrindex] = namearr[index];
			arrindex = arrindex+1;
					  }
		else{
			if(holder == '-'){
				outputarr[arrindex] = namearr[index+1];
				arrindex = arrindex+1;
							 }
			}
		index = index+1;
						 }
		outputarr[arrindex] = '\0';
	printf("%s \n", outputarr);

			}