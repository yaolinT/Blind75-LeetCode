# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome 
# when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
###############################################################
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right 
# and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. 
# From right to left, it becomes 121-. 
# Therefore it is not a palindrome.

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. 
# Therefore it is not a palindrome.
###############################################################

# approach 1
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
def isPalindrome(x):
    # x = [int(a) for a in str(x)]
    
    #less then one
    if x<0:
        return False
    # num to list
    y=[]
    for i in str(x):
        x=int(i)
        # print(x)
        y.append(x)
    print(y)
#when x lenth is even        
    if len(y)%2==0:
        z=int(len(y)/2)
        print(z)
        for i in range(z):
            # i=i+1
            print(i)
            I=(len(y)-1)-i
            print(I)
            if y[i] != y[I]:
                print(y[i])
                print(y[I])
                print("false")
                return False
            else:
                print(y[i])
                print(y[I])
                print("true")
        return True
#when x lenth is odd               
    else:                
        z=int(len(y)/2-0.5)
        print(z)
        for i in range(z):
            i=i+1
            print(i)
            if y[z-i] != y[z+i]:
                print(y[z-i])
                print(y[z+i])
                print("false")
                return False
            else:
                print(y[z-i])
                print(y[z+i])
                print("true")
        return True
        
## Driver code
if __name__=='__main__':
	x = 121
	print(isPalindrome(x))
        