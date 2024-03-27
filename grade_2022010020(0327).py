def input_students():   # 학생 정보를 입력하는 함수
    students = []
    for i in range(5): 
        student_id = input("학번: ")
        name = input("이름: ")
        scores = []
        for subject in ['영어', 'C-언어', '파이썬']: 
            score = float(input(f"{subject}: "))
            scores.append(score)
        students.append({'student_id': student_id, 'name': name, 'scores': scores})
        print()
    return students

def calculate_total(scores):  # 총점을 계산하는 함수
    return sum(scores)


def calculate_average(scores):  # 평균을 계산하는 함수
    return sum(scores) / len(scores)


def calculate_grade(scores):  # 학점을 계산하는 함수
    ave = sum(scores) / len(scores) 
    if ave >= 95:
        return "A+"
    elif ave >= 90:
        return "A"
    elif ave >= 85:
        return "B+"
    elif ave >= 80:
        return "B"
    elif ave >= 75:
        return "C+"
    elif ave >= 70:
        return "C"
    elif ave >= 65:
        return "D+"
    elif ave >= 60:
        return "D"
    else:
        return "F"


def calculate_rank(students): # 등수를 계산하여 학생에게 할당하는 함수
    students.sort(key=lambda x: calculate_average(x['scores']), reverse=True)
    for i, student in enumerate(students):
        student['average_rank'] = i + 1
    return students


def output_students(students): # 학생 정보 출력 함수
    print("\n\n")
    print("==============================================================================================")
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("==============================================================================================")

    for student in students:
        total_score = calculate_total(student['scores'])
        average_score = calculate_average(student['scores'])
        grade = calculate_grade(student['scores'])
        rank = student['average_rank'] 
        print(f"{student['student_id']}\t{student['name']}\t{student['scores'][0]}\t{student['scores'][1]}\t{student['scores'][2]}\t{total_score}\t{average_score:.2f}\t{grade}\t{rank}")


students = input_students()  # 학생 정보 입력하기
students_with_rank = calculate_rank(students)  # 등수 계산하기
output_students(students_with_rank)  # 학생 정보 출력하기