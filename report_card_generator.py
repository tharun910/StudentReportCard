# Grade Calculation Module
# CSV Reader Module
import csv
import os
import statistics

os.makedirs("report_cards", exist_ok=True)

def get_grade(avg):
    # Excellent
    if avg >= 90:
        return "A"

    # Very Good
    elif avg >= 80:
        return "B"

    # Good
    elif avg >= 70:
        return "C"

    # Pass
    elif avg >= 60:
        return "D"

    # Fail
    else:
        return "F"

with open("data/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]

        marks = [
            int(row["Math"]),
            int(row["Science"]),
            int(row["English"])
        ]
# Check that all marks are between 0 and 100
if any(mark < 0 or mark > 100 for mark in marks):
    print(f"Invalid marks for {name}")
    continue
        total = sum(marks)
        average = total / len(marks)

        if len(marks) > 1:
            std_dev = statistics.stdev(marks)
        else:
            std_dev = 0

        grade = get_grade(average)

        with open(f"report_cards/{name}.txt", "w") as report:
            report.write("===== STUDENT REPORT CARD =====\n")
            report.write(f"Name: {name}\n")
            report.write(f"Math: {marks[0]}\n")
            report.write(f"Science: {marks[1]}\n")
            report.write(f"English: {marks[2]}\n")
            report.write(f"Total: {total}\n")
            report.write(f"Average: {average:.2f}\n")
            report.write(f"Standard Deviation: {std_dev:.2f}\n")
            report.write(f"Grade: {grade}\n")

print("Report cards generated successfully!")