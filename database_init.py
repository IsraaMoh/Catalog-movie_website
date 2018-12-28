#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')

# Bind the engine to the metadata of the Base class

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


session = DBSession()


session.query(Category).delete()


session.query(Items).delete()


session.query(User).delete()

# Create fake users

User1 = User(name='esraamohmmad2', email='esraamohmmad2@gmail.com',
             picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

# Create fake Movies categories

Category1 = Category(name='Horror', user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name='Romantic', user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name='Drama', user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name='Thriller', user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name='Animation', user_id=1)
session.add(Category5)
session.commit()

# full items with correct category

Item1 = Items(
    name='The Fault in Our Stars',
    date=datetime.datetime.now(),
    description="""American romantic tragedy film directed by Josh Boone,
    based on the 2012 novel of the same name by John Green.
               The film stars Shailene Woodley, Ansel Elgort, Laura Dern,
               Sam Trammell, Nat Wolff, and Willem Dafoe playing supporting
               roles.
               Woodley plays Hazel Grace Lancaster,
               a sixteen-year-old cancer patient who is forced by her
               parents to attend a support group,
               where she meets and subsequently falls in love
               with Augustus Waters, another cancer patient,
               played by Elgort""",
    picture="https://bit.ly/2VhDMLY",
    category_id=2,
    user_id=1,
    )
session.add(Item1)
session.commit()

Item2 = Items(
    name='To the Bone',
    date=datetime.datetime.now(),
    description="""American drama film, written and directed by Marti
    Noxon and starring Lily Collins, Keanu Reeves, Carrie Preston,
                        Lili Taylor, Alex Sharp. The film follows a young woman
                        (Collins) as she battles anorexia. The film premiered
                        in competition at the Sundance Film Festival,
                        as a contender in the U.S. Dramatic Competition.
                        It was released worldwide on Netflix """,
    picture="https://bit.ly/2AemIxp",
    category_id=3,
    user_id=1,
    )
session.add(Item2)
session.commit()

Item3 = Items(
    name='Searching',
    date=datetime.datetime.now(),
    description="""Drama, Mystery, Thriller Movie, American thriller
    film directed by Aneesh Chaganty in his feature debut and
               written by Chaganty and Sev Ohanian. Set almost entirely
               on smartphones and computer screens,
               the film follows a father (John Cho) trying
               to find his missing 16-year-old
               daughter (Michelle La) with the help of a police detective
               (Debra Messing).
               It is the first mainstream Hollywood thriller
               headlined by an Asian-American acto""",
    picture="https://bit.ly/2ESRmzy",
    category_id=4,
    user_id=1,
    )
session.add(Item3)
session.commit()

Item4 = Items(
    name='Frozen',
    date=datetime.datetime.now(),
    description="""American 3D computer-animated musical fantasy
    film produced by Walt Disney Animation Studios and released by
    Walt Disney Pictures.
               The 53 rd Disney animated feature film, it is inspired by
               Hans Christian Andersen's fairy tale "The Snow Queen".
               It tells the story of
               a fearless princess who sets off on a journey alongside
               a rugged iceman, his loyal reindeer, and a naive snowman
               to find her estranged sister
               whose icy powers have inadvertently trapped
               their kingdom in eternal winter.""",
    picture="https://bit.ly/2AinnOQ",
    category_id=5,
    user_id=1,
    )
session.add(Item4)
session.commit()

Item5 = Items(
    name="Don't Breathe",
    date=datetime.datetime.now(),
    description="""Crime, Horror, Thriller Movie, American horror film directed
    by Fede Alvarez, and co-written by Alvarez and Rodo Sayagues.
               The film stars Jane Levy, Dylan Minnette, Daniel Zovatto,
               and Stephen Lang, and focuses on three
               friends who get trapped inside a blind man's house
               while breaking into it.""",
    picture="https://bit.ly/2Ag9SP6",
    category_id=1,
    user_id=1,
    )
session.add(Item5)
session.commit()

print 'compelete add data base :)'
