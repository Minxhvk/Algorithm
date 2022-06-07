from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_bridge = [0] * bridge_length
    truck_weights = truck_weights

    while len(truck_on_bridge):
        answer += 1
        truck_on_bridge.pop(0)
        if truck_weights:
            if sum(truck_on_bridge) + truck_weights[0] <= weight:
                truck_on_bridge.append(truck_weights.pop(0))
            else:
                truck_on_bridge.append(0)

    return answer
