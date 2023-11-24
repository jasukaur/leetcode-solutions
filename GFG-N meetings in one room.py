#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        ct = 1
        s = 1
        e = 0
        
        combined = list(zip(end, start))

        # Sort the combined list based on the elements from list 'b'
        sorted_combined = sorted(combined, key=lambda x: x[0])
        
        # Extract the sorted elements from both lists 'a' and 'b'
        end, start = zip(*sorted_combined)
        
        while s<len(start):
            if end[e] < start[s]:
                ct +=1
                
                s+=1
                e = s-1
            else:
                s+=1
        
        return ct


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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends