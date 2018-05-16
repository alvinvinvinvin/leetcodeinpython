class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        for h, k in sorted(people, key=lambda p: -1100*p[0]+p[1]):
            print("h:",h,"k:",k)
            q.insert(k, (h, k))
        return q

arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
a = Solution()
a.reconstructQueue(arr)