'''Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*********
 *******
  *****
   ***
    *
Print the pattern in the function given to you.'''
n=int(input("enter n"))
if 1<=n<=100:
    i=1
    for i in range(n,0,-1):
            print( " "*(n-i)  + "*"*(2*i-1) )