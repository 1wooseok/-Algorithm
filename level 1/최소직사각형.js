function solution(sizes) {
    //-> 큰거는 큰것끼리, 작은거는 작은것끼리 모아서 각각 최대값 반환
    const greater = [];
    const smaller = [];
    
    for (let i=0; i<sizes.length; i++) {
        let w = sizes[i][0];
        let h = sizes[i][1]; 
        if(w < h) {
            greater.push(h);
            smaller.push(w)
        } else {
            greater.push(w);
            smaller.push(h)
        } 
    }
    return Math.max(...greater) * Math.max(...smaller)
}