
numbers = [5,2,1,8,-3,13,24,25,64,24,12,12,11]
# numbers = ["banana", "apple", "strawberry"]
# numbers.sort()
print(numbers)

j=1
for _ in range(len(numbers)-1):
    swapped = False
    i = 0

    while i < len(numbers)-j:
        
        num1 = numbers[i]
        num2 = numbers[i+1]

        if num1 > num2:
            numbers[i] = num2
            numbers[i+1] = num1
            swapped = True    
        i+=1

    if not swapped:
        break   
    j+=1
    print(numbers)    

