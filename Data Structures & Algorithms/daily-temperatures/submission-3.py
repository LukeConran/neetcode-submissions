class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        temps = temperatures[::-1]
        for i in range(len(temps)):
            # print(f"i = {i}, stack before operation:")
            # print(stack)
            emptied = False
            if i == 0:
                stack.append((temps[i], i))
                # print(f"stack after operation:")
                # print(stack)
                # print()
                continue
            while temps[i] >= stack[-1][0]:
                stack.pop()
                if len(stack) == 0:
                    res[i] = 0
                    emptied = True
                    stack.append((temps[i], i))
                    break
            if not emptied:
                res[i] = i - stack[-1][1]
                stack.append((temps[i], i))
            # print(f"stack after operation:")
            # print(stack)
            # print()

        return res[::-1]