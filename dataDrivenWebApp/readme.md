Presents the user with varity of options in a menu.
Where they would be able to CRUD


Theory:
- Creating Database with SQLAlchemy
    * Configuration(To import all needed modules):
    * Class(rep data):
        rep. of tables as a py class
        extends the base class
        nested inside would be the table and mapper code
    * Table:
    * Mapper:

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