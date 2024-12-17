from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from postges.db import Base


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    address = Column(String)

    relationships = relationship("Relationships", back_populates="student")  # הוספת back_populates כאן
    lifestyle = relationship("Student_lifestyle", back_populates="student", uselist=False)
    course_performance = relationship("Student_course_performance", back_populates="student", uselist=True)
    reviews = relationship("Student_reviews", back_populates="student")

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'address': self.address
        }

