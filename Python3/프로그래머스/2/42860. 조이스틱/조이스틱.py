def solution(name):
    answer = 0
    # 위아래 
    for letter in name:
        from_A = ord(letter) - ord('A')
        from_Z = ord('Z') - ord(letter) + 1
        answer += min(from_A, from_Z)
        
    # 좌우
    ## 1. 기본 ( 오른쪽으로 쭉 )
    
    ## A 가 연달아서 나온다면 일단 몇개 나오는지 알아야겠지
    ## A 가 연달아서 여러번 나올 수도 있음
    ## 근데 결국에는 A 뭉치가 끝나는 부분이 중요한거잖아? 거기까지 갔다가 돌아오거나, 아예 거꾸로 가서 거기서 멈추거나
    ## 최소값을 계속 업데이트하면서 제일 작은거 발견하면 그걸로 갈아탄다는 느낌
    
    N = len(name)
    ## 1. 오른쪽으로 쭉 가는 경우
    min_move = N - 1
    for i in range(N):
        next_idx = i + 1
        if next_idx < N and name[next_idx] != 'A':
            continue
        while next_idx < N and name[next_idx] == 'A':
            next_idx += 1
    ## 2. 오른쪽으로 갔다가 되돌아가서 남은 구간을 가는 경우
        distance1 = i + i + (N-next_idx)
    ## 3. 왼쪽으로 갔다가 되돌아가서 남은 구간 가기 
        distance2 = (N-next_idx)*2 + i
        min_move = min(min_move, distance1, distance2)
    
    return answer + min_move
    
    