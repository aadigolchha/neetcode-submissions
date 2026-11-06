class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        cars = {}
        for i in range(len(position)):
            cars[position[i]] = speed[i]

        position.sort()
        fleets = 0
        slowest = 0
        for i in range(len(position) - 1, -1, -1):
            time = (target - position[i]) / cars[position[i]]
            if  time > slowest:
                slowest = time
                fleets += 1
                

        return fleets




