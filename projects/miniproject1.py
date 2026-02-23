def calculate_course_grade(assignments, total_weight):

    print("\n--- Enter Assignment Grades ---")
    while True:
        name = input("\nEnter assignment name (or type 'done'): ")
        if name.lower() == 'done':
            break

        grade = float(input("Enter grade (0-100): "))
        weight = float(input("Enter weight (as a percentage, ex: 20 for 20%): "))

        assignments.append((grade, weight))
        total_weight += weight

    weighted_sum = 0
    for grade, weight in assignments:
        weighted_sum += grade * (weight / 100)

    print(f"\nCurrent Course Grade: {weighted_sum:.2f}%")
    print(f"Total Weight Entered: {total_weight}%")

    return weighted_sum, total_weight

calculate_course_grade([], 0)