'''

    Python Task

'''

# for i in range(5):
#     print(i*"*")

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(end="*")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if(i==j or i+j==6):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(5):
#     for j in range(5):
#         print((i+j)%2,end="")
#     print()

# Rombus
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,6):
#         print("*",end="")
#     print()

#Traingle
# for i in range(1,6):
#     for j in range(0,5-i):
#         print(" ",end="")
#     for j in range(0,2*i-1):
#         print("*",end="")
#     print()
    
#Traingle Inverted
for i in range(6,0,-1):
    for j in range(0,5-i+1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()



