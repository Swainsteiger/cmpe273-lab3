import json

students = []
classes = []


def getStudent(_, info, id):
    for student in students:
        if student['id'] == id:
            return student
    return "Student not found."


def getClass(_, info, id):
    for temp in classes:
        if temp['id'] == id:
            return temp
    return "Class not found."


def addStudent(_, info, name):
    if len(students) == 0:
        stud_id = 0
    else:
        stud_id = students[-1]['id'] + 1
    student = \
        {
            'id': stud_id,
            'name': name
        }
    students.append(student)
    return student


def addClass(_, info, name):
    if len(classes) == 0:
        class_id = 0
    else:
        class_id = classes[-1]['id'] + 1
    newClass = \
        {
            'id': class_id,
            'name': name,
            'students': []
        }
    classes.append(newClass)
    return newClass


def updateClass(_, info, class_id, stud_id):
    s = {}
    for student in students:
        if student['id'] == stud_id:
            s = student
            for temp in classes:
                if temp['id'] == class_id:
                    stud_list = temp['students']
                    stud_list.append(s)
                    break
        else:
            return "Please add student first"
    return temp
