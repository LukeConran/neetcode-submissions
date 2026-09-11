class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = (target - position) / speed
        # I guess we just sort, iterate down and see if the car behind time is <= time ahead, and if it is set it equal to teh same time. We then append it to a stack? and we could do popall next time something doesn't catch up to that fleet?

        times = [(target - pos) / spd for pos, spd in zip(position, speed)]
        # print(times)
        _, sorted_tms = map(list, zip(*sorted(zip(position, times))))
        # print(sorted_tms)
        sorted_tms_bw = sorted_tms[::-1]
        # print(sorted_tms_bw)

        fleet_stack = [sorted_tms_bw[0]]
        count = 0
        for i in range(1, len(sorted_tms_bw)):
            if sorted_tms_bw[i] <= fleet_stack[-1]:
                fleet_stack.append(fleet_stack[-1])
            else:
                fleet_stack = []
                count += 1
                fleet_stack.append(sorted_tms_bw[i])

        if fleet_stack:
            count += 1
        return count

