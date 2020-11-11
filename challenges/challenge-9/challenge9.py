from inspect import getsource as gs


# solution
def solution(a): b, c, d, e = map(a.count,"ewns"); return b ^ c < (c+d < 6) > d ^ e


print(gs(solution))
