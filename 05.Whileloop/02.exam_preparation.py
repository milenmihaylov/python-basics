import statistics

failed_threshold = int(input())
score_list = []
failed_scores = 0
last_problem = ''

problem = input()
while not problem == "Enough":
    score = int(input())
    score_list.append(score)
    last_problem = problem
    if score <= 4:
        failed_scores += 1
        if failed_scores == failed_threshold:
            print(f"You need a break, {failed_scores} poor grades.")
            break
    problem = input()

average_score = statistics.mean(score_list)
scores_count = len(score_list)
if problem == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {scores_count}")
    print(f"Last problem: {last_problem}")
