# ==========================================
# Question No 1: Employee Pay Calculator
# ==========================================

def calculate_pay():
    print("----- Employee Pay Calculator -----")
    hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter hourly rate: "))

    if hours <= 40:
        total_pay = hours * rate
    else:
        normal_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        total_pay = normal_pay + overtime_pay

    print(f"Total Pay: {total_pay:.2f}")
    print()


# ==========================================
# Question No 2: Advanced Student Marksheet
# ==========================================

def student_marksheet():
    print("----- Advanced Student Marksheet -----")
    name = input("Enter student's name: ")
    roll_no = input("Enter roll number: ")

    subjects = []
    marks = []

    for i in range(1, 6):
        subject_name = f"Subject{i}"
        mark = float(input(f"Enter marks for {subject_name} (out of 100): "))
        subjects.append(subject_name)
        marks.append(mark)

    total_marks = sum(marks)
    percentage = total_marks / 5

    # Determine grade
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Check pass/fail
    failed_subject = any(m < 40 for m in marks)
    if failed_subject:
        result = "Fail"
    elif percentage < 40:
        result = "Fail"
    else:
        result = "Pass"

    # Display complete marksheet
    print("\n========== MARKSHEET ==========")
    print(f"Name        : {name}")
    print(f"Roll No     : {roll_no}")
    print("--------------------------------")
    for subj, mark in zip(subjects, marks):
        print(f"{subj:<10}: {mark}")
    print("--------------------------------")
    print(f"Total Marks : {total_marks}/500")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print("================================")


# ==========================================
# Main Program
# ==========================================

if __name__ == "__main__":
    calculate_pay()
    student_marksheet()
