# 2.1
# try:
#     student_name = input("Write the student's name: ")#     assignment_scores = input("Write scores for assignments: ").split(",")
#     lab_scores = input("Write scores for labs: ").split(",")#     test_scores = input("Write scores for tests: ").split()
##     assignment_scores = [int(score) for score in assignment_scores]
#     lab_scores = [float(score) for score in lab_scores]#     test_scores = [int(score) for score in test_scores]
##     student = {
#         'name': student_name,#         'assignment': assignment_scores,
#         'lab': lab_scores,#         'test': test_scores
#     }# student["test"]
##     print("Student information:")
#     print(student)#
# except (ValueError, IndexError):#     print("Wrong value or sequence out of range!!! ")

#2.2
# try:
#     student_name = input("Write student's name: ")#
#     assignment_scores = list(map(int, input("Write assignment scores: ").split(',')))
# input = "3,4,5,6,7"# input.split()  ---> ["3", "4", "5", "6", "7"]
# map(int, )#     lab_scores = list(map(float, input("Write lab scores: ").split(',')))
#     test_scores = list(map(int, input("Write test scores: ").split(',')))
##     submission_check = {}
##     total_submissions = len(assignment_scores) + len(lab_scores) + len(test_scores)
##     if total_submissions == 8:
#         submission_check[student_name] = total_submissions#     else:
#         submission_check[student_name] = 0#
#     print("Submission Check:")#     print(submission_check)
## except (ValueError, IndexError):
#     print("Wrong value or sequence out of range!!! ")

#2.3
def final(student):
    if len(student['assignment']) >= 4 and len(student['test']) >= 4 and len(student['lab']) >= 4:
        final_grade = 0.3 * sum(student['assignment']) / len(student['assignment']) + \
                      0.5 * sum(student['lab']) / len(student['lab']) + \
                      0.2 * sum(student['test']) / len(student['test'])
        student['final grade'] = round(final_grade, 2)
    else:
        student['final grade'] = 0.0
student_name = input("Enter student's name: ")
assignment = [float(x) for x in input("Assignment grades separated by space: ").split()]
test = [float(x) for x in input("Test grades separated by space: ").split()]
lab = [float(x) for x in input("Lab grades separated by space: ").split()]
result = {'name': student_name, 'assignment': assignment, 'test': test, 'lab': lab}
final(result)
print(result)

# #2.4
# def final2():
#     student_name = input("Enter student's name: ")
#     assignm = [float(x) for x in input("Enter assignment grades separated by space: ").split()]
#     test2 = [float(x) for x in input("Enter test grades separated by space: ").split()]
#     lab2 = [float(x) for x in input("Enter lab grades separated by space: ").split()]
#     final2 = float(input("Enter final grade: "))
#     student = {'name': student_name, 'assignment': assignm, 'test': test2, 'lab': lab2,
#                'final2': final2}
#     return student
# NUMstudents = int(input("Enter the number of students: "))
# students = {}
# for _ in range(NUMstudents):
#     student_data = final2()
#     students[student_data['name']] = {'assignment': student_data['assignment'], 'test': student_data['test'],
#                                       'lab': student_data['lab'], 'final_grade': student_data['final_grade']}
# print(students)