[Go To Back](../mysql.md)

# MySQL Recursive CTE

**개요**: MySQL 재귀 CTE와 이를 사용해 계층 구조의 데이터를 순회하는 방법을 배운다.

> `common table expression (CTE)`는 MySQL 버전 8.0 이상인 경우에만 사용 가능하다. 따라서 이번 튜토리얼을 진행하기 전에 올바른 MySQL의 버전이 설치되어 있는지 확인한다.

## 1. MySQL recursive CTE 소개

- 명시된 종료 조건(termination condition)을 만족할 때까지 계층 구조를 순회한다.
- 아래 코드는 재귀 CTE의 문법을 보여준다.

```
WITH RECURSIVE cte_name AS (
    initial_query   -- anchor member
    UNION ALL
    recursive_query -- recursive member that references to the CTE name
)
SELECT * FROM cte_name;

```

### 1.1 재귀 CTE는 세가지 주요 구성 요소

1. `초기 쿼리(initial_query)`
2. `재귀 쿼리(recursive query)` 
    - `재귀 멤버(recursive member)`는 `UNION ALL` 또는 `UNION DISTINCT` 오퍼레이터에 의해 `앵커 멤버(anchor member)`와 조인된다.
3. `종료 조건(termination condition)`
    - 재귀 멤버가 더 이상 로우(row)를 반환하지 않으면 재귀는 중지된다.

### 1.2 재귀 CTE 실행 순서

1. 앵커 멤버와 재귀 멤버로 분리한다.
2. `기본 결과 세트(R0)`를 만들기 위해서 앵커 멤버를 실행한다. `R0`는 다음 이터레이션을 위해 사용한다.
3. 재귀 멤버는 `Ri` 입력값을 받고 `Ri + 1` 출력값을 생성한다. 예를 들어 기본 결과 세트인 `R0`를 입력받으면 결과세트 `R1`을 반환한다. 
4. 재귀 멤버가 결과 세트를 반환하지 못할 때 까지 `3번째 단계`를 반복한다. 즉, 종료 조건을 만족할 때까지 반복한다.
5. 마지막으로 `R0`부터 `Rn` 까지의 모든 결과 세트를 `UNION ALL` 오퍼레이터를 사용해 결합한다.

### 1.3 재귀 멤버 제약조건
- 재귀 멤버는 다음 조건을 반드시 포함하지 않아야 한다.
    - 집계함수(Aggregate function) : `MAX`, `MIN`, `SUM`, `AVG`, `COUNT` 등
    - `GROUP BY` 조건
    - `ORDER BY` 조건
    - `LIMIT` 조건
    - `DISTINCT`
- 위의 제약 조건들은 앵커 멤버에게 적용되지 않는다.
- `UNION DISTINCT`를 사용하는 경우를 제외하고 `DISTINCT`는 허용되지 않는다.
- 재귀 멤버는 CTE name을 한번만 참조하기 때문에 `FROM` 절에 서브쿼리를 사용할 수 없다.

## 2. 기본 MySQL 재귀 CTE 예제
```
WITH RECURSIVE cte_count(n)
AS (
    SELECT 1
    UNION ALL
    SELECT n + 1
    FROM cte_count -- CTE name
    WHERE n < 3
)

SELECT n FROM cte_count;
```

```
# Anchor member
SELECT 1 // R0 : 1

# Recursive Member
# Input
# R0 : 1
# Output
# R1 : 2
SELECT 1 + 1    // R1 : 2
FROM cte_count
WHERE 1 < 3

# Input
# R1 : 2
# Output
# R2 : 3
SELECT 2 + 1    // R2 : 3
FROM cte_count
WHERE 2 < 3

# Input
# R2 : 3
SELECT 3 + 1
FROM cte_count
WHERE 3 < 3     # 종료 조건 만족
```

## 3. 계층 구조 데이터를 순회하기 위해 MysSQL 재귀 CTE 사용하기
```
# mydb 데이터베이스 생성
CREATE DATABASE IF NOT EXIST mydb;

# employees 테이블 생성
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT
); 

# employees 테이블에 데이터 추가
INSERT INTO employees VALUES
    (1, 'John Doe', NULL),         -- CEO, no manager
    (2, 'Jane Smith', 1),          -- Manager, reports to CEO
    (3, 'Bob Johnson', 2),         -- Employee, reports to Jane Smith
    (4, 'Alice Brown', 2),         -- Employee, reports to Jane Smith
    (5, 'Charlie Davis', 3);       -- Employee, reports to Bob Johnson

# MySQL 재귀 CTE 사용
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level
    FROM
        employees
    WHERE
        manager_id IS NULL -- anchor member (root of the hierarchy)

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        eh.level + 1
    FROM 
        employees e
    INNER JOIN
        EmployeeHierarchy eh ON e.manager_id = eh.employee_id -- Recursive member
)

# CTE로 조회
SELECT
    employee_id,
    employee_name,
    manager_id,
    level
FROM
    EmployeeHierarchy
ORDER BY
    level, employee_id;
```

# Source
- [MySQL Recursive CTE](https://www.mysqltutorial.org/mysql-basics/mysql-recursive-cte/)