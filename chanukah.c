// iterations = int(input())
// finalans = []
// for i in range(0,iterations):
// 	list1 = list(map(int,input().split()))
// 	num = list1[0]
// 	check = list1[1]
// 	candles = 0
// 	for j in range(0,check):
// 		candles = candles+j+1
// 	candles = candles+check
// 	finalans.append(candles)

// for k in range(0,len(finalans)):
// 	print((k+1),finalans[k])

#include <stdio.h>

int main(){
	int iterations, num, actual,candles;
	scanf("%d",&iterations);
	int finalans[iterations];
	for(int i=0;i<iterations;i++){
		scanf("%d %d", &num, &actual);
		candles = 0;
		for(int j=0;j<actual;j++){
			candles = candles+j+1;}
		candles = candles+actual;
		finalans[i] = candles;
	}
	for(int k =0; k<iterations;k++){
		printf("%d %d\n",k+1,finalans[k]);
	}
}