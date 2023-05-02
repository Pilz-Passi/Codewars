def positive_sum(arr):
    result = 0
    for number in arr:
        if number >= 0:
            result += number
    return result

result = positive_sum([1,-4,7,12])
print(result)
result = positive_sum([1,2,3,4,5])
print(result)
result = positive_sum([1,-2,3,4,5])
print(result)
result = positive_sum([-1,2,3,4,-5])
print(result)