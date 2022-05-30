from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy import Integer, String, DateTime, Date, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime

engine = create_engine("sqlite:///flotilla.db")

Base = declarative_base()


class Conduuctor(Base):
    __tablename__ = "tbl_conductor"

    id = Column(Integer, Sequence("conductor_id_seq"), primary_key=True)
    nombre = Column(String(50),  nullable=False)
    edad = Column(Integer, nullable=True)
    direccion = Column(String(80), nullable=True)
    asignaciones = relationship("Asignacion")



class Vehiculo(Base):
    __tablename__ = "tbl_vehiculos"

    id = Column(Integer, Sequence("vehiculo_id_seq"), primary_key=True)
    modelo = Column(String(30), nullable=False)
    marca = Column(String(20), nullable=False)
    annio = Column(Integer, nullable=True)
    placas = Column(String(10), nullable=True)
    asignaciones = relationship("Asignacion")



class Mantenimiento(Base):
    __tablename__ = "tbl_mantenimientos"

    id = Column(Integer, Sequence("manto_id_seq"), primary_key=True)
    fecha_mnto = Column(DateTime, default=datetime.datetime.utcnow)


class Mecanico(Base):
    __tablename__ = "tbl_mecanicos"

    id = Column(Integer, Sequence("meecanico_id_seq"), primary_key=True)
    nombre = Column(String(50), nullable=False)


class Falla(Base):
    __tablename__ = "tbl_fallas"

    id = Column(Integer, Sequence("falla_id_seq"), primary_key=True)
    descrip = Column(String,nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("tbl_vehiculos.id"), nullable=False)
    mantenimiento_id = Column(Integer, ForeignKey("tbl_mantenimientos.id"), nullable=False)
    mecanico_id = Column(Integer, ForeignKey("tbl_mecanicos.id"), nullable=False)


class Asignacion(Base):
    __tablename__ = "tbl_asignaciones"

    id = Column(Integer, Sequence("asigna_id_seq"), primary_key=True)
    vehiculo_id = Column(Integer, ForeignKey("tbl_vehiculos.id"), nullable=False)
    conductor_id = Column(Integer, ForeignKey("tbl_conductor.id"), nullable=False)
    fecha_expiracion = Column(Date, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
