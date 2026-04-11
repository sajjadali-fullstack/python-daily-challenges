# WAP to input rollno, name, 3 subject of  marks. Calculate total & avg marks.


name = input("Enter Name : ")
rollno = int(input("Enter Rollno : "))
subject1 = int(input("Enter Subject 1 marks : "))
subject2 = int(input("Enter Subject 2 marks : "))
subject3 = int(input("Enter Subject 3 marks : "))

total = subject1 + subject2 + subject3
average = total / 3

print(f"""
---------------------------------
        STUDENT REPORT 
---------------------------------
Name of the student is : {name}
Rollno : {rollno}
---------------------------------
Subject 1 Marks : {subject1}
Subject 2 Marks : {subject2}
Subject 3 Marks : {subject3}
---------------------------------
total of 3 is : {total}
Average is : {average:.2f}
---------------------------------
""")