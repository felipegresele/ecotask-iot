import psycopg2
import os

# --- FUNÇÃO 1: INICIALIZAÇÃO E CRIAÇÃO DA TABELA ---
def setup_database():
    """Conecta ao DB e cria a tabela 'chat_log' se ela não existir."""
    
    # ⚠️ Nota: Adicione sslmode='require' se estiver rodando localmente!
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    
    try:
        cursor = conn.cursor()
        
        # SQL para criar a tabela. O "IF NOT EXISTS" garante que não haverá erro
        # se você rodar essa função várias vezes.
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS chat_log (
                id SERIAL PRIMARY KEY,
                user_question TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_sql)
        conn.commit() # Salva a criação da tabela no banco
        print("Tabela 'chat_log' verificada/criada com sucesso.")
        
    except Exception as e:
        # Se houver erro de conexão (ex: senha incorreta), isso será capturado
        print(f"Erro ao configurar o banco de dados: {e}")
        
    finally:
        # Garante que a conexão será fechada
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# --- FUNÇÃO 2: SUA FUNÇÃO ORIGINAL DE LOG ---
def log_chat(user_question, ai_response):
    """Conecta ao DB e insere o log de chat."""
    
    # ⚠️ Nota: Adicione sslmode='require' se estiver rodando localmente!
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO chat_log (user_question, ai_response)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (user_question, ai_response))
        conn.commit()
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

# --- COMO USAR ---
# 1. No ponto de entrada principal do seu projeto (por exemplo, app.py), 
# chame setup_database() ANTES de qualquer requisição que chame log_chat().

# Exemplo:
# if __name__ == "__main__":
#     setup_database() # Garante que a tabela existe
#     # Inicia o servidor web ou o loop principal
#     # ...