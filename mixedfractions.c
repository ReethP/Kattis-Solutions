#include <stdio.h>

int main(){
while(1){
	int firnum, secnum;
	scanf("%d %d", &firnum, &secnum);
	if(firnum == 0 && secnum == 0){
		break;
	}
	else{
		int counter = 0, product = 0;
		while(firnum >= secnum){
				product = firnum - secnum;
				firnum = firnum - secnum;	
				counter = counter + 1;}
		printf("%d %d / %d\n", counter, firnum, secnum);
	}
}}