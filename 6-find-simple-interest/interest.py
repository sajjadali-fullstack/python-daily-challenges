# WAP to find Simple Interest

price = float(input("Enter Amount : "))
time = int(input("Enter Time : "))
rate = float(input("Enter Rate : "))

simple_interest = price * time * rate / 100  # Formula

print(f'Amount : {price} Time {time} Rate : {rate} Simple Interest {simple_interest:.2f}')
