from typing import List

def minTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    robot.sort()
    factory.sort()
    
    def distance(x: int, y: int) -> int:
        return abs(y - x)
    
    def repair(robot_pos: int, factory_pos: int, limit: int) -> int:
        repair_count = min(limit, abs(robot_pos - factory_pos))
        return repair_count * distance(robot_pos, factory_pos)
    
    total_distance = 0
    for r in robot:
        min_dist = float('inf')
        for f in factory:
            dist = repair(r, f[0], f[1])
            min_dist = min(min_dist, dist)
        total_distance += min_dist
    
    return total_distance

robot = [0, 4, 6]
factory = [[2, 2], [6, 2]]
print(minTotalDistance(robot, factory))  