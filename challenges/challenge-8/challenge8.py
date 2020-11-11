from inspect import getsource as gs


# solution
solution=lambda n:n % 2*[28,30]+[31]


print(gs(solution))
