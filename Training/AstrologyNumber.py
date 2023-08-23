'''

Astrology Number

'''

# Method 1
# n=int(input())
# while(n//10!=0):
#     t=n 
#     s=0
#     while t>0:
#         s+=(t%10)
#         t//=10
#     n=s
# print(n)

""" Method 2 (refer)  """
n=int(input())
if(n%9==0):
    print("9")
else:
    print(n%9)

# Method 3
# n=int(input())
# s=0
# while(n>9):
#     s+=(n%9)
#     n//=10
# print(s)
    

# Method 4
# n = int(input()) 
# while n >= 10: 
#     n = sum(int(digit) for digit in str(n)) 
#     print(n)


