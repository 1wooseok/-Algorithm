// 비교한 값이 크면 index를 오른쪽으로 이동시키는걸 반복

export default function injection_sort(arr) {
  for(let i=1; i<arr.length; i++) {
    const key = arr[i];
    while (1 <= i && arr[i-1] > key) {
      arr[i] = arr[i-1];
      i--;
    }
    arr[i] = key;
  }
  return arr;
}