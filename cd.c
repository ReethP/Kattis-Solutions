#include <stdio.h>
#include <stdlib.h>

int binsearch(int *jack, int lenjack, int cdjill){
	int lower = 0;
	int upper = lenjack-1;
	int middle;
	while(lower <= upper){
		middle = (lower+upper)/2;
		if(cdjill>jack[middle]){lower = middle+1;}
		else if(cdjill<jack[middle]){upper = middle-1;}
		else{return 1;}
	}
	return 0;
}

void looper(){
	while (1){
		int jack, jill;
		scanf("%d", &jack);
		getchar();
		scanf("%d", &jill);
		if((jack == 0 && jill == 0)){
			break;}
		int *jackcds = (int*)malloc(sizeof(int)*jack);
		int cdjack;
		int cdjill;
		int both = 0;

		for(int i = 0; i<jack;i++){
			scanf("%d", &cdjack);
			jackcds[i] = cdjack;
		}

		for(int i = 0; i<jill;i++){
			scanf("%d", &cdjill);
			if(binsearch(jackcds,jack,cdjill) == 1){
				both = both+1;
			}
		}
		printf("%d\n",both);
		free(jackcds);
		}
}
int main(){
	looper();
	return 0;
}