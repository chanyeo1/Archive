[Go To Back](./gs.md)

# 데이터 페칭


## 서버 컴포넌트에서 `fetch`로 데이터 페칭하기

- 서버 컴포넌트에서 `TypeScript`로 `async`/`await`를 사용할려면 `5.1.3` 버전 이상과 `@types/react` `18.2.8` 버전 이상을 사용해야 한다. 

```
async function getData() {
    const res = await fetch('https://api.example.com/...')
    // The return value is *not* serialized
    // You can return Date, Map, Set, etc.

    if(!res.ok) {
        // This will activate the closest `error.js` Error Boundary
        throw new Error('Failed to fetch data')
    }

    return res.json()
}

export default async function Page() {
    const data = await getData()

    return <main></main>
}
```