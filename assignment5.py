name = input("Enter the student's name:")
dictionary= {"Alice":85, "Tom":66, "David":99}
if name in dictionary:
    print(f"{name} marks: {dictionary[name]}")
else:
    print("student not found")