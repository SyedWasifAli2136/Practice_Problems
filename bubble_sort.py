numbers = [5,2,1,8,-3,13,24,25,64,24,12,12,11]

# numbers.sort()
print(numbers)

j=1
for _ in range(len(numbers)):

    i = 0

    while i < len(numbers)-j:
        
        num1 = numbers[i]
        num2 = numbers[i+1]

        if num1 > num2:
            numbers[i] = num2
            numbers[i+1] = num1
        i+=1
    j+=1
    print(numbers)    

