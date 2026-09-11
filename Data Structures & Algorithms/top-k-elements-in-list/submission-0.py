class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        new_d = {}
        answer = []
        i = 0

        for num in nums:
            d[num] = 1 + d.get(num, 0)

        for key,v in d.items():
            new_d.setdefault(v, []).append(key)

        while i < k:
            max_k = max(new_d)
            val_list = new_d.pop(max_k)
            for j in range(min(k-i, len(val_list))):
                answer.append(val_list[j])
                i += 1
            
        return answer