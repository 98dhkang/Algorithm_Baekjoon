#include <stdio.h>

int main(){
	int c, n;
	int sum[10] = { 0 };
	int cnt = 0;
	int score[100];
	int av[10];
	float per[100];

	scanf("%d", &c); // 테스트 케이스의 개수

	for (int i = 0; i < c; i++){ //테스트 케이스의 개수만큼 학생수를 받음
		scanf("%d", &n); // 학생의 수
		for (int j = 0; j < n; j++){ // 학생의 수 만큼 점수를 받음
			scanf("%d", score[j]); //점수
			sum[i] += score[j]; // 0번째 케이스에서 학생들의 점수 총 합
			// 각 점수는 살려야하기 때문에 배열로 저장
			// 각 케이스의 합도 따로 저장해야 함
		}
		av[i] = sum[i] / n;

		if (av[i] < score[i]){
			cnt++;
		}

		per[i] = cnt / n * 100;
		printf("%6.3f", per[i]);
	}
	
	return 0;
}