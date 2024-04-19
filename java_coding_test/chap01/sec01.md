[Go To Back](../javaCodingTest.md)

# 1.1 시간 복잡도 표기법 알아보기

- 시간 복잡도: 주어진 문제를 해결하기 위한 연산 횟수, 일반적으로 `1억 번의 연산 = 1초`로 간주

## 시간 복잡도 정의

**시간 복잡도 유형***
- 빅-오메가: `최선일 때(best case)`의 연산 횟수를 나타내는 표기법
- 빅-세타: `보통일 때(average case)`의 연산 횟수를 나타내는 표기법
- 빅-오: `최악일 때(worst case)`의 연산 횟수를 나타내는 표기법

**시간 복잡도 예제 코드**
```
// timeComplexityExample1.java
public class timeComplexityExample1 {
    public static void main(String[] args) {
        // 1 ~ 100 사이 값 랜덤 선택
        int findNumber = (int)(Math.random() * 100);
        for(int i = 0; i < 100; i++) {
            if(i == findNumber) {
                System.out.println(i);
                break;
            }
        }
    }
}
```
- 빅-오메가의 시간 복잡도: `1번`
- 빅-세타의 시간 복잡도: `2/N번`
- 빅-오의 시간 복잡도: `N번`

## 코딩 테스트에서는 어떤 시간 복잡도 유형을 사용해야 할까?
- 다양한 테스트 케이스를 수행해 모든 테스트 케이스를 통과해야만 하므로 시간 복잡도는 `최악일 때(worst case)`를 염두에 둬야 한다.

