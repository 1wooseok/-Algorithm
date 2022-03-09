// 정렬되지 않은 배열중 최소값을 왼쪽에 배치시킴.

export default function selection_sort(arr) {
  for(let i=0; i<arr.length; i++) {
    let min = i;
    for(let j=i+1; j<arr.length; j++) {
      if(arr[j] < arr[min]) {
        min = j;
      }
    }
    let tmp = arr[i];
    arr[i] = arr[min];
    arr[min] = tmp;
  }
  return arr;
}