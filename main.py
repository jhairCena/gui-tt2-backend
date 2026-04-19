# main.py - API REST para gestión de pacientes
from fastapi import FastAPI, Depends                         # framework + dependencias
from fastapi.middleware.cors import CORSMiddleware           # permite conexión desde React
from sqlalchemy.orm import Session                           # manejo de sesiones
from pydantic import BaseModel                               # validación de datos
from datetime import date                                    # tipo fecha
from database import engine, SessionLocal                    # motor y sesiones
import models                                                # importa módulo models
from models import Base, Paciente                            # modelos y base
from database import DATABASE_URL                            # verifica la URL
print("DATABASE_URL:", DATABASE_URL)                         # imprime en terminal

Base.metadata.create_all(bind=engine)                        # crea tablas si no existen
print("Tablas registradas:", Base.metadata.tables.keys())    # verifica tablas registradas

app = FastAPI()                                              # instancia de la app

app.add_middleware(                                          # configura CORS
    CORSMiddleware,
    allow_origins=["*"],                                     # permite cualquier origen
    allow_methods=["*"],                                     # permite todos los métodos
    allow_headers=["*"],                                     # permite todos los headers
)

def get_db():                                                # dependencia de sesión
    db = SessionLocal()                                      # abre sesión
    try:
        yield db                                             # entrega sesión
    finally:
        db.close()                                           # cierra sesión

class PacienteSchema(BaseModel):                             # esquema de entrada
    nombre:       str                                        # nombre(s)
    ap_paterno:   str                                        # apellido paterno
    ap_materno:   str                                        # apellido materno
    fecha_nac:    date                                       # fecha de nacimiento
    padecimiento: str                                        # padecimiento

    class Config:                                            # config de pydantic
        from_attributes = True                               # permite ORM → schema

@app.get("/")                                                # ruta de prueba
def root():
    return {"status": "ok"}                                  # respuesta simple

@app.get("/pacientes")                                       # obtener todos los pacientes
def obtener_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()                          # retorna lista completa

@app.post("/pacientes")                                      # registrar paciente
def crear_paciente(paciente: PacienteSchema, db: Session = Depends(get_db)):
    nuevo = Paciente(**paciente.dict())                      # crea objeto paciente
    db.add(nuevo)                                            # agrega a la sesión
    db.commit()                                              # guarda en BD
    db.refresh(nuevo)                                        # refresca el objeto
    return nuevo                                             # retorna el paciente creado