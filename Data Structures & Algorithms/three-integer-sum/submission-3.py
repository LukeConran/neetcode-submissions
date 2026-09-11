class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)
        ls = []

        for i, num in enumerate(ns):
            if num > 0: #can break if we go past 0 cause impossbile for sum then
                break
            if i > 0 and num == ns[i - 1]: #don't recheck duplicate numbers
                continue

            l, r = i+1, len(ns) - 1
            while l < r:
                sol = num + ns[l] + ns[r]
                if sol > 0:
                    r -= 1
                elif sol < 0:
                    l += 1
                else:
                    ls.append([num, ns[l], ns[r]])
                    l += 1
                    r -= 1
                    while ns[l] == ns[l-1] and l < r: #again, dont recheck dupes
                        l +=1
        return ls