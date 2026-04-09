# Q.3 WAP to convert given character from upper to lower without function

# 1. Upper to Lower 📌

char = "A"
print(char)  # A

value = ord(char) + 32  # 97

char1 = chr(value)
print(char1)  # a



print('=='* 32)
# 2. Lower to Upper 📌

char = 'a'
print(char)  # a

value = ord(char) - 32  # 65

char1 = chr(value)
print(char1)  # A




print('=='* 32)
# 3. number to ACII value 📌

value = 65
print(value) # 65

char = chr(value)

print(char)  # A