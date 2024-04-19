[Go To Back](../javaCodingTest.md)

# 1.2 시간 복잡도 활용하기

## 알고리즘 선택의 기준으로 사용하기

### 000. 수 정렬하기

- 시간제한 2초 = 2억 번 이하의 연산 횟수
- `시간 제한`과 `데이터 크기` → 정렬 알고리즘 선택
- 연산 횟수는 1초에 1억 번 연산하는 것을 기준으로 생각
- 시간 복잡도는 항상 최악일 때, 즉 데이터의 크기가 가장 클 때를 기준으로 생각

**연산 횟수 계산 방법**
```
연산 횟수 = 알고리즘 시간 복잡도 * 데이터의 크기
```
**알고리즘 적합성 평가**
```
버블 정렬 = (1,000,000)^2 = 1,000,000,000,000 > 200,000,000 → 부적합 알고리즘
병합 정렬 = 1,000,000log(1,000,000) = 약 2,000,000 < 200,000,000 → 적합 알고리즘
```
- 시간 복잡도 분석 → 알고리즘 선택 → 문제의 실마리 찾기

## 시간 복잡도를 바탕으로 코드 로직 개선하기

**시간 복잡도 도출 기준**
- `상수`는 시간 복잡도 계산에서 제외
- 가장 많이 중첩된 반복문의 수행 횟수가 시간 복잡도의 기준

**연산 횟수가 N인 경우**
```
public class 시간복잡도_판별원리1 {
    public static void main(String[] args) {
        int N = 100000;
        int cnt = 0;

        for(int i = 0; i < N; i++) {
            System.out.println("연산 횟수:" + cnt++);
        }
    }
}
```
**연산 횟수가 3N인 경우**
```
public class 시간복잡도_판별원리2 {
    public static void main(String[] args) {
        int N = 100000;
        int cnt = 0;

        for(int i = 0; i < N; i++) {
            System.out.println("연산 횟수:" + cnt++);
        }
        for(int i = 0; i < N; i++) {
            System.out.println("연산 횟수:" + cnt++);
        }
        for(int i = 0; i < N; i++) {
            System.out.println("연산 횟수:" + cnt++);
        }
    }
}
```
**연산 횟수가 N^2인 경우**
```
public class 시간복잡도_판별원리3 {
    public static void main(String[] args) {
        int N = 100000;
        int cnt = 0;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                System.out.println("연산 횟수:" + cnt++);
            }
        }
    }
}
```

