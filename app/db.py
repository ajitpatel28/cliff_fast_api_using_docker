from sqlalchemy import create_engine,MetaData
engine=create_engine("mysql+pymysql:// root:pass@localhost:3307/test")
meta=MetaData()
conn=engine.connect()