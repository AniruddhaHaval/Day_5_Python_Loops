student_heights = [150, 120, 100, 150]

no_of_students = len(student_heights)

print(no_of_students)

total_height = 0

for height in student_heights:
    total_height += height

print(f"Average height is {total_height/no_of_students}")