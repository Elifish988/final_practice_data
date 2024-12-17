from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from postges.db import Base


class Student_reviews(Base):
    __tablename__ = 'student_reviews'
    review_id = Column(String, primary_key=True)
    content = Column(String)
    score = Column(Integer)
    thumbs_up_count = Column(Integer)
    review_created_version = Column(String)
    date_time = Column(String)  # אם יש צורך באחסון כ'תאריך' אפשר לשנות ל-DateTime
    app_version = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))

    # קשר עם טבלת Students
    student = relationship("Students", back_populates="reviews")

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'content': self.content,
            'score': self.score,
            'thumbs_up_count': self.thumbs_up_count,
            'review_created_version': self.review_created_version,
            'date_time': self.date_time,
            'app_version': self.app_version,
            'student_id': self.student_id
        }
