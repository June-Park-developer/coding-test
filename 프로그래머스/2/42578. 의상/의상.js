function solution(clothes) {
    const categorized = {};
    const N = clothes.length;
    const categories = [];
    for (let i = 0; i < N; i++){
        const pair = clothes[i];
        const category = pair[1];
        const cloth = pair[0];
        if (!categorized[category]){
            categorized[category] = 0;
        }
        categorized[category]++;
        if (!categories.includes(category))
        categories.push(category);
    }
    let answer = 1;
    for (category of categories){
        answer = answer * (categorized[category] + 1);
    }
    return answer - 1;
    
}