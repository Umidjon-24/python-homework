import csv
from collections import defaultdict
filename = "grades.csv"

with open(filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    data_list = defaultdict(list)

    for row in csv_reader:
        subject = row['Subject']
        grade = int(row['Grade'])
        data_list[subject].append(grade)

average = {subject: sum(grade)/len(grade) for subject, grade in data_list.items()}

with open('average_grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average grade'])
    for subject, grade in average.items():
        writer.writerow([subject, grade])