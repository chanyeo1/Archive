[Go To Back](../postgresql.md)

# Primary Keys vs. UNIQUE Constraints in PostgreSQL

## 기본키와 유니크 제약조건의 역할
- `PostgreSQL`에서 기본키와 유니크키는 인덱스를 생성한다.

## NULL 처리
- `PostgreSQL`에서 기본키는 `NOT NULL` 제약 조건을 가진다. 하지만 유니크키는 `NULL` 값을 허용한다.

## 외래키 사용
- `PostgreSQL`에서 기본키와 유니크 키는 외래키로 사용가능하다.

## 결론
- 기본키와 유니크키는 논리적인 관점에서 중요할 뿐만 아니라 데이터베이스 성능 문제이기도 하다. 보통 인덱싱은 성능에 상당한 영향을 미치기 때문이다.
- PostgreSQL의 좋은 성능에 대해 알고 싶다면 [PostgreSQL performance](https://www.cybertec-postgresql.com/en/postgresql-create-indexes-after-bulk-loading/)을 참고한다.

# Source
- [Primary Keys vs. UNIQUE Constraints in PostgreSQL](https://www.cybertec-postgresql.com/en/primary-keys-vs-unique-constraints-in-postgresql/)