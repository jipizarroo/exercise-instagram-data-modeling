import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

        
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True) 
    username = Column(String(200), nullable = False)
    password = Column(String(200), nullable = False)
    email = Column(String(200), nullable = False)


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    avatar = Column(String(200), nullable = True)
    biography = Column(String(255), nullable = True)
    location = Column(String(255), nullable = True)
    story_Highlights = Column(String(255), nullable = True)
    post_Highlights = Column(String(255), nullable = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User)

class Follower(Base):
    __tablename__ = "followers"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)    
    user = relationship(User)
    follower_id = Column(Integer, ForeignKey("users.id"), primary_key=True)    
    follower = relationship(User)

class Post(Base):
    __tablename__="posts"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship(User)
    media = Column(String(255), nullable = False)
    sub_titulo = Column(String(255), nullable=True)
    

class Comment(Base):
    __tablename__="comments"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship(User)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    post = relationship(Post)
    commenttext = Column(String(255), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')