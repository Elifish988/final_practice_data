from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from postges.db import Base

class Student_course_performance(Base):
    __tablename__ = 'student_Course_Performance'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_name = Column(String, primary_key=True)
    current_grade = Column(Integer)
    attendance_rate = Column(Float)
    assignments_completed = Column(Integer)
    missed_deadlines = Column(Integer)
    participation_score = Column(Float)
    midterm_grade = Column(Float)
    study_group_attendance = Column(Integer)
    office_hours_visits = Column(Integer)
    extra_credit_completed = Column(Integer)

    # קשר עם טבלת Students
    student = relationship("Students", back_populates="course_performance")

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'course_name': self.course_name,
            'current_grade': self.current_grade,
            'attendance_rate': self.attendance_rate,
            'assignments_completed': self.assignments_completed,
            'missed_deadlines': self.missed_deadlines,
            'participation_score': self.participation_score,
            'midterm_grade': self.midterm_grade,
            'study_group_attendance': self.study_group_attendance,
            'office_hours_visits': self.office_hours_visits,
            'extra_credit_completed': self.extra_credit_completed
        }

from postges.models.students_model import Students

