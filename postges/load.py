import csv
import json
from postges.db import session
from postges.models.Classes_model import Classes
from postges.models.Relationships_model import Relationships
from postges.models.Student_reviews_model import Student_reviews
from postges.models.Teachers_model import Teachers
from postges.models.student_course_performance_model import Student_course_performance
from postges.models.student_lifestyle_model import Student_lifestyle
from postges.models.students_model import Students


def load_json():
    with open('academic_network.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # הוספת מורים
    for teacher_data in data['teachers']:
        teacher = Teachers(**teacher_data)
        session.add(teacher)

    # הוספת שיעורים
    for class_data in data['classes']:
        class_ = Classes(**class_data)
        session.add(class_)

    # הוספת קשרים
    for relationship_data in data['relationships']:
        student = session.query(Students).filter_by(id=relationship_data['student_id']).first()
        teacher = session.query(Teachers).filter_by(id=relationship_data['teacher_id']).first()
        class_ = session.query(Classes).filter_by(id=relationship_data['class_id']).first()

        if student and teacher and class_:
            relationship = Relationships(**relationship_data)
            session.add(relationship)
        else:
            print(f"הקשר לא יכול להיווסף, חוסר בסטודנט, מורה או כיתה")

    # שמירת הנתונים
    session.commit()


def load_all_csv():
    # קריאת קובץ 'students.csv' וטעינת הנתונים
    with open('students-profiles.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = Students(
                first_name=row['first_name'],
                last_name=row['last_name'],
                age=int(row['age']),
                address=row['address']
            )
            session.add(student)

    # קריאת קובץ 'student_course_performance.csv' וטעינת הנתונים
    with open('student_course_performance.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # בדיקת אם הסטודנט קיים בטבלת Students
            student = session.query(Students).filter_by(id=int(row['student_id'])).first()
            if student:
                performance = Student_course_performance(
                    student_id=int(row['student_id']),
                    course_name=row['course_name'],
                    current_grade=float(row['current_grade']),
                    attendance_rate=float(row['attendance_rate']),
                    assignments_completed=int(row['assignments_completed']),
                    missed_deadlines=int(row['missed_deadlines']),
                    participation_score=float(row['participation_score']),
                    midterm_grade=float(row['midterm_grade']),
                    study_group_attendance=int(row['study_group_attendance']),
                    office_hours_visits=int(row['office_hours_visits']),
                    extra_credit_completed=int(row['extra_credit_completed'])
                )
                session.add(performance)
            else:
                print(f"סטודנט עם ID {row['student_id']} לא נמצא בטבלת Students")

    # קריאת קובץ 'student_lifestyle.csv' וטעינת הנתונים
    with open('student_lifestyle.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lifestyle = Student_lifestyle(
                Student_ID=int(row['Student_ID']),
                Study_Hours_Per_Day=float(row['Study_Hours_Per_Day']),
                Extracurricular_Hours_Per_Day=float(row['Extracurricular_Hours_Per_Day']),
                Sleep_Hours_Per_Day=float(row['Sleep_Hours_Per_Day']),
                Social_Hours_Per_Day=float(row['Social_Hours_Per_Day']),
                Physical_Activity_Hours_Per_Day=float(row['Physical_Activity_Hours_Per_Day']),
                GPA=float(row['GPA']),
                Stress_Level=row['Stress_Level']
            )
            session.add(lifestyle)

    # קריאת קובץ 'student_reviews.csv' וטעינת הנתונים
    with open('reviews_with_students.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            review = Student_reviews(
                review_id=row['review_id'],
                content=row['content'],
                score=int(row['score']),
                thumbs_up_count=int(row['thumbs_up_count']),
                review_created_version=row['review_created_version'],
                date_time=row['date_time'],
                app_version=row['app_version'],
                student_id=int(row['student_id'])
            )
            session.add(review)

    # שמירת כל השינויים במסד הנתונים
    session.commit()
