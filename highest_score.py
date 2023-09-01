student_score = [120, 50, 25, 30, 400, 45, 10]

highest_score = 0

for score in student_score:
    if score > highest_score:
        highest_score = score

min_score = highest_score
for score in student_score:
    if score < min_score:
        min_score = score

print(highest_score)
print(min_score)

print(max(student_score))
print(min(student_score))

