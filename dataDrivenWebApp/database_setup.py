import sys
# Config
from sqlalchemy import Column, ForeignKey, Integer, String #Mapper code
from sqlalchemy.ext.declarative import declarative_base #Config and class code
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine # Config

Base = declarative_base() # Let SQLAlchemy know that classes are special that corresponds to columns in table

# Classes
class Restaurant(Base):
    # Create a table rep, __tablename__ let SQLA know var to be used
    __tablename__ = 'restaurant'
    name = Column(String(80),nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80),nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine) # Goes into database and adds the classes as new tables in the database


    
