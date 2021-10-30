<!-- This file has been fixed by shradha on branch feature1 -->

rollno = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
gender = input("Enter Gender: ")
standard = int(input("Enter Class: "))
english = int(input("Enter English Marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
maths = int(input("Enter Maths marks: "))
hindi = int(input("Enter Hindi marks: "))
obtained_marks = english + physics + chemistry + maths + hindi
percentage = obtained_marks / 500 * 100
print(percentage)

print("=================STUDENT'S MARKSHEET===================")
print("Your Roll is: " + str(rollno))
print("Your Name is: " + name)
print("Your Gender is: " + gender)
print("Your Class is: " + str(standard))
print("Total Marks are: 500 ")
print("Obtained Marks are:" + str(obtained_marks))
print("Your Percentage is: " + str(percentage))

if percentage >= 90:
    print("Grade: A+")
    print("Remarks: Very Excellent")
elif percentage >= 80:
    print("Grade: A")
    print("Remarks: Excellent")
elif percentage >= 70:
    print("Grade: B+")
    print("Remarks: Very Good")
elif percentage >=60:
    print("Grade: B")
    print("Remarks: Good")
elif percentage >= 50:
    print("Grade: C")
    print("Remarks: Fair"
elif percentage >= 40:
    print("Grade: D")
    print("Remarks: Poor")
elif percentage >= 33:
    print("Grade: E")
    print("Remarks: Need Improvement")
else:
    print("Grade: F (Fail)")
    print("Remarks: Failure")

i = 0
subjects_name = " "

if english < 33:
    i = i + 1
    subjects_name += "English "
if physics < 33:
    i = i + 1
    subjects_name += "Physics "
if chemistry < 33:
    i = i + 1
    subjects_name += "Chemistry "
if maths < 33:
    i = i + 1
    subjects_name += "Maths "
if hindi < 33:
    i = i + 1
    subjects_name += "Hindi "
    
print("Failed Subjects Count: " + str(i))
print("Failed Subjects Name: " + subjects_name)
