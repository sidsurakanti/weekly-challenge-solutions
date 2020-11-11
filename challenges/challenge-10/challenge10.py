from inspect import getsource as gs


# solution
solution=lambda k:(1,-1)[k%2]*(k*k+k)//2

print(gs(solution))
