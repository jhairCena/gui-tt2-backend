# models.py - definición del modelo de datos para pacientes
from sqlalchemy import Column, Integer, String, Date, DateTime  # tipos de columnas
from sqlalchemy.orm import declarative_base                     # base declarativa
from datetime import datetime                                   # tipo datetime

Base = declarative_base()                                       # base propia del modelo

class Paciente(Base):                                           # modelo de paciente
    __tablename__ = "pacientes"                                 # nombre de la tabla

    id           = Column(Integer, primary_key=True, index=True) # id autoincremental
    nombre       = Column(String(100))                           # nombre(s)
    ap_paterno   = Column(String(100))                           # apellido paterno
    ap_materno   = Column(String(100))                           # apellido materno
    fecha_nac    = Column(Date)                                  # fecha de nacimiento
    padecimiento = Column(String(200))                           # padecimiento
    created_at   = Column(DateTime, default=datetime.utcnow)    # fecha de creación auto