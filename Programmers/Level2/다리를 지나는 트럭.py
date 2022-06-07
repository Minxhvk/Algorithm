from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while len(truck_on_bridge):
        answer += 1
        bridge_weight -= truck_on_bridge.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                buffer = truck_weights.popleft()
                bridge_weight += buffer
                truck_on_bridge.append(buffer)
            else:
                truck_on_bridge.append(0)
    return answer
