import csv

marks = []

with open('marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks.append(int(row['Marks']))

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("📊 Student Marks Analysis")
print("--------------------------")
print(f"Average Marks: {average}")
print(f"Highest Marks: {highest}")
print(f"Lowest Marks: {lowest}")

print("\nPass/Fail Status:")
with open('marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        status = "Pass" if int(row['Marks']) >= 50 else "Fail"
        print(f"{row['Name']} : {status}")
