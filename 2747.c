#include <stdio.h>

int main()
{
	int arr[100];
	int n;
	arr[0] = 0;
	arr[1] = 1;
	scanf_s("%d", &n);

	for (int i = 0; i < 50; i++){
		arr[i + 2] = arr[i] + arr[i + 1];
	}
	printf("%d", arr[n]);
	return 0;
}



