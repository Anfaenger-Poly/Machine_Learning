/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int* p;
	int a;
	int arr[10] = {3, 2, 1, 4, 5, 8, 7, 6, 10, 9};

	printf("%p\n", p);
	a = 5;
	p = arr;

	printf("%p\n", p);
	printf("%d\n", *(p+1));

	return 0;
}
