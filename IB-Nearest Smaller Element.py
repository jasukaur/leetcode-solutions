class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        S = list()
        res = []

        for i in range(len(A)): 
            while (len(S) > 0 and S[-1] >= A[i]):
                S.pop()
            
            if (len(S) == 0):
                res.append(-1)
            else:
                res.append(S[-1])

            S.append(A[i])

        return res
                
                
