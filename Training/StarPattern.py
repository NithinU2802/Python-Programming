'''

Input:
water

Output:
w w w
 aaa 
water  
 eee 
r r r 

'''

# s=input()
# n=len(s)
# k=0
# for i in range(n):
#     for j in range(n):
#         if(i==n//2):
#             for l in range(n):
#                 print(s[l],end=" ")
#             break;
#         if (j==n//2 or i==j or j==n-i-1):
#             print(s[k],end=" ")
#         else:
#             print(" ",end=" ")
#     k+=1
#     print()
    
s=input()
n=len(s)
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1 or n//2==j):
            print(s[i],end=" ")
        elif n//2==i:
            print(s[j],end=" ")
        else:
            print(" ",end=" ")
    print()
