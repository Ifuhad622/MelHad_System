# setup_db.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Database configuration
DATABASE_URL = 'sqlite:///mydatabase.db'

# Create engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Define a sample table
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50), nullable=False),
    Column('email', String(100), nullable=False)
)

# Create tables in the database
metadata.create_all()

print("Database setup complete!")
