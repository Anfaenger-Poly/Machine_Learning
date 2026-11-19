/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int* p;
	int a;

	printf("%p\n", p);
	
	a = 5;
	p = &a;

	printf("%p\n", p);
	printf("%d\n", *p);

	return 0;
}
