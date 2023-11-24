#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
    
        # Initialize platforms needed and result
        platforms_needed = 1
        result = 1
    
        # Iterate through arrival and departure times
        i = 1
        j = 0
        
        
    
        while i < n and j < n:
            # If a train is arriving before the previous one departs, a new platform is needed
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
    
                # Update the result if the current platforms_needed is greater
                result = max(result, platforms_needed)
            else:
                # If a train is departing, free up a platform
                platforms_needed -= 1
                j += 1
    
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends