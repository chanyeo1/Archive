// https://www.altcademy.com/blog/how-to-get-user-input-in-javascript/
// https://stackoverflow.com/questions/61394928/get-user-input-through-node-js-console
// https://www.acmicpc.net/problem/2750
const prompt = require('prompt-sync')();

// 5, 2, 3, 4, 1 cursor=0 5,2 비교
// 2, 5, 3, 4, 1 cursor=1 5,3 비교
// 2, 3, 5, 4, 1 cursor=2 5,4 비교
// 2, 3, 4, 5, 1 cursor=3 5,1 비교

// 2, 3, 4, 1, 5 cursor=0 2,3 비교
// 2, 3, 4, 1, 5 cursor=1 3,4 비교
// 2, 3, 4, 1, 5 cursor=2 4,1 비교

// 2, 3, 1, 4, 5 cursor=0 2,3 비교
// 2, 3, 1, 4, 5 cursor=1 3,1 비교

// 2, 1, 3, 4, 5 cursor=0 2,1 비교

// 1, 2, 3, 4, 5

const NUMBER_COUNT = prompt('')

const arr = [];
for(let i = 0; i < NUMBER_COUNT; i++) {
    const num = prompt('')
    arr.push(num)
}

for(let i = 0; i < (arr.length - 1); i++) {
    // moving cursor
    for(let j = 0; j < (arr.length - (i + 1)); j++) {
        if(arr[j] > arr[j+1]) {
            const temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
        }
    }
}

console.log(arr)