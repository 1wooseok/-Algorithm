function solution(cacheSize, cities) {
  const cache = [];

  const HIT = 1;
  const MISS = 5;

  let result = 0;

  if (cacheSize === 0) {
    return cities.length * MISS;
  }

  for (let city of cities) {
    console.log(cache)
    city = city.toLowerCase();
    let flag = false;
    for (let i of cache) {
      const key = Object.keys(i);
      if (key === city) {
        result += HIT;
        cache[key]++;
        flag = true;
      }
    }
    if (!flag) {
      result += MISS;
      if (cache.length === cacheSize) {
        const least = getLeast(cache);
        cache.splice(least, 1)
      }
      let obj = {}
      obj[city] = 1;
      cache.push(obj)
    }
  }

  return result;
}

function getLeast(list) {
  let least = 9999999999;
  let result;

  for (let i = 0; i < list.length; i++) {
    let x = Object.keys(list[i])[0];
    if (list[x] < result) {
      least = list[x];
      result = i;
    }
  }

  return result;
}