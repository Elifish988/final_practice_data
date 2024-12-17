from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from postges.db import Base


class Student_lifestyle(Base):
    __tablename__ = 'Student_Lifestyle'

    Student_ID = Column(Integer, ForeignKey('students.id'), primary_key=True)
    Study_Hours_Per_Day = Column(Integer)
    Extracurricular_Hours_Per_Day = Column(Integer)
    Sleep_Hours_Per_Day = Column(Integer)
    Social_Hours_Per_Day = Column(Integer)
    Physical_Activity_Hours_Per_Day = Column(Integer)
    GPA = Column(Float)
    Stress_Level = Column(String)

    # קשר עם טבלת Students
    student = relationship("Students", back_populates="lifestyle", uselist=False)

    def to_dict(self):
        return {
            'Student_ID': self.Student_ID,
            'Study_Hours_Per_Day': self.Study_Hours_Per_Day,
            'Extracurricular_Hours_Per_Day': self.Extracurricular_Hours_Per_Day,
            'Sleep_Hours_Per_Day': self.Sleep_Hours_Per_Day,
            'Social_Hours_Per_Day': self.Social_Hours_Per_Day,
            'Physical_Activity_Hours_Per_Day': self.Physical_Activity_Hours_Per_Day,
            'GPA': self.GPA,
            'Stress_Level': self.Stress_Level
        }