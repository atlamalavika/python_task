marks_of_student=int(input("enter value: "))
if (marks_of_student==35):
    print("Border pass")
elif (marks_of_student>35 and marks_of_student<=100):
    print("pass")
elif(marks_of_student>100):
    print("Invalid data")
else:
    print("Fail")