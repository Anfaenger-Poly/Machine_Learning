/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int coins [] = {500, 100, 50, 10};
	int n, i;

	printf("금액을 입력하세요 : ");
	scanf("%d", &n);
	
	for (i = 0; i < 4; i++) {
                printf("%d원: %d개\n", coins[i], n / coins[i]);
                n %= coins[i];
        }

	return 0;
}
