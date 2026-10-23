import streamlit as st
from core.database import engine, Base, get_db
from modules.cadastros.models import Cliente

# Cria as tabelas na base de dados PostgreSQL do Supabase (apenas na primeira execução)
Base.metadata.create_all(bind=engine)

st.title("Bancada Smart - ERP")
st.header("Novo Cliente")

with st.form("form_cliente"):
    nome = st.text_input("Nome do Cliente*")
    telefone = st.text_input("Telefone/WhatsApp*")
    cpf = st.text_input("NIF/CPF")
    
    submit_button = st.form_submit_button("Guardar Cliente")

    if submit_button:
        if not nome or not telefone:
            st.error("Os campos Nome e Telefone são obrigatórios.")
        else:
            db = next(get_db())
            novo_cliente = Cliente(nome=nome, telefone=telefone, nif_cpf=cpf)
            
            try:
                db.add(novo_cliente)
                db.commit()
                st.success(f"Cliente {nome} guardado com sucesso!")
            except Exception as e:
                db.rollback()
                st.error(f"Erro ao guardar cliente: {e}")