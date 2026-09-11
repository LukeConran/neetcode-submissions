class Solution:
    def isValid(self, s: str) -> bool:
        para_list = []
        para_dict = {'}':'{', ']':'[', ')':'('}
        if len(s) % 2 == 1: return False

        for char in s:
            if char in para_dict.values():
                para_list.append(char)
                print(para_list)
            elif len(para_list) == 0:
                return False
            else:
                if para_list[-1] != para_dict[char]:
                    return False
                para_list.pop()

        if len(para_list) == 0: return True
        return False