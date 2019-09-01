from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///matcha.db', echo=True)
Base = declarative_base()

class Usrs(Base):
    __tablename__ = "usrs"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    realname = Column(String)
    password = Column(String)
    hashkey = Column(String)
    e_mail = Column(String)
    gender = Column(Integer)
    sexuality = Column(Integer)
    biography = Column(String)
    interests = Column(String)
    pic1 = Column(String)
    pic2 = Column(String)
    pic3 = Column(String)
    pic4 = Column(String)
    pic5 = Column(String)

    def __init__(self, username, realname, password, hashkey, e_mail, gender, sexuality, biography, interests,
                pic1, pic2, pic3, pic4, pic5):
        self.username = username
        self.realname = realname
        self.password = password
        self.hashkey = hashkey
        self.e_mail = e_mail
        self.gender = gender
        self.sexuality = sexuality
        self.biography = biography
        self.interests = interests
        self.pic1 = pic1
        self.pic2 = pic2
        self.pic3 = pic3
        self.pic4 = pic4
        self.pic5 = pic5

# class Chat(Base):
#     __tablename__ = "chat"

#     tId = Column(Integer)
#     rId = Column(Integer)
#     msg = Column(String)

#     def __init__(self, tId, rId, msg):
#         self.tId = tId
#         self.rId = rId
#         self.msg = msg

Base.metadata.create_all(engine)
