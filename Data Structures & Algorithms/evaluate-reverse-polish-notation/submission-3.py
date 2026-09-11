class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        operands = set(['+', '-', '/', '*'])

        for i in range(len(tokens)):
            if tokens[i] not in operands:
                number_stack.append(int(tokens[i]))
            else:
                val2 = number_stack.pop()
                val1 = number_stack.pop()
                # print(f"{val1} {tokens[i]} {val2}")
                if tokens[i] == '+':
                    number_stack.append(val1 + val2)
                elif tokens[i] == '-':
                    number_stack.append(val1 - val2)
                elif tokens[i] == '*':
                    number_stack.append(val1 * val2)
                else:
                    number_stack.append(int(val1 / val2))

        return number_stack[0]