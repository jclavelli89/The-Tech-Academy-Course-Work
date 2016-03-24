def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
        firstn(19)
        print(num)


    
sum_of_first_n = sum(firstn(1000000))
