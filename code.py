def input_single_exam():
    exam_label = "Exam 1"
    print(f"\nEntering scores for {exam_label}")
    num_subjects = int(input("Enter number of subjects: "))
    subject_scores = {}

    for j in range(num_subjects):
        while True:
            try:
                score = float(input(f"Enter score for Subject {j + 1}: "))
                if 0 <= score <= 100:
                    subject_scores[f"Subject {j + 1}"] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    return {exam_label: subject_scores}


def input_multiple_exams():
    exams = {}
    num_exams = int(input("Enter the number of exams: "))

    for i in range(num_exams):
        exam_label = f"Exam {i + 1}"
        print(f"\nEntering scores for {exam_label}")
        num_subjects = int(input(f"Enter number of subjects in {exam_label}: "))
        subject_scores = {}

        for j in range(num_subjects):
            while True:
                try:
                    score = float(input(f"Enter score for Subject {j + 1}: "))
                    if 0 <= score <= 100:
                        subject_scores[f"Subject {j + 1}"] = score
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Enter a numeric value.")

        exams[exam_label] = subject_scores
    return exams


def analyze_exam(exam_label, scores):
    total = sum(scores.values())
    avg = total / len(scores)
    print(f"\nPerformance in {exam_label}:")
    for subject, score in scores.items():
        print(f"{subject}: {score}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print("Result:", "Pass" if avg >= 40 else "Fail")


def analyze_all_exams(exams):
    print("\nOverall Performance Across All Exams:")
    grand_total = 0
    subject_count = 0

    for exam_label, scores in exams.items():
        total = sum(scores.values())
        avg = total / len(scores)
        grand_total += total
        subject_count += len(scores)

        print(f"\n{exam_label}")
        for subject, score in scores.items():
            print(f"{subject}: {score}")
        print(f"Total: {total}")
        print(f"Average: {avg:.2f}")
        print("Result:", "Pass" if avg >= 40 else "Fail")

    if subject_count > 0:
        overall_avg = grand_total / subject_count
        print(f"\nOverall Average Across All Exams: {overall_avg:.2f}")
        print("Final Result:", "Pass" if overall_avg >= 40 else "Fail")
    else:
        print("No subjects found to calculate overall average.")


# ---------- Main Program ----------

print("Student Performance Analyzer")

while True:
    print("\nMENU")
    print("1. Analyze Performance of a Particular Exam")
    print("2. Analyze Performance of All Exams")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        single_exam = input_single_exam()
        exam_label = list(single_exam.keys())[0]
        analyze_exam(exam_label, single_exam[exam_label])

    elif choice == "2":
        exams_data = input_multiple_exams()
        analyze_all_exams(exams_data)

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
