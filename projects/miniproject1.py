def grade_to_gpa(grade):
    """Convert a percentage grade (0-100) to GPA (0-4.0)."""
    if grade >= 93:
        return 4.0
    elif grade >= 90:
        return 3.7
    elif grade >= 87:
        return 3.3
    elif grade >= 83:
        return 3.0
    elif grade >= 80:
        return 2.7
    elif grade >= 77:
        return 2.3
    elif grade >= 73:
        return 2.0
    elif grade >= 70:
        return 1.7
    elif grade >= 67:
        return 1.3
    elif grade >= 63:
        return 1.0
    else:
        return 0.0


def calculate_course_grade(assignments, total_weight):
    """Accept assignment grades and weights, calculate weighted course grade."""
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


def calculate_required_grade(current_grade, current_weight, target_grade, remaining_weight):
    """Calculate the grade needed on remaining assignments to reach a target grade."""
    # remaining_weight is the percentage of the course not yet graded
    if remaining_weight <= 0:
        print("No remaining weight in the course.")
        return None
    
    # Formula: current_contribution + required_grade * remaining_weight_fraction = target
    # current_contribution = current_grade * (current_weight / 100)
    # required_grade = (target - current_contribution) / (remaining_weight / 100)
    
    current_contribution = current_grade * (current_weight / 100)
    remaining_fraction = remaining_weight / 100
    
    required = (target_grade - current_contribution) / remaining_fraction
    
    return required


def calculate_gpa(courses):
    """Calculate overall GPA from multiple courses with grades and credit hours."""
    if not courses:
        print("No courses entered.")
        return None
    
    total_grade_points = 0
    total_credits = 0
    
    for course_grade, credits in courses:
        gpa_value = grade_to_gpa(course_grade)
        grade_points = gpa_value * credits
        total_grade_points += grade_points
        total_credits += credits
    
    overall_gpa = total_grade_points / total_credits
    return overall_gpa


def main():
    """Main program loop."""
    while True:
        print("\n=== Grade Calculator ===")
        print("1. Calculate current course grade")
        print("2. Calculate required grade for target")
        print("3. Calculate overall GPA")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")
        
        if choice == '1':
            assignments = []
            current_grade, total_weight = calculate_course_grade(assignments, 0)
        
        elif choice == '2':
            current_grade = float(input("Enter your current course grade: "))
            current_weight = float(input("Enter the weight of grades completed (ex: 60 for 60%): "))
            target_grade = float(input("Enter your target grade: "))
            remaining_weight = 100 - current_weight
            
            required = calculate_required_grade(current_grade, current_weight, target_grade, remaining_weight)
            
            if required is not None:
                if required > 100:
                    print(f"\nTo reach {target_grade}%, you would need {required:.2f}% on remaining work.")
                    print("This is impossible! Consider adjusting your target grade.")
                elif required < 0:
                    print(f"\nYou only need {0:.2f}% on remaining work to reach {target_grade}%.")
                    print("You've already achieved your target!")
                else:
                    print(f"\nYou need {required:.2f}% on remaining work to reach {target_grade}%.")
        
        elif choice == '3':
            courses = []
            print("\n--- Enter Previous Courses ---")
            while True:
                response = input("\nEnter a course grade as a percentage (or type 'done'): ")
                if response.lower() == 'done':
                    break
                
                course_grade = float(response)
                credits = float(input("Enter credit hours for this course: "))
                courses.append((course_grade, credits))
            
            if courses:
                overall_gpa = calculate_gpa(courses)
                print(f"\nOverall GPA: {overall_gpa:.2f}")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()