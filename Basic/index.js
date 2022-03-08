import selection_sort from "./selection_sort.js";
import bubble_sort from "./bubble_sort.js";
import injection_sort from "./injection_sort.js";
import quick_sort from "./quick_sort.js";

const testArr = [16,647,15,124,24,642,32,4,7,68,43];
const testArr2 = [16,647,15,124,24,642,32,4,7,68,43];
const testArr3 = [16,647,15,124,24,642,32,4,7,68,43];
const testArr4 = [16,647,15,124,24,642,32,4,7,68,43];

console.log('선택 정렬 : ' + selection_sort(testArr));
console.log('거품 정렬 : ' + bubble_sort(testArr2));
console.log('삽입 정렬 : ' + injection_sort(testArr3));
console.log('퀵 정렬 : ' + quick_sort(testArr4));