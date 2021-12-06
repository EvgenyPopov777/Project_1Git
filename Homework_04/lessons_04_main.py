def power_numbers(*numbers,cub=0):
    for num in numbers:
        if  num > 0:
            # s = s+num
            # k=k+1
            print(num,end=' в кубе = ')
            cub=num**3
            print(cub)
power_numbers(-3,1,2,3,4,5,0,6,-1)


