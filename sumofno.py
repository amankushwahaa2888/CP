#sum of digits
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num=num//10
print("Sum of digits:", sum)
