from sqlalchemy import Column,  String
from sqlalchemy.orm import relationship
from postges.db import Base

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(String, primary_key=True)
    name = Column(String)
    department = Column(String)
    title = Column(String)
    office = Column(String)
    email = Column(String)

    # קשר עם טבלת Classes
    classes = relationship("Classes", back_populates="teacher")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'department': self.department,
            'title': self.title,
            'office': self.office,
            'email': self.email
        }
