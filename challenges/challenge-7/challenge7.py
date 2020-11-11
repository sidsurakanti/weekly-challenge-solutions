# solution
def solution(t):
    t, c = t.split(), {}
    for w in t:
        c[w] = (c[w] + 1 if w in c else 1)
    d = [k for k, v in sorted(c.items(), key=lambda d: d[1])[::-1]]
    return " ".join(str(d.index(i) + 1) for i in t)
