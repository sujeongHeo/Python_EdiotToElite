// https://www.hackerrank.com/challenges/30-operators/problem?h_r=email&unlock_token=ab03c25b29310f011d83d172b21509fc23279549&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder
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

// Complete the solve function below.
function solve(meal_cost, tip_percent, tax_percent) {
    let result = 0;
    result = meal_cost + (tip_percent*meal_cost * 0.01) + ( meal_cost *tax_percent * 0.01);
    console.log(Math.round(result))
    result = Math.round(result)
    return result;

}

function main() {
    const meal_cost = parseFloat(readLine());

    const tip_percent = parseInt(readLine(), 10);

    const tax_percent = parseInt(readLine(), 10);

    solve(meal_cost, tip_percent, tax_percent);
}
