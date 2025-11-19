import psycopg2
import os

# --- FUNÇÃO 1: INICIALIZAÇÃO E CRIAÇÃO DA TABELA ---
def setup_database():
    """Conecta ao DB e cria a tabela 'chat_log' se ela não existir."""
    
    # Parâmetros de conexão
    conn_params = {
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
        "database": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        # Adicione o sslmode='require' AQUI se estiver rodando em sua máquina local
        # Exemplo: 'sslmode': 'require'
    }

    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        # SQL para criar a tabela. O "IF NOT EXISTS" garante que não haverá erro
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS chat_log (
                id SERIAL PRIMARY KEY,
                user_question TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_sql)
        conn.commit()
        print("Tabela 'chat_log' verificada/criada com sucesso.")
        
    except Exception as e:
        print(f"Erro ao configurar o banco de dados (setup_database): {e}")
        # É importante levantar o erro aqui para que o deploy falhe se o DB estiver inacessível
        raise 
    finally:
        if conn:
            conn.close()

# --- FUNÇÃO 2: LOG DE CHAT ---
def log_chat(user_question, ai_response):
    """Conecta ao DB e insere o log de chat."""
    
    # Parâmetros de conexão
    conn_params = {
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
        "database": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        # Adicione o sslmode='require' AQUI se estiver rodando em sua máquina local
    }
    
    conn = None
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        sql = """
            INSERT INTO chat_log (user_question, ai_response)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (user_question, ai_response))
        conn.commit()
    except Exception as e:
        # Registra o erro de inserção, mas tenta não quebrar a requisição principal
        print(f"Erro ao inserir log no banco de dados: {e}")
    finally:
        if conn:
            conn.close()