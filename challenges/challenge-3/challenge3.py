fill = lambda matrix:sum([obj for row in matrix for obj in row]) == 15

# should return False
print(fill([[0,0,0,0,1],
            [1,1,1,1,1],
            [0,0,0,0,0]]))

# should return True
print(fill([[1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]]))
