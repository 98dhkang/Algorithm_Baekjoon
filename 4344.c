#include <stdio.h>

int main(){
	int c, n;
	int sum[10] = { 0 };
	int cnt = 0;
	int score[100];
	int av[10];
	float per[100];

	scanf("%d", &c); // �׽�Ʈ ���̽��� ����

	for (int i = 0; i < c; i++){ //�׽�Ʈ ���̽��� ������ŭ �л����� ����
		scanf("%d", &n); // �л��� ��
		for (int j = 0; j < n; j++){ // �л��� �� ��ŭ ������ ����
			scanf("%d", score[j]); //����
			sum[i] += score[j]; // 0��° ���̽����� �л����� ���� �� ��
			// �� ������ ������ϱ� ������ �迭�� ����
			// �� ���̽��� �յ� ���� �����ؾ� ��
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