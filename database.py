from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from sqlalchemy import Column, Integer, String, ForeignKey,create_engine,Table,MetaData
import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

Base= declarative_base()
engine= create_engine(connection_string,echo=True)

Session= sessionmaker()
class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer(),primary_key=True)
    student_name = Column(String(25),nullable=False,unique=True)
    email = Column(String(25),nullable=False,unique=True)
    def __repr__(self):
        return f"Students({self.student_name},{self.email})"
    

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer(), primary_key=True)
    course_name = Column(String(25),nullable=False,unique=True)
    def __repr__(self):
        return f"Course({self.course_name})"

class StudentCourse(Base):
    __tablename__ = 'student_course'
    id = Column(Integer(), primary_key=True)
    student_id = Column(Integer(), ForeignKey('students.id'))
    course_id = Column(Integer(), ForeignKey('course.id'))
    student = relationship('Students', backref='student_course')
    course = relationship('Course', backref='student_course')
    
    def __repr__(self):
        return f"StudentCourse({self.student_id},{self.course_id})"

class Instructor(Base):
    __tablename__ = 'instructor'
    id = Column(Integer(), primary_key=True)
    instructor_name = Column(String(25),nullable=False,unique=True)
    course_id = Column(Integer(), ForeignKey('course.id'))
    course = relationship('Course', backref='instructor')

    def __repr__(self):
        return f"Instructor({self.instructor_name},{self.course_id})"

    