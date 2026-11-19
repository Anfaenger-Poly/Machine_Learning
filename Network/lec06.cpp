/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int input;

	scanf("%d", &input);

	switch (input) {
		case 1:
			printf("It's yummy\n");
			break;
		case 2:
			printf("It's cool\n");
			break;
		case 3:
			printf("zzz \n");
			break;
		defaule:
			printf("I don't get it\n");
			break;
	}
	return 0;
}
