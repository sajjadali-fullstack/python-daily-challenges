# Q.1 WAP to Swap / interchange two float vaues from standard input

# 1 way 
num1 = float(input("Enter 1 value : "))
num2 = float(input("Enter 2 value : "))

print(f'Before swapping num1 : {num1} and num2 : {num2}')

num3 = num1
num1 = num2
num2 = num3

print(f'After Swapping num1 : {num1} and num2 : {num2}')


# 2 way 

a = float(input("Enter value 1 : "))
b = float(input("Enter value 2 :"))

print(f'Before Swapping A is : {a} and B is : {b}')

a, b = b, a

print(f'After Swapping A is : {a} and B is : {b}')