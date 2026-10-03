class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dic = defaultdict(int)
        for num in nums:
            nums_dic[num] += 1
        heap = []
        for num in nums_dic:
            heapq.heappush(heap, (nums_dic[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for i in range (k):
            ans.append(heap[i][1])
        return ans 