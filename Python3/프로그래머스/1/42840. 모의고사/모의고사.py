def solution(answers):
    scores = [0,0,0]
    
    answer_2_hash = {1 : 1, 3: 3, 5: 4, 7:5}
    answer_3_hash = {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}
    
    for i in range(0, len(answers)):
        if (i % 5) + 1 == answers[i] :
            scores[0] += 1
        if i % 2 == 0 and answers[i] == 2:
            scores[1] += 1
        if i % 2 != 0 and answer_2_hash[i%8] == answers[i]:
            scores[1] += 1
        if answer_3_hash[i%10] == answers[i]:
            scores[2] += 1
            
    max_score = max(scores)
    answer = []
    for i in range(0, 3):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer