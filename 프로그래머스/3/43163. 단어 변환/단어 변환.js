function solution(begin, target, words) {
    if (!words.includes(target)) {
        return 0;
    }
    
    console.log("target 이 words 에 있긴 해요~! ");
    
    const wordLength = begin.length;
    const nodes = [begin, ...words];
    console.log(`wordLength = ${wordLength}, nodes = ${nodes}`);
    // (1) 인접리스트 생성
    const adjList = {};
    
    for (let i = 0; i < nodes.length; i++){
        for (let j = 0; j <nodes.length; j++){
            let diff = 0;
            const currentNode = nodes[i];
            const comparedNode = nodes[j];
            for(let k = 0; k < wordLength; k++){
                if (currentNode[k] !== comparedNode[k]){
                    diff++;
                }
            }
            if (diff === 1) {
                if (!adjList[currentNode]) {
                    adjList[currentNode] = [];
                    }
                adjList[currentNode].push(comparedNode);
            }
        }
        
    }
    console.log(`adjList 는`, adjList);
    
    // (2) 최단거리 업데이트 하기
    const visited = [];
    const distances = {};
    let round = 1;
    const updated = [];
    
    // 2-1) 최단거리 초기화 (시작만 0, 나머지는 Infinity)
    for (let node of nodes) {
        distances[node] = Infinity;
    }
    distances[begin] = 0;
    
    // 2-2) 방문 함수
    function visit(node){
        if (visited.length === nodes.length){
            return;
        }
        visited.push(node);
        const adjNodes = adjList[node];
        for (let adjNode of adjNodes) {
            if (visited.includes(adjNode)){
                continue;
            }
            if (distances[adjNode] > round){
                distances[adjNode] = round;
                updated.push(adjNode);
            }
        }
        round++;
        
        while(updated.length > 0) {
            const newNode = updated.pop();
            visit (newNode);
        }
    }
    
    visit(begin);
    
    console.log(`visited: `, visited);
    console.log(`distance: `, distances);
    
    if (distances[target] === Infinity) {
        return 0;
    }
    return distances[target];

    
    
}