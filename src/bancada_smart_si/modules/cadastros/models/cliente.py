from sqlalchemy import Column, Integer, String, DateTime, func
from core.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    cpf = Column(String, nullable=False, unique=True, index=True)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    instagram = Column(String, nullable=False)

    criado_em = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
    deletado_em = Column(DateTime(timezone=True))
    