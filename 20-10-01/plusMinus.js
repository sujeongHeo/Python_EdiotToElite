'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the plusMinus function below.
function plusMinus(arr) {
    
    let PlusPortion = 0,
        MinusPortion = 0,
        ZeroPortion = 0

    for (let i of arr) {
        if (i > 0){
            PlusPortion += 1;
        }
        else if ( i == 0 ){
            ZeroPortion += 1;
        }
        else {
            MinusPortion += 1;
        }
    }

    PlusPortion = PlusPortion / arr.length;
    MinusPortion = MinusPortion / arr.length;
    ZeroPortion = ZeroPortion / arr.length;
    console.log(PlusPortion.toFixed(6));
    console.log(MinusPortion.toFixed(6));
    console.log(ZeroPortion.toFixed(5));


}

function main() {
    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
