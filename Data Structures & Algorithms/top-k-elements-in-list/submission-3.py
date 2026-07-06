class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
        

        freqs = sorted(counter.values())
        freq_pointer = len(freqs)

        count = 1
        out = []
        for key, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            if count > k:
                break
            out.append(key)
            count += 1
        return out
