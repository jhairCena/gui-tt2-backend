# models.py - definición de modelos de datos
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey  # tipos
from sqlalchemy.dialects.postgresql import ARRAY                             # array PostgreSQL
from sqlalchemy.orm import declarative_base                                  # base declarativa
from datetime import datetime                                                 # tipo datetime

Base = declarative_base()                                                    # base propia

class Paciente(Base):                                                        # modelo paciente
    __tablename__ = "pacientes"

    id           = Column(Integer, primary_key=True, index=True)             # id autoincremental
    nombre       = Column(String(100))                                       # nombre(s)
    ap_paterno   = Column(String(100))                                       # apellido paterno
    ap_materno   = Column(String(100))                                       # apellido materno
    fecha_nac    = Column(Date)                                              # fecha nacimiento
    padecimiento = Column(String(200))                                       # padecimiento
    created_at   = Column(DateTime, default=datetime.utcnow)                 # fecha creación

class Termografia(Base):                                                     # modelo termografía
    __tablename__ = "termografias"

    id          = Column(Integer, primary_key=True, index=True)              # id autoincremental
    paciente_id = Column(Integer, ForeignKey('pacientes.id', ondelete='CASCADE'), nullable=False)
    fecha       = Column(String(20), nullable=False)                         # ej: 2026-04-25
    imagenes    = Column(ARRAY(String), nullable=False)                      # URLs Drive
    created_at  = Column(DateTime, default=datetime.utcnow)                  # fecha creación