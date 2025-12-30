def solution(bridge_length, weight, truck_weights):
    bridge = [0 for i in range(0, bridge_length)]
    t = 0
    total = 0
    while len(truck_weights) > 0 or total > 0 :
        t += 1
        passed = bridge.pop(0)
        total -= passed
        if truck_weights and total + truck_weights[0] <= weight:
            new = truck_weights[0]
            bridge.append(new)
            total += new
            truck_weights.pop(0)
        else:
            bridge.append(0)
        
    return t
            
        