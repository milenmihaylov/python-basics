import statistics

student_name = input()
grades = []
failed = False
for grade in range(1, 13):
    score = float(input())
    if score < 4:
        grades.append(score)
        score = float(input())
        if score < 4:
            failed = True
            print(f"{student_name} has been excluded at {grade} grade")
            break
    else:
        grades.append(score)

if not failed:
    average_grade = statistics.mean(grades)
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
