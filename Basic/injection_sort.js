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