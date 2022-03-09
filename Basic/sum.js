// 분할 정복을 이용한 배열 요소 합
export default function regression_sum(arr) {
  if(arr.length === 0) {
    return 0;
  }
  return arr[0] + regression_sum(arr.filter((x, idx) => idx > 0));
}
