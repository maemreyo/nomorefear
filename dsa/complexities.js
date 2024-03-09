// VD1
console.log("Hello World")
// => Time complexity: O(1)

// VD2
let i, n1 = 8;
for (i = 1; i <= n1; i++) {
    console.log("Hello World !!!");
}
// => Time complexity: O(n)


// VD3
for (i = 1; i <= 8; i = i * 2) {
    console.log("Hello World !!!");
}
// => Time complexity: O(log(n))

// VD4
function sum(a, b) {
    return a + b; // 1 for arithmetic operations + 1 for return => O(2) = O(1) since 2 is constant
}

let a = 5, b = 6;
console.log(sum(a, b));
// => Time complexity: O(1)

// VD5
let n = 3;
let m = 3;
let arr = [[3, 2, 7], [2, 6, 8], [5, 1, 9]];
let sum = 0;

// Iterating over all 1-D arrays in 2-D array
for (let i = 0; i < n; i++) {
    // Printing all elements in ith 1-D array
    for (let j = 0; j < m; j++) {

        // Printing jth element of ith row
        sum += arr[i][j];
    }
}
console.log(sum);
// => Time complexity: O(n*m)