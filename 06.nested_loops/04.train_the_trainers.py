from statistics import mean

assessments_number = int(input())
presentation_title = input()
presentation_scores = []

while presentation_title != 'Finish':
    grades_list = []

    for grades in range(assessments_number):
        grade = float(input())
        grades_list.append(grade)

    current_ave_score = mean(grades_list)
    presentation_scores.append(current_ave_score)
    print(f"{presentation_title} - {current_ave_score:.2f}.")

    presentation_title = input()
    if presentation_title == 'Finish':
        break

student_assessment = mean(presentation_scores)
print(f"Student's final assessment is {student_assessment:.2f}.")
