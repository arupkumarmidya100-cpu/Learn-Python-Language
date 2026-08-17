marks={}
n=int(input("Enter number of student:"))
for i in range(n):
    name=input("Enter student name:",)
    mark=int(input("Enter marks:"))
    marks[name]=mark
highest_student=max(marks,key=marks.get)
print("student with highest marks :",highest_student)
print("highest marks:",marks[highest_student])