export default function quick_sort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = Math.floor(arr.length/2);
  const lesser = [];
  const greater = [];

  for (let i = 0; i < pivot; i++) {
    arr[i] > arr[pivot] ? greater.push(arr[i]) : lesser.push(arr[i]);
  }
  for (let i = pivot+1; i < arr.length; i++) {
    arr[i] > arr[pivot] ? greater.push(arr[i]) : lesser.push(arr[i]);
  }

  return quick_sort(lesser).concat(arr[pivot], quick_sort(greater));
}
