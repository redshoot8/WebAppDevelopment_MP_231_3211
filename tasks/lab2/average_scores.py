def compute_average_scores(scores):
    n = len(scores[0])
    x = len(scores)
    
    student_sums = [0.0] * n
    
    for subject_scores in scores:
        for i in range(n):
            student_sums[i] += subject_scores[i]
    
    averages = [round(total / x, 1) for total in student_sums]
    
    return tuple(averages)


if __name__ == '__main__':
    n, x = map(int, input().split())

    scores = []
    for _ in range(x):
        subject_scores = tuple(map(float, input().split()))
        scores.append(subject_scores)

    # Вычисляем и выводим средние баллы
    result = compute_average_scores(scores)
    for avg in result:
        print(avg)
