#!/usr/bin/env python

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, and_
import os

path = os.path.abspath(os.path.dirname(__file__)) + "/"
db = path + 'Users.db'

engine = create_engine('sqlite:///' + db)
engine.echo = False

metadata = MetaData(engine)

if not os.path.exists(db):
	Users = Table('Users', metadata,
		Column('id', Integer, primary_key = True),
		Column('Nombre', String(20)),
	        Column('Apellidos', String(20)),
	        Column('Profesion', String(20)),
	        Column('Telefono', String(20)),
	        Column('Github', String(20)),
	        Column('Twitter', String(20)),
	        Column('Facebook', String(20)),
	        Column('NombreP', String(20)),
	        Column('Tipo', String(20)),
	        Column('Tecnologia', String(20)),
	        Column('Repositorio', String(20)),
	        Column('Sitio', String(20)),
		Column('Contribuidores', String(20)),
		)

	Users.create()
else:
	Users = Table('Users', metadata, autoload = True)