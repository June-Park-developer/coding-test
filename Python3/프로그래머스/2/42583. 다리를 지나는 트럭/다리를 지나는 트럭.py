from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     # 초기화 (다리, 시간, total 무게)
#     bridge = [0 for i in range(0, bridge_length)]
#     t = 0
#     total_weight = 0
    
#     # truck_weights 가 빌때까지
#     # 시간 +1 되면서, 일단 하나는 다리에서 빠지며 무게 감소
#     # 다음꺼 비교해서 무게가 되면 트럭에서 빼고 다리에 추가하고 토탈무게 증가
#     # 무게가 초과하면 0 을 추가하기만
#     while len(truck_weights) > 0:
#         t += 1
#         passed = bridge.pop(0)
#         total_weight -= passed
        
#         new = truck_weights[0]
#         if (total_weight + new <= weight):
#             truck_weights.pop(0)
#             bridge.append(new)
#             total_weight += new
#         else:
#             bridge.append(0)
    
#     return t + bridge_length
    
    
        
# deque 를 사용한 풀이도 해볼 것
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for i in range(0, bridge_length))
    weights = deque(truck_weights)
    t = 0
    total_weight = 0
    
    while weights :
        t += 1
        passed = bridge.popleft()
        total_weight -= passed
        
        new = weights[0]
        
        if  (total_weight + new ) <= weight:
            bridge.append(new)
            weights.popleft()
            total_weight += new
            
        else:
            bridge.append(0)
    
    return t + bridge_length




# 문제의 핵심 로직
## bridge 를 큐로 두고 다리 위에 올라가고, 다리에서 빠져나가고를 실제로 굴림
        