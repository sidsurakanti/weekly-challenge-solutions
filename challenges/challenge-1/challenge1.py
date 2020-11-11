# short solution
lateRide1=lambda n:sum(map(int,f"{n//60}{n%60}"))


# readable solution
def lateRide2(num):
    hh, mm = num // 60, num % 60
    total = sum([int(i) for i in f"{hh}{mm}"])
    return total


cases = [240, 808, 290]
for case in cases:
    print(lateRide1(case))
    print(lateRide2(case))
