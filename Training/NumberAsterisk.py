'''

Input: 5

Output:
*
* *
* 1 *
* 2 3 *
* 4 5 6 *
* 7 8 *
* 9 *
* *
*

'''


n=5
k=1
for i in range(n+n):
    if(i<n):
        for j in range(i+1):
            if(j==0 or j==i):
                print("*",end=" ")
            else:
                print(k,end=" ")
                k+=1 
        print()
    else:
        for j in range(n-(i-n)-2,-1,-1):
            if(j==0 or j==n-(i-n)-2):
                print("*",end=" ")
            else:
                print(k,end=" ")
                k+=1 
        print()

# for i in range(n-2,-1,-1):
#     for j in range(i+1):
#         if(j==0 or j==i):
#             print("*",end=" ")
#         else:
#             print(k,end=" ")
#             k+=1 
#     print()
