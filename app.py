import sqlite3
import streamlit as st

# Criar tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('usuarios.db')  # Conectar ao banco de dados SQLite (será criado se não existir)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    st.success('Tabela criada com sucesso!')

# Adicionar novo usuário
def adicionar_usuario(nome, email):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Usuario (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    st.success('Usuário adicionado com sucesso!')

# Streamlit
st.title('Adicionar Usuário')

# Formulário para adicionar usuário
nome = st.text_input('Nome do usuário')
email = st.text_input('Email do usuário')

# Botão para criar tabela
# if st.button('Criar Tabela'):
#     criar_tabela()

# Botão para adicionar usuário
if st.button('Adicionar Usuário'):
    adicionar_usuario(nome, email)
