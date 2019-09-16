#include<stdio.h>

int main(){

	char input[250];
	char answer[250];
	int counter = 0;
	scanf("%s", input);

	for(int i = 0;i<250;i++){
		if(input[i] != input[i+1]){
			answer[counter] = input[i];
			counter = counter+1;
		}
	}
	answer[counter] = '\0';
	printf("%s\n", answer);

}