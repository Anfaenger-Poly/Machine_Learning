/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int i;

	printf("Please input number : ");
	scanf("%d", &i);

	if (i == 7) {
		printf("7\n");
	} else {
		if (i == 4) {
			printf("4\n");
		} else {
			printf("other numebr : %d\n", i);
		}
	}

	return 0;
}
