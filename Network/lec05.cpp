/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main () {
	int n;
	int i;

	printf("1 이외의 숫자를 입력하세요");
	scanf("%d", &n);


	for (i = 2; i < n; i++) {
	       if (n % i == 0) {
			printf("소수가 아닙니다");
			break;
	 	} else {
			printf("소수입니다");
			break;
		}
	}
}	
