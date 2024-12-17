import pandas as pd
from postges.db import  session
from postges.models import Students
from postges.models import Student_course_performance
from postges.models import Student_lifestyle

# שליפת נתונים מטבלת Students
students_query = session.query(Students).all()
students_data = [student.to_dict() for student in students_query]
students_df = pd.DataFrame(students_data)

# שליפת נתונים מטבלת Student_Lifestyle
lifestyle_query = session.query(Student_lifestyle).all()
lifestyle_data = [student.to_dict() for student in lifestyle_query]
lifestyle_df = pd.DataFrame(lifestyle_data)

# שליפת נתונים מטבלת Student_Course_Performance
performance_query = session.query(Student_course_performance).all()
performance_data = [performance.to_dict() for performance in performance_query]
performance_df = pd.DataFrame(performance_data)

# סגירת session
session.close()

def average_sleep_hours():
    average_sleep_hours = lifestyle_df['Sleep_Hours_Per_Day'].mean()
    return average_sleep_hours

def average_current_grade():
    average_current_grade = performance_df['current_grade'].mean()
    return average_current_grade


def students_sleep_below_average_and_grade_above_average():
    """שליפת סטודנטים עם שעות שינה נמוכות מהממוצע וציון גבוה מהממוצע"""
    # חישוב ממוצעים
    avg_sleep = average_sleep_hours()
    avg_grade = average_current_grade()

    # איחוד הנתונים: Students, Student_lifestyle ו- Student_course_performance
    merged_df = pd.merge(students_df, lifestyle_df, left_on='id', right_on='Student_ID')
    merged_df = pd.merge(merged_df, performance_df, left_on='id', right_on='student_id')

    # סינון הסטודנטים לפי התנאים
    filtered_students = merged_df[
        (merged_df['Sleep_Hours_Per_Day'] < avg_sleep) &
        (merged_df['current_grade'] > avg_grade)
        ]

    # החזרת התוצאה עם שמות הסטודנטים בלבד
    return filtered_students[['id', 'first_name', 'last_name', 'Sleep_Hours_Per_Day', 'current_grade']]


# הפעלת הפונקציה והדפסת התוצאות
if __name__ == "__main__":
    print("ממוצע שעות השינה:", average_sleep_hours())
    print("ממוצע הציונים:", average_current_grade())

    print("\nסטודנטים עם שעות שינה נמוכות מהממוצע וציון גבוה מהממוצע:")
    students_result = students_sleep_below_average_and_grade_above_average()
    print(students_result)
