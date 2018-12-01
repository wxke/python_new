#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
engine  = create_engine('mysql+pymysql://root:123456@localhost/student',
                        encoding='utf-8',echo=True)

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(32))

    def __repr__(self):
        return '<%s name:%s password:%s>' %(self.id,self.name,self.password)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()
# user_obj = User(name='wxk',password='123456')
#
# print(user_obj.name,user_obj.id)
#
# Session.add(user_obj)
# print(user_obj.name,user_obj.id)
# Session.commit()

data = Session.query(User).filter(User.id <3).first()#查询 #在filter中加条件 select

data.name ='155' #修改只有找到唯一的想修改的数据
print(data)
Session.commit()