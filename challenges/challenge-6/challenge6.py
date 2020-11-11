from inspect import getsource as gs


# solution
def solution(value1, weight1, value2, weight2, max_weight):
    # if both weights combined are less than or equal to the max weight
    if max(weight1, weight2) <= max_weight:
        return value1 + value2 if weight1 + weight2 <= max_weight else max(value1, value2)

    # if both weights are bigger than the max weight
    elif min(weight1, weight2) > max_weight:
        return 0

    # if only one weight is smaller than the max weight
    else:
        return value1 if weight1 <= max_weight <= weight2 else value2


print(len(gs(solution)))
