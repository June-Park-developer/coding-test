function solution(orders, course) {
  const answer = [];
  const ordersArray = orders.map((order) => order.split(``));
  for (let i = 0; i < course.length; i++) {
    const n = course[i];
    const hash = {};
    for (let j = 0; j < orders.length; j++) {
      const order = ordersArray[j];
      if (order.length >= n) {
        const keys = getCombosByLength(order, n);
        for (let key of keys) {
          if (!hash[key]) {
            hash[key] = 0;
          }
          hash[key]++;
        }
      }
    }
    const entries = Object.entries(hash);
    const maxCount = Math.max(...entries.map(([_, count]) => count));
    const maxKeys = entries
      .filter(([_, count]) => count === maxCount && count >= 2)
      .map(([key, _]) => key);
    answer.push(...maxKeys);
  }
  answer.sort();
  return answer;
}


function getCombosByLength(array, length) {
  const result = [];
  array.sort();

  function dfs(index, path) {
    if (path.length === length) {
      const combo = path.join(``);
      result.push(combo);
      return;
    }

    for (let i = index; i < array.length; i++) {
      dfs(i + 1, [...path, array[i]]);
    }
  }

  dfs(0, []);
  return result;
}