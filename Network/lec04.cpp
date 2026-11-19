/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int i;
	int j;
	int n;

	printf("몇 단?");
	scanf("%d", &n);

	for (i = 1; i < 10; i++) {
		printf("%d * %d = %d", n, i, n*i);
	}

	return 0;
}

