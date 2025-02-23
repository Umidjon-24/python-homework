#TASK 4
def enrollment_stats(list1):
    student_numbers = list()
    tuition_fees = list()
    for i in range (len(universities)):
        student_numbers.append(list1[i][1])
        tuition_fees.append(list1[i][2])
    
    return student_numbers, tuition_fees

def mean(list2):
    sum = 0
    for i in range (len(list2)):
        sum += list2[i]
    return sum/len(list2)
def median(list3):
    list3.sort()
    if len(list3)%2 == 1:
        return list3[len(list3)//2]
    else:
        return (list3[len(list3)//2]+list3[len(list3)//2+1])/2

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

student_num, tuition = enrollment_stats(universities)
total_students = 0
total_tuition = 0
for i in range (len(universities)):
    total_students += universities[i][1]  
    total_tuition += universities[i][2]

print(30*'*')
print(f"Total students: {total_students:,} \nTotal tuition: {total_tuition:,} \n")
print(f"Student mean: {mean(student_num):,.2f} \nStudent meadian: {median(student_num):,} \n")
print(f"Tuition mean: $ {mean(tuition):,.2f} \nTuition median: $ {median(tuition):,}")
print(30*"*")


