#include<stdio.h>

int main(){
	int input = 0, answer = 0;
	do{
	scanf("%d", &input);
	if(input == -1){break;}
	// getchar();
	// entry inputs[input];
	int speed[input], hours[input];
	for(int i=0;i<input;i++){
		scanf("%d %d", &speed[i], &hours[i]);
		// printf("\n");
		// getchar();
		// printf("%d %d\n", speed[i], hours[i]);
	}

	for(int i=0;i<input;i++){
		if(i == 0){
			answer = speed[i]*hours[i];
		}
		else{
			answer = answer+((speed[i])*(hours[i]-hours[i-1]));
			// printf("%d %d\n",(speed[i]-speed[i-1]),(hours[i]-hours[i-1]));
		}
		// printf("%d %d\n", speed[i], hours[i]);
							  }
	printf("%d miles\n", answer);
					  }while(input != -1);
	}
