from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Category, Base, Item, User

engine = create_engine('sqlite:///catalognew.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Create dummy user
user1 = User(name="First User", email="firstuser@example.com")
session.add(user1)
session.commit()


# Music Category
music_category = Category(user_id=1, name="Music")
session.add(music_category)
session.commit()

# A few Items
musicItem1 = Item(user_id=1, name="Hall and Oates Greatest Hits",
                    description="Greatest Hits album featuring some of their best songs",
                    price="$9.99", category=music_category)

session.add(musicItem1)
session.commit()

musicItem2 = Item(user_id=1, name="Master of Puppets",
                    description="considered to be one of Metallica's finest albums",
                    price="$11.99", category=music_category)

session.add(musicItem2)
session.commit()

musicItem3 = Item(user_id=1, name="Some Girls",
                    description="Classic album by The Rolling Stones",
                    price="$10.99", category=music_category)

session.add(musicItem3)
session.commit()

# Movie Category
movie_category = Category(user_id=1, name="Movies")
session.add(movie_category)
session.commit()

# Items for the movie category
movieItem1 = Item(user_id=1, name="Step Brothers", description=
                    "Comedy staring Will Farrel and John C. Riley",
                    price="16.99", category=movie_category)

session.add(movieItem1)
session.commit()

movieItem2 = Item(user_id=1, name="Avengers: Infinity War", description=
                    "The latest installment in Marvel's Avenger series",
                    price="$24.99", category=movie_category)

session.add(movieItem2)
session.commit()

movieItem3 = Item(user_id=1, name="The Hangover", description=
"Comedy about misadventures in Vegas. Starring Bradley Cooper and Zach Galifianakis",
price="$14.99", category=movie_category)

session.add(movieItem3)
session.commit()





