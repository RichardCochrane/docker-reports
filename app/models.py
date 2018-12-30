from sqlalchemy import Column, DateTime, Integer, String
from app.db import Base


class ExerciseSummary(Base):
    """Class representing the exercises saved."""

    __tablename__ = "exercise_summary"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    subject = Column(String(80), nullable=False)

    def __repr__(self):
        """Return a readable version of the exercise summary."""
        return 'Exercise: {} | {} | {}'.format(
            self.id, self.subject, self.created_at.strftime('%-d %B %Y'))
