from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from postges.db import Base

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(String, primary_key=True)
    course_name = Column(String)
    section = Column(Integer)
    department = Column(String)
    semester = Column(String)
    room = Column(String)
    schedule = Column(String)
    teacher_id = Column(String, ForeignKey('teachers.id'))

    # קשר עם טבלת Teachers
    teacher = relationship("Teachers", back_populates="classes")

    # קשר עם טבלת Relationships
    relationships = relationship("Relationships", back_populates="classes")

    def to_dict(self):
        return {
            'id': self.id,
            'course_name': self.course_name,
            'section': self.section,
            'department': self.department,
            'semester': self.semester,
            'room': self.room,
            'schedule': self.schedule,
            'teacher_id': self.teacher_id
        }
