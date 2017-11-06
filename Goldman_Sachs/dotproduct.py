def dotproduct(a, b):
    product = 0
    for (i ,j) in zip(a, b):
        product += i * j
    return (product)

a = [1,2,3,4,5,6]
b = [11,12,13,14,15,16]
print(dotproduct(a,b))
