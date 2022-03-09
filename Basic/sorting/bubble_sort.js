// 한 사이클마다 오른쪽에 가장 큰 값이 배치됨.

export default function bubble_sort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; (j < arr.length - i - 1); j++) {
      if (arr[j] > arr[j + 1]) {
        let tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
      }
    }
  }
  return arr;
}
