/*
 * 이 프로그램은 예제 파일입니다.
 */
// 2026.11.11

#include <stdio.h>

int main() {
	int i;
	int subject, score;
	double sum_score = 0;

	printf("몇 과목인가요?");
	scanf("%d", &subject);

	printf("각 과목 점수를 입력해주세요\n");
	for (i = 1; i <= subject; i++) {
		printf("과목 %d : ", i);
		scanf("%d", &score);
		sum_score = sum_score + score;
	}

	printf("평균 : %.2f\n", sum_score / subject);

	return 0;

}
