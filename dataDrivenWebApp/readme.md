Presents the user with varity of options in a menu.
Where they would be able to CRUD


Theory:

Module 02: Full Stack Foundations

Lesson 01: Working with CRUD

- Creating Database with SQLAlchemy
    * Configuration(To import all needed modules):
    * Class(rep data):
        rep. of tables as a py class
        extends the base class
        nested inside would be the table and mapper code
    * Table:
    * Mapper:

-   In this lesson, we performed all of our CRUD operations with SQLAlchemy on an SQLite database. Before we perform any operations, we must first import the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database:

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from database_setup import Base, Restaurant, MenuItem

    engine = create_engine('sqlite:///restaurantMenu.db')
    Base.metadata.bind=engine
    DBSession = sessionmaker(bind = engine)
    session = DBSession()


- CRUD Create
    * engine = create_engine() lets sqlAlchemy know which .db we are communicating with.

    * Base.metadata.bind # Binds the engine with the base class, ie class definations and corresponding Tables in db

    * DBSession = sessionmaker object establishes a communication b/w code exe and the engine created.

    * SQLAlchemy exe. database operations via an interface (Session). 
        • Session allows us to write down all the commands we would like to execute
        • So when we would like to make a change in our database we can do that from the any of the methods inside the session object.
        • DBSession obj provides a session zone for all of the objects loaded db session obj, any change made in the objs in session won't be persisted in the database until we call session commit.

    * Making a new entry in db
        • newEntry = ClassName(property = "value",...)
        • session.add(newEntry)
        • session.commit()
        >>> Base.metadata.bind = engine
        >>> DBSession = sessionmaker(bind=engine)
        >>> session = DBSession()
        >>> myFirstRestaurant = Restaurant(name = "Pizza Palace")
        >>> session.add(myFirstRestaurant)
        >>> session.commit()

    * Do to db find table that corresponds to restaurant and display all
        >>> session.query(Restaurant).all
        <bound method Query.all of <sqlalchemy.orm.query.Query object at 0x10ae232b0>>
        >>> cheesepizza = MenuItem(name = "Cheese Pizza", description="Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant )
        >>> session.add(cheesepizza)
        >>> session.commit()
        >>> session.query(MenuItem).all()

    * Reading from database
        firstResult = session.query(Restaurant).first()

    * Updaing a existing
        • Find entry : filter_by
        • Reset Values
        • Add to session
        • session.commit()

        rebecca = session.query(Employee).filter_by(name = "Rebecca Allen").one()
        RebeccaAddress = session.query(Address).filter_by(employee_id = rebecca.id).one()
        RebeccasAddress.street = "120 Loran Circle"
        RebeccasAddress.zip = "22309"
        session.add(RebeccasAddress)
        session.commit()
    
    * Deleting 
        • Find entry
        • session.delete(entry)
        • session.commit()

        spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
        print(spinach.restaurant.name) -> Auntie Ann's Diner
        session.delete(spinach) 
        session.commit() # To persist the change


Lesson 02: Making a Web Server

- Protocols: For clients and server to commnunicate in the same language
    TCP,IP,HTTP

