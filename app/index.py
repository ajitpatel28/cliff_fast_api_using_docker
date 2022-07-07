from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from db import meta
users = Table(

    'users',meta,
    Column('fullname',String(255)),
    Column('email',String(255)),
    Column('password',String(255))

)