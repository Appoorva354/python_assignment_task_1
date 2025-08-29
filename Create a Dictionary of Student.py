students_marks={
    "Alice": 85,
    "Bob": 78,
    "Charlie" : 92,
    "David" : 67
}
name= input("Enter the student's name: ")
if name in students_marks:
    print(f"{name}'s marks: {students_marks[name]}")
else:
    print("student doesn't exist")