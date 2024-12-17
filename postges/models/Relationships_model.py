from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from postges.db import Base

class Relationships(Base):
    __tablename__ = 'relationships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    class_id = Column(String, ForeignKey('classes.id'))
    teacher_id = Column(String, ForeignKey('teachers.id'))
    enrollment_date = Column(String)
    relationship_type = Column(String)

    # קשרים עם הטבלאות Students, Classes, Teachers
    student = relationship("Students", back_populates="relationships")
    classes = relationship("Classes", back_populates="relationships")
    # teacher = relationship("Teachers")

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'class_id': self.class_id,
            'teacher_id': self.teacher_id,
            'enrollment_date': self.enrollment_date,
            'relationship_type': self.relationship_type
        }

