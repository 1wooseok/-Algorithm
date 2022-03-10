// 한 사이클마다 탐색 범위 절반씩 줄어듬
function binary_search(arr, target) {
  let start = 0;
  let end = arr.length;

  while (start <= end) {
    let mid = Math.floor((end + start) / 2);
    if (arr[mid] === target) {
      return arr[mid];
    } else if (arr[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return false;
}