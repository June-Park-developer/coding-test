def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# collections.Counter
## 이터러블을 넣으면 각 항목이 몇번 나왔는지를 세어주는 편리한 클래스
## 심지어 뺄셈, 덧셈도 가능하다!

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
