from app import db
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

class Stage(db.Model):
    id = Column(
    	  Integer,
    	  primary_key=True,
    	  nullable=False,
    )

    name = Column(
        String,
        nullable=False,
    )

    lead_id = Column(
    	  Integer,
    	  ForeignKey("lead.id")
    )

    lead = relationship(
        "Lead",
        back_populates="stages"
    )

    def __repr__(self):
        return '<Stage %r>' % self.id