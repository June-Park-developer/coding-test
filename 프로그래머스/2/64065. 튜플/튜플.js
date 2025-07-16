function solution(s) {
    const answer = [];
    const N = s.length;
    
    
    const sets = s.slice(2, N-2).split(`},{`);
   
    sets.sort((a,b)=> a.length - b.length);
    console.log(sets);
    const sets2 = sets.map((set) => set.split(','));
    // console.log(sets2);
    
    for (let i = 0; i < sets2.length; i++){
        const out = [`{`, `}`, `,`];
        const set = sets2[i];
        sets2[i] = set.filter((letter) => !out.includes(letter));
    }
    // console.log(sets2);
    
    sets2.sort((a,b) => a.length - b.length);
    // console.log(sets2);
    
    for (let i =0; i < sets2.length; i++){
        const set = sets2[i];
        for (let j = 0; j < set.length; j++){
            const number = parseInt(set[j]);
            if (!answer.includes(number)){
                answer.push(number);
            }
        }
    }
    return answer;
    
}