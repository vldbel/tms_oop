from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote_plus
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from flask import render_template
from flask import request

DB_CONN_STRING = "postgresql+psycopg2://testdbuser:%s@localhost/testdb" % quote_plus("TempP@$$")


engine = create_engine(DB_CONN_STRING)
session = Session(bind=engine)

# with engine.connect() as connection:
#      result = connection.execute(text('SELECT 1'))

class Model(DeclarativeBase):
    ...

class Car(Model):
    __tablename__ = 'car'
    id = Column('id', Integer(), primary_key=True)
    serialno = Column('serialno', Integer(), unique=True, nullable=False) 
    brand = Column('brand', String(255))
    model = Column('model', String(255))

Model.metadata.create_all(engine)

# car2 = Car(serialno="12346", brand="BMW", model="X5")
# car3 = Car(serialno="12347", brand="Subaru", model="Legacy")
# car4 = Car(serialno="12348", brand="Nissan", model="x-trail")
# session.add(car2)
# session.add(car3)
# session.add(car4)
# session.commit()

app = Flask(__name__, template_folder='templates')

@app.route("/")
def show_cars():
    count_of_cars = session.query(Car).count()
    cars = session.query(Car).all()
    cont = {'count_of_cars': count_of_cars, "cars": cars}
    return render_template('main_page.html', context=cont)


@app.route("/new_car", methods=['GET', 'POST'])
def new_car():
    if request.method == 'GET':
        return render_template('input_page.html', context={"message": ""})
    elif request.method == 'POST':
        res: dict = request.form
        new_car = Car(**res)
        session.add(new_car)
        session.commit()
    return render_template('input_page.html', context={"message": "success"})