'''
1005. Maximize Sum Of Array After K Negations
https://leetcode.com/contest/weekly-contest-127/problems/maximize-sum-of-array-after-k-negations/
'''

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        count = 0;
        my_list = A
        new_list = []
        j = 0
        
        for index, item in enumerate(my_list):
            print(index, item)
            if j < K:
                smallest = min(my_list)
                #my_list.remove(smallest)
                print("smallest = "+str(smallest))
                smallest *= -1
                print("smallest = "+str(smallest))
                new_list.append(smallest)
                j += 1
            else:
                new_list.append(item)  
        print("new_list = "+str(new_list))
        print("sum(new_list) = "+str(sum(new_list)))
        return sum(new_list) 

'''

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heapq.heapify(A)
        for i in range(K):
            p = heapq.heappop(A)
            if p == 0:
                break
            heapq.heappush(A, -p)
        return sum(A)

for i in range(K):
    f=min(A)
    A[A.index(f)]= -A[A.index(f)]
return sum(A)


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = []
        o = ['*', '//', '+', '-']
        k = 0
        for i in range(N, 0, -1):
            s.append(str(i))
            s.append(o[k])
            k = (k + 1) % 4
        s.pop()
        return eval(''.join(s))



class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = a + b
        m = c.most_common(1)[0]
        if m[1] < n:
            return -1
        cand = m[0]
        ac, bc = 0, 0
        for i in range(n):
            if cand != A[i]:
                if cand != B[i]:
                    return -1
                ac += 1
            elif cand != B[i]:
                bc += 1
        return min(ac, bc)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, p):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not p:
            return None
        ret = TreeNode(p[0])
        i = 1
        while i < len(p) and p[i] < p[0]:
            i += 1
        ret.left = self.bstFromPreorder(p[1 : i])
        ret.right = self.bstFromPreorder(p[i : ])
        return ret
'''