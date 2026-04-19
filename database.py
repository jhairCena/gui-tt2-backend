# database.py - configuración de la base de datos con SQLAlchemy
from sqlalchemy import create_engine                        # motor de BD
from sqlalchemy.orm import declarative_base                 # base para modelos
from sqlalchemy.orm import sessionmaker                     # manejo de sesiones
from dotenv import load_dotenv                             # carga variables de entorno
import os                                                   # acceso a variables

load_dotenv()                                              # carga el .env

DATABASE_URL = os.getenv("DATABASE_URL")                   # URL completa de conexión
engine = create_engine(DATABASE_URL)                       # crea el motor
SessionLocal = sessionmaker(bind=engine)                   # fábrica de sesiones
Base = declarative_base()                                  # base para modelos