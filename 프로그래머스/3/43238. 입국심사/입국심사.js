function solution(n, times) {
    let answer = 0;
    
    const maxTime = Math.max(...times);
    console.log(maxTime);
    
    let min = 1;
    let max = n * maxTime;
    
    while (min <= max) {
        const midTime = Math.floor((min + max) / 2);
        let total = 0;
        for (let time of times) {
            total += Math.floor(midTime / time);
        }
        if (total >= n) {
            answer = midTime;
            max = midTime-1;
        } else if (total  < n) {
            min = midTime+1;
        } 
        
    }
    return answer;
}