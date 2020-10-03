# from app import db
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lead(Base):
    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    stages = relationship(
        "Stage",
        back_populates="lead"
    )

    def __repr__(self):
        return '<Lead %r>' % self.id